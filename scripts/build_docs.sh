#!/usr/bin/env bash
# Rebuild the model documentation page from ontology/triple.ttl with the vendored
# pyLODE fork (tools/pylode — see tools/pylode/PATCHES.md for the deviations from
# upstream). Uses the scripts/ virtualenv.
#
# Usage:
#   scripts/build_docs.sh                       # preview in build/docs-preview/
#   scripts/build_docs.sh ontology/html/triple  # promote to the official page
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$REPO/build/docs-preview}"
PY="$REPO/scripts/venv/bin/python"
[ -x "$PY" ] || { echo "ERRORE: venv mancante — cd scripts && python -m venv venv && pip install -r requirements.txt"; exit 1; }
PYTHONPATH="$REPO/tools" "$PY" -m pylode.cli "$REPO/ontology/triple.ttl" \
  --sections "$REPO/ontology/doc/sections" \
  --figures  "$REPO/ontology/doc/figures" \
  -o "$OUT/index.html"
echo "Pagina generata in: $OUT"
