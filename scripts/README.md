# Scripts — the repository's entry points

`scripts/` holds the commands you run; `tools/` holds the software they drive.
The contract between the two: **nothing in `tools/` is invoked directly** — every
tool is reached through an entry point here, which knows the paths, the
virtualenv and the arguments. `tools/` can change shape without breaking anyone.

## Setup

The virtualenv lives *inside* this directory (project convention):

```bash
cd scripts
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Activate it before running any script.

## Entry points

| Command | What it does |
|---|---|
| `python merge_iterations.py --output ../ontology/triple.ttl` | Merges every `development/NN/TBOX.ttl` plus `ontology/metadata.ttl` into the consolidated model. **Always pass `--output`**: the bare default writes to the legacy `triple-ontology.ttl` path. |
| `python build.py` *(from repo root)* | Compiles each controlled vocabulary (`vocabularies/serializations/ttl/*.ttl` + its `.metadata.ttl` sidecar + the shared metadata) into `build/`. |
| `python scripts/check_model.py` *(from repo root)* | Model invariants: one comment per term and language, every `triple:` term documented, no new global axioms on foreign terms, every referenced term declared. |
| `python scripts/validate.py` *(from repo root)* | SHACL validation of the exemplar ABOXes, `examples/` and the vocabularies against `shapes/`. |
| `scripts/build_docs.sh [output-base]` | Regenerates **the whole published surface**: the seven documentation pages — the model (SKOS-Reference-style chapters from `ontology/doc/sections/`, figures from `ontology/doc/figures/`) plus the six vocabularies — with the vendored pyLODE fork in `tools/pylode/`, and the landing `index.html` at the root (one card per artefact, via `build_index.py`). Recompiles the vocabularies (`build.py`) first; every page ships with its `static/` and `.ttl`/`.rdf`/`.jsonld` serializations. No argument = preview in `build/docs-preview/` (git-ignored); `ontology/html` = the official pages. |
| `python scripts/build_index.py -o <file>` | The landing page alone — one card per artefact (titles, descriptions, versions, term counts read from `ontology/triple.ttl` and the compiled vocabularies in `build/`, so it can never go stale). Normally driven by `build_docs.sh`. |

## Tools (in `tools/`)

- `tools/pylode/` — the patched pyLODE fork that renders the documentation
  pages. Vendored 2026-08-12; every deviation from upstream is recorded in
  `tools/pylode/PATCHES.md`. Runs on this directory's virtualenv, via
  `build_docs.sh` only.
