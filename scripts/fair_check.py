#!/usr/bin/env python3
"""FAIR assessment of the ontology with FOOPS!, run locally. See HANDOFF.md.

The public instance (https://foops.linkeddata.es) cannot reach gotriple.eu while
the edge accepts TLS 1.3 only, so this runs the same FOOPS! release on the local
JVM. The jar is downloaded once into build/foops/ (git-ignored); the server is
started for the assessment and stopped afterwards, unless one is already up.

Usage (from the repository root):
  python scripts/fair_check.py                     # the deployed canonical IRI
  python scripts/fair_check.py --local             # ontology/triple.ttl, not yet deployed
  python scripts/fair_check.py --local docs/license/ontology.ttl
  python scripts/fair_check.py --uri https://w3id.org/oc/ontology
  python scripts/fair_check.py --min 80            # exit 1 below 80 %
  python scripts/fair_check.py --json out.json     # keep the full report
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

FOOPS_VERSION = "0.4.0"
FOOPS_JAR_URL = ("https://github.com/oeg-upm/fair_ontologies/releases/download/"
                 f"v{FOOPS_VERSION}/fair_ontologies-{FOOPS_VERSION}.jar")
CANONICAL_IRI = "https://gotriple.eu/ontology/triple"
FOOPS_PORT = 8083
STARTUP_TIMEOUT = 120  # seconds; Spring Boot needs ~20 on a laptop

ROOT = Path(__file__).resolve().parent.parent
JAR = ROOT / "build" / "foops" / f"fair_ontologies-{FOOPS_VERSION}.jar"

# On a localhost URL these fail for reasons unrelated to the ontology.
LOCAL_ONLY_FAILURES = {"URI2", "PURL1"}


def ensure_jar() -> Path:
    if JAR.exists():
        return JAR
    JAR.parent.mkdir(parents=True, exist_ok=True)
    print(f"scarico FOOPS! v{FOOPS_VERSION} (~40 MB) in {JAR.relative_to(ROOT)} ...")
    partial = JAR.with_suffix(".part")
    with urllib.request.urlopen(FOOPS_JAR_URL) as resp, open(partial, "wb") as out:
        shutil.copyfileobj(resp, out)
    partial.rename(JAR)
    return JAR


def server_up(port: int) -> bool:
    try:
        urllib.request.urlopen(f"http://localhost:{port}/", timeout=2)
        return True
    except urllib.error.HTTPError:
        return True  # it answered, even if with an error page
    except OSError:
        return False


def start_foops(port: int) -> subprocess.Popen:
    if shutil.which("java") is None:
        sys.exit("java non trovato: serve un JDK >= 11 (per TLS 1.3)")
    log = open(JAR.parent / "foops.log", "w")
    proc = subprocess.Popen(
        ["java", "-jar", f"-Dserver.port={port}", str(JAR)],
        stdout=log, stderr=subprocess.STDOUT,
    )
    deadline = time.monotonic() + STARTUP_TIMEOUT
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            sys.exit(f"FOOPS! si è fermato all'avvio — vedi {log.name}")
        if server_up(port):
            return proc
        time.sleep(1)
    proc.terminate()
    sys.exit(f"FOOPS! non risponde dopo {STARTUP_TIMEOUT}s — vedi {log.name}")


def serve_file(path: Path) -> tuple[str, http.server.HTTPServer]:
    """Serve one file on a free localhost port; return its URL."""
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = functools.partial(Quiet, directory=str(path.parent))
    # Threading: FOOPS! fetches the file from several checks; do not serialise them.
    httpd = http.server.ThreadingHTTPServer(("localhost", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return f"http://localhost:{httpd.server_port}/{path.name}", httpd


def edge_preflight() -> list[str]:
    """Can a non-browser client dereference our IRIs? FOOPS! is one (Java), and so
    is every RDF client. When the edge refuses it, the resolution checks fail for
    reasons that have nothing to do with the ontology — say so up front."""
    problems = []
    for iri in (CANONICAL_IRI, f"{CANONICAL_IRI}/{current_version()}"):
        req = urllib.request.Request(iri, headers={"Accept": "text/turtle",
                                                   "User-Agent": "Java/21"})
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status != 200:
                    problems.append(f"{iri} -> {resp.status}")
        except urllib.error.HTTPError as e:
            problems.append(f"{iri} -> {e.code}")
        except OSError as e:
            problems.append(f"{iri} -> {e}")
    return problems


def current_version() -> str:
    for line in (ROOT / "ontology" / "metadata.ttl").read_text().splitlines():
        if "owl:versionInfo" in line:
            return line.split('"')[1]
    return ""


def assess(uri: str, port: int) -> dict:
    req = urllib.request.Request(
        f"http://localhost:{port}/assessOntology",
        data=json.dumps({"ontologyUri": uri}).encode(),
        headers={"Content-Type": "application/json;charset=UTF-8"},
    )
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.load(resp)


def report(result: dict, local: bool) -> float:
    score = result["overall_score"] * 100
    checks = result["checks"]
    passed = sum(1 for c in checks if c["status"] == "ok")
    print(f"\nscore: {score:.1f} %   ({passed}/{len(checks)} check ok)\n")
    for c in checks:
        cid = c["id"].rsplit("/", 1)[-1]
        mark = "ok" if c["status"] == "ok" else "✗"
        note = "  (atteso su localhost)" if local and cid in LOCAL_ONLY_FAILURES and mark == "✗" else ""
        print(f"  {mark:<3} {cid:<11} {c['total_passed_tests']}/{c['total_tests_run']}  "
              f"{c['explanation'][:95]}{note}")
    return score


def main() -> int:
    ap = argparse.ArgumentParser(description="FAIR assessment with FOOPS!, run locally.")
    target = ap.add_mutually_exclusive_group()
    target.add_argument("--uri", help=f"IRI to assess (default: {CANONICAL_IRI})")
    target.add_argument("--local", nargs="?", const="ontology/triple.ttl", metavar="FILE",
                        help="assess a local file not yet deployed (default: ontology/triple.ttl)")
    ap.add_argument("--min", type=float, metavar="PERCENT",
                    help="exit with status 1 if the score is below this threshold")
    ap.add_argument("--json", type=Path, metavar="FILE", help="write the full FOOPS! report here")
    ap.add_argument("--port", type=int, default=FOOPS_PORT)
    args = ap.parse_args()

    problems = edge_preflight()
    if problems:
        print("ATTENZIONE: l'edge di gotriple.eu respinge un client non-browser:")
        for p in problems:
            print(f"   {p}")
        print("   URI1, CN1, DOC1, VER2 (e con --uri sul dominio, quasi tutto) falliranno\n"
              "   per l'edge, non per l'ontologia. Vedi HANDOFF.md §2.1.\n")

    ensure_jar()
    proc = None if server_up(args.port) else start_foops(args.port)
    httpd = None
    try:
        if args.local:
            path = (ROOT / args.local).resolve()
            if not path.exists():
                sys.exit(f"file non trovato: {path}")
            uri, httpd = serve_file(path)
        else:
            uri = args.uri or CANONICAL_IRI
        print(f"FOOPS! v{FOOPS_VERSION} su {uri}")
        result = assess(uri, args.port)
    finally:
        if httpd:
            httpd.shutdown()
        if proc:
            proc.terminate()
            proc.wait(timeout=30)

    if args.json:
        args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    score = report(result, local=bool(args.local))
    if args.min is not None and score < args.min:
        print(f"\nsotto la soglia: {score:.1f} % < {args.min:.1f} %")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
