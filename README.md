# TRIPLE Ontology

The TRIPLE project, launched in October 2019 and coordinated by the French National Center for
Scientific Research (CNRS), involved 22 partners from 15 European countries. Its primary aim was
to develop the [GoTriple.eu](https://GoTriple.eu) discovery platform, a multilingual access point for discovering and reusing
research artefacts in the social sciences and humanities (SSH).

The TRIPLE Ontology formalises the GoTriple data model using semantic technologies. It addresses
the challenge of managing heterogeneous data aggregated by GoTriple's data processing pipeline
(SCRE), which integrates research artefacts from diverse external sources with varying structures
and formats. The ontology is developed following the [SAMOD](https://essepuntato.it/samod/)
(Simplified Agile Methodology for Ontology Development) methodology: every piece of the model was
introduced by an iteration with a motivating scenario, competency questions and a tested exemplar
dataset.

## Current state

The current release is **[3.1.0](https://github.com/atrium-research/triple-ontology/releases/latest)**.
The ontology ships as **one consolidated model plus six controlled vocabularies**, siblings under
the same root:

| Artefact | Namespace | Prefix |
|---|---|---|
| TRIPLE model | `https://gotriple.eu/ontology/triple/` | `triple:` |
| Discipline | `https://gotriple.eu/ontology/discipline/` | `disc:` |
| ContentType | `https://gotriple.eu/ontology/content-type/` | `ct:` |
| ConditionOfAccess | `https://gotriple.eu/ontology/condition-of-access/` | `coa:` |
| License | `https://gotriple.eu/ontology/license/` | `lic:` |
| ProjectType | `https://gotriple.eu/ontology/project-type/` | `pt:` |
| DDC proxies | `https://gotriple.eu/ontology/ddc/` | `ddc:` |

Concept IRIs use the **production key verbatim** (`disc:musiq`, `ct:typ_article`,
`coa:acr_open-access`): mapping a GoTriple record to the vocabulary is namespace + key, with no
lookup table. The full naming rules are in [`URI-CONVENTIONS.md`](URI-CONVENTIONS.md).

> **Deployment note.** `https://www.gotriple.eu/ontology/triple` currently serves release 2.1.0.
> Until the 3.x pages are deployed, consult the documentation inside this repository
> (`docs/`), which is regenerated and verified at every release.

## How to read this repository

**To see what the ontology is (five minutes):**

1. The [latest release](https://github.com/atrium-research/triple-ontology/releases/latest) —
   its notes summarise the state: breaking changes, new modeling, verification results.
2. `docs/triple/index.html` — the model's documentation page, with every class and
   property anchored. One sibling page per vocabulary (`docs/<vocabulary>/`), and the
   landing index at `docs/index.html`. Open them locally from a clone or from the
   release archive.
3. `docs/triple/triple.ttl` — the consolidated model (structure only, no instance data), and
   `vocabularies/serializations/ttl/` — the vocabulary sources.

**To understand why it is the way it is:**

4. [`CHANGELOG.md`](CHANGELOG.md) — every substantive change has a dated entry with its
   rationale: the reasoned history of the ontology.
5. [`URI-CONVENTIONS.md`](URI-CONVENTIONS.md) — the normative rules: namespaces, minting,
   term identity, external alignment, anchors, versioning, URL handling.
6. `development/NN/` — the 21 SAMOD iterations. Each one records the motivating scenario, the
   competency questions and the tested exemplar behind one piece of the model: if you want to
   know why `triple:isDuplicateOf` exists, read `development/20/`.
7. `shapes/` — the SHACL profile: which identifiers, URLs and links are mandatory for which
   entity.

## Repository structure

* **`development/`** — 21 SAMOD iterations (`01`–`21`), each a complete test case:
  * `motivating-scenario.md` — use case description and examples
  * `informal-competency-questions.md` — natural-language requirements
  * `glossary-of-terms.md` — terminology of the iteration's TBox
  * `formal-competency-questions.md` — the requirements as SPARQL queries
  * `TBOX.ttl` / `ABOX.ttl` — the model and its exemplar data
  * `modelet.graphml` / `modelet.png` — Graffoo diagram (yEd)
* **`docs/`** — the published surface, deployed as-is under `gotriple.eu/ontology/`:
  the landing `index.html` (one card per artefact) plus one directory per artefact
  (`triple/` + the six vocabularies), each with its documentation page, `static/`
  and `.ttl`/`.rdf`/`.jsonld` serializations; `docs/README.md` is the
  **resolution specification** (redirect rules, content negotiation, 404 policy)
  * `docs/triple/` also holds the model **sources**: `triple.ttl` (the canonical
    consolidated model, merged from all iterations), `metadata.ttl` (single
    source of the shared ontology metadata) and `doc/` (the narrative chapters
    and figures of the model page)
* **`vocabularies/serializations/ttl/`** — the six controlled vocabularies, each with a
  `.metadata.ttl` sidecar; compiled into `build/` by `scripts/build.py`
* **`shapes/`** — SHACL shapes (identifiers, URLs, deduplication, per-entity profiles)
* **`patterns/`** — reusable modeling patterns (identifier, controlled vocabularies,
  original values, …)
* **`sparql/`** — mirror of each iteration's formal competency questions
* **`examples/`** — JSON-LD examples of platform data
* **`diagrams/`** — Graffoo diagrams of the consolidated model (being realigned to 3.x)
* **`scripts/`** — the entry points you run (merge, build, validate, docs);
  see `scripts/README.md`
* **`tools/`** — vendored software driven by the scripts, never invoked
  directly: `tools/pylode/` renders the documentation pages
  (deviations from upstream in its `PATCHES.md`)

## Working locally

The Python virtualenv lives inside `scripts/`:

```bash
cd scripts
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# regenerate the consolidated model (default output: ../docs/triple/triple.ttl)
python merge_iterations.py

# checks, from the repository root
cd ..
python scripts/check_model.py    # model invariants (one home per term, no foreign axioms…)
python scripts/validate.py       # SHACL validation of exemplars and vocabularies
python scripts/build.py          # compile the vocabularies into build/
scripts/build_docs.sh            # regenerate all documentation pages + the landing index (preview in build/docs-preview/)
```

At every release the full battery runs: the 172 SPARQL competency questions of the 21 iterations
against the consolidated model, the SHACL profile, the model invariants, and an isomorphism check
between the model and every published serialization.

## Versioning

Semantic versioning, single-sourced from `docs/triple/metadata.ttl` (`owl:versionInfo`); GitHub
releases carry the artefacts and the release notes. Breaking changes are recorded in the
CHANGELOG with their rationale.
