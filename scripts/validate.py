#!/usr/bin/env python3
"""Validate TRIPLE data against the SHACL shapes in shapes/.

Usage (from the repo root, with the venv active):
    python scripts/validate.py                  # iteration ABOXes + examples/ + vocabularies/
    python scripts/validate.py <file> [<file>…]
"""
import glob
import sys
from pathlib import Path

from pyshacl import validate
from rdflib import Graph

ROOT = Path(__file__).resolve().parent.parent


def shapes_graph() -> Graph:
    g = Graph()
    for f in sorted((ROOT / "shapes").glob("*.ttl")):
        g.parse(f, format="turtle")
    return g


def ontology_graph() -> Graph:
    """The TBox is needed as ont_graph so sh:class can see the type hierarchy."""
    g = Graph()
    g.parse(ROOT / "ontology" / "triple.ttl", format="turtle")
    return g


# Iterations whose motivating scenario is about identifiers, and whose exemplar
# data is therefore expected to be conformant. The other iterations use documents
# as vehicles for teaching something else (disciplines, licences, coverage,
# clustering) and carry deliberately partial instances: validating them against a
# publication profile would be a category error, so they are out of scope here.
IDENTIFIER_ITERATIONS = ("01", "04", "05", "06", "07", "08", "10", "11", "12", "19", "20")


def targets(argv: list[str]) -> list[Path]:
    if argv:
        return [Path(a) for a in argv]
    files = [ROOT / "development" / it / "ABOX.ttl" for it in IDENTIFIER_ITERATIONS]
    files = [f for f in files if f.exists()]
    files += sorted(ROOT.glob("examples/**/*.ttl"))
    files += [f for f in sorted((ROOT / "vocabularies" / "serializations" / "ttl").glob("*.ttl"))
              if not f.name.endswith(".metadata.ttl")]
    return files


def main() -> int:
    shapes, onto = shapes_graph(), ontology_graph()
    failed = 0
    for path in targets(sys.argv[1:]):
        data = Graph()
        data.parse(path, format="turtle")
        conforms, _, text = validate(
            data, shacl_graph=shapes, ont_graph=onto, allow_infos=True, allow_warnings=True
        )
        label = str(path.relative_to(ROOT)) if path.is_absolute() else str(path)
        if conforms:
            print(f"  OK       {label}")
        else:
            failed += 1
            n = text.count("Constraint Violation")
            print(f"  FALLITO  {label}  ({n} violazioni)")
            for line in text.splitlines():
                s = line.strip()
                if s.startswith(("Focus Node:", "Message:")):
                    print(f"             {s}")
    print(f"\n{'tutti conformi' if not failed else f'{failed} file non conformi'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
