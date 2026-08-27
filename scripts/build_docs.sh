#!/usr/bin/env bash
# Rebuild the documentation pages — the model plus the six controlled vocabularies —
# with the vendored pyLODE fork (tools/pylode — see tools/pylode/PATCHES.md for the
# deviations from upstream). Every page ships as index.html + static/ + the
# ontology.ttl/.jsonld/.rdf serializations, all emitted by the tool itself.
# Uses the scripts/ virtualenv.
#
# Usage:
#   scripts/build_docs.sh          # preview in build/docs-preview/{triple,discipline,...}
#   scripts/build_docs.sh docs     # promote to the official pages
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$REPO/build/docs-preview}"
PY="$REPO/scripts/venv/bin/python"
[ -x "$PY" ] || { echo "ERRORE: venv mancante — cd scripts && python -m venv venv && pip install -r requirements.txt"; exit 1; }

# 1. Recompile the vocabularies (source + sidecar + shared metadata -> build/*.ttl),
#    so the pages are never rendered from stale input.
(cd "$REPO" && "$PY" scripts/build.py)

# 2. The model page: narrative chapters + per-term figures.
PYTHONPATH="$REPO/tools" "$PY" -m pylode.cli "$REPO/docs/triple/triple.ttl" \
  --sections "$REPO/docs/triple/doc/sections" \
  --figures  "$REPO/docs/triple/doc/figures" \
  -o "$OUT/triple/index.html"

# 3. One page per compiled vocabulary; CamelCase file name -> kebab-case
#    directory (the same rule build.py uses for the vocabulary IRIs).
for src in "$REPO"/build/*.ttl; do
  name="$(basename "$src" .ttl)"
  dir="$(printf '%s' "$name" | sed -E 's/([a-z0-9])([A-Z])/\1-\2/g' | tr '[:upper:]' '[:lower:]')"
  PYTHONPATH="$REPO/tools" "$PY" -m pylode.cli "$src" -o "$OUT/$dir/index.html"
done

# 4. The landing index served at /ontology — one card per artefact,
#    built from the same inputs as the pages.
"$PY" "$REPO/scripts/build_index.py" -o "$OUT/index.html"

echo "Pagine generate in: $OUT"
