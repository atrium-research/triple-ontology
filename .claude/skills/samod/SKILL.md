---
name: samod
description: Use this skill when working on TRIPLE ontology SAMOD iterations — creating or extending a `development/NN/` iteration, authoring its 7 artifacts (motivating scenario, ICQ, glossary, TBOX, ABOX, FCQ, modelet diagram), merging a modelet into the consolidated `ontology/triple.ttl`, running the three SAMOD tests (model / data / query), or refactoring with the project's conventions (`prefix:LocalName` labels, SKOS controlled-vocabulary pattern, external alignments). Trigger on phrases like "new iteration", "SAMOD", "add a modelet", "refactor the TBOX", "run CQs", "merge iterations". The skill grounds the canonical Peroni 2016 methodology in the concrete tooling choices this repo has standardized (Turtle, Graffoo/yEd, `merge_iterations.py`, glossary-TBox-only rule).
---

# SAMOD — ontology development workflow for TRIPLE

SAMOD (Peroni, 2016) is the iterative methodology used to build the TRIPLE ontology. The standard prescribes *what* to do; this skill locks in *how* this repository does it.

## 0. Before you start

- Canonical methodology reference: https://essepuntato.it/samod/ (paper: DOI `10.6084/m9.figshare.3189769`).
- Canonical project conventions: `CLAUDE.md` (file templates, label/naming rules, metadata block) and `SAMOD-METHODOLOGY.md` (project-flavored summary).
- **Always activate the venv before running scripts:** `source scripts/venv/bin/activate` (the venv lives *inside* `scripts/`, not at repo root).

## 1. SAMOD in one page

### Terminology (use these exact names)

| Symbol   | Meaning                                                                   | File in this repo                                |
| -------- | ------------------------------------------------------------------------- | ------------------------------------------------ |
| MS       | Motivating Scenario — NL description + examples                           | `development/NN/motivating-scenario.md`          |
| CQ       | Informal Competency Questions — NL requirements                           | `development/NN/informal-competency-questions.md`|
| GoT      | Glossary of Terms — TBox terms only (no ABox individuals)                 | `development/NN/glossary-of-terms.md`            |
| TBox     | Formal OWL 2 model (classes, properties, restrictions)                    | `development/NN/TBOX.ttl`                        |
| ABox     | Exemplar RDF dataset implementing the MS examples                         | `development/NN/ABOX.ttl`                        |
| SQ       | SPARQL 1.1 queries formalizing each CQ                                    | `development/NN/formal-competency-questions.md`  |
| Modelet  | The stand-alone model for iteration N (diagram + TBox)                    | `development/NN/modelet.graphml` / `.png`        |
| Test Case T_n | 6-tuple (MS, CQ, GoT, TBox, ABox, SQ) for iteration N                | the whole `development/NN/` directory            |
| BoT      | Bag of Test Cases — all T_1 … T_n                                         | `development/` (the set of iteration dirs)       |
| Current Model | TBox released at end of iteration N-1                                | `ontology/triple.ttl` (+ `ontology/modules/*`)   |

### The three phases (applied *per iteration*)

1. **Define a new test case** — write MS → CQ → GoT → design modelet → author TBox + ABox → write SQ → run Model / Data / Query tests → commit T_n.
2. **Merge** modelet with current model — integrate axioms, collapse semantically-identical entities, update *all* prior T_i in BoT, rerun formal tests.
3. **Refactor** current model — add alignments, documentation, inferencing-aware constructs; rerun *all* tests on *all* T_i.

### Core design principles (Phase 1)

- **7 ± 2 entities per modelet.** If bigger, split into two iterations.
- **Middle-out.** Start from concrete entities in MS; generalize/specialize later.
- **Self-explanatory IRIs.** Local names readable without `rdfs:label`.
- **Reuse patterns.** Check `patterns/` first (identifier, date, language, spatial/temporal coverage, person-organization, status).

### One home per term

The same term is declared in many iterations — `triple:Document` in fifteen of them, the identifier
schemes in nine — because every iteration must run its own three tests on `TBOX.ttl + ABOX.ttl` alone,
with no imports. That duplication is deliberate and stays. What must **not** be duplicated is the
*annotation*, because `merge_iterations.py` unions the iterations and two different `rdfs:comment` on
the same term become two comments in the consolidated model, and the documentation generator renders
both.

The rule:

- **The annotation of a term — `rdfs:label`, `rdfs:comment` — is written in exactly one iteration:
  the one that introduces it.** Never re-annotate a term an earlier iteration already documents; if the
  definition needs to change, change it *there* and leave the other iterations alone.
- Every other iteration that uses the term declares **only what its own tests need**: the type, and the
  local axioms it introduces (a restriction on its own class, a `rdfs:range` on a property it mints).
  A bare `foaf:Person rdf:type owl:Class .` is the normal, correct form.
- **Never assert `rdfs:domain`, `rdfs:range` or `rdfs:subPropertyOf` on a term outside the `triple:`
  namespace.** Those are global statements about somebody else's property: `schema:knowsAbout` was given
  `rdfs:range skos:Concept`, which contradicts Schema.org's own `rangeIncludes Text, Thing, URL` and typed
  every value of that property, everywhere, as a SKOS concept. Constrain the value **per class**, with an
  `owl:allValuesFrom` restriction, or — better, when it must actually be checked — in `shapes/`.
- Vocabulary individuals an ABox uses (disciplines, project types, identifier schemes) **must be declared
  in that iteration's own TBox or ABox**, with their label, or the iteration's competency questions
  return nothing: the vocabulary files are not part of the iteration graph.

`scripts/check_model.py` enforces the first three; run it after every merge.

### The three tests (run at the end of Phase 1, then again in Phases 2 and 3)

| Test       | Formal requirement                          | Rhetorical requirement                      |
| ---------- | ------------------------------------------- | ------------------------------------------- |
| Model test | TBox consistent (reasoner)                  | TBox covers MS; vocabulary is appropriate   |
| Data test  | TBox + ABox consistent                      | ABox fully describes MS examples            |
| Query test | SPARQL wellformed; executes on TBox + ABox  | SQ answers map to CQ expected outcomes      |

Formal = computable. Rhetorical = human-reviewed. In Phase 2 we run **only formal** tests across the whole BoT; in Phase 3 we run **all requirements** across the whole BoT.

## 2. Project fills for SAMOD's deliberate gaps

SAMOD is silent on tooling — this repo has already decided. Do *not* re-open these decisions inside an iteration; propose changes as cross-cutting ADRs instead.

| SAMOD gap                      | TRIPLE project convention                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------- |
| RDF serialization              | **Turtle** (`.ttl`) for all TBox/ABox/vocabularies                                              |
| Reasoner                       | Protégé (manual check) + `rdflib` parse-load (programmatic smoke test)                          |
| SPARQL engine                  | `rdflib` Graph.query (no separate triplestore needed for tests)                                 |
| Graphical notation             | **Graffoo** authored in **yEd** — `modelet.graphml` + PNG export                                |
| Iteration layout               | Fixed 7 files per `development/NN/` (see table above); no extra files                           |
| External references — labels   | **`prefix:LocalName`** only (e.g. `rdfs:label "schema:Dataset"@en`)                             |
| Glossary scope                 | **TBox names only.** Never list ABox exemplars in `glossary-of-terms.md`.                       |
| Controlled vocabularies        | SKOS pattern: `triple:vocabulary_name` ConceptScheme + `triple:prefix_concept-name` Concepts with `skos:exactMatch`/`closeMatch` to external KOS. Sources live in `vocabularies/serializations/ttl/*.ttl` with `.metadata.ttl` sidecars; compiled outputs land in `build/` via `scripts/build.py`. |
| External ontology alignment    | `skos:exactMatch` / `skos:closeMatch` / `rdfs:subClassOf` on TBox classes; link in `Documentation`-phase metadata                                                                         |
| Merge (Phase 2)                | `scripts/merge_iterations.py` — **warning**: its default output is the legacy `ontology/triple-ontology.ttl`. Always pass `--output ../ontology/triple.ttl` to overwrite the canonical file. |
| Milestones                     | Git commits at the end of each SAMOD phase (`samod: iter NN phase 1 done` style)                |
| Documentation output           | Per-module HTML under `ontology/modules/html/<Module>/`                                         |
| Ontology metadata              | The exhaustive block (`dcterms:*`, `vann:*`, `schema:citation`, `owl:versionInfo`, `owl:priorVersion`) documented in `CLAUDE.md` → *Ontology Metadata and Serialization Guidelines* |
| Identifier value carrier       | **`litre:hasLiteralValue`** (from `http://www.essepuntato.it/2010/06/literalreification/`) — *not* `datacite:hasIdentifierValue`. |
| Identifier typing              | **No identifier subclasses.** Every identifier is a plain `datacite:Identifier` told apart by its `datacite:usesIdentifierScheme`. Adding a new kind of identifier means adding one scheme individual, declared in the consolidated ontology — never a class. |
| Duplicate-document clustering  | Class **`triple:Cluster`**, property **`triple:inCluster`** (exactly 1 per Document). There is *no* `DocumentCluster` / `belongsToDocumentCluster`. |

## 3. Phase 1 — Define a new test case

Concrete sequence when the user asks for a new iteration N:

1. **Scope check.** Confirm with the user: (a) iteration number (next free under `development/`), (b) MS name, (c) whether it extends or refactors a previous iteration. If MS covers more than ~7 classes, propose splitting *before* creating files.
2. **Create the directory.** `mkdir development/NN` and scaffold the seven files using the ready-to-paste skeletons in `references/templates.md` (motivating scenario, glossary, informal and formal competency questions, TBOX, ABOX, modelet).
3. **Write MS first.** `motivating-scenario.md` must contain: Name, General Description, Technical Specification, Examples. Examples must be concrete enough to become ABox instances — abstract "user wants to search" is too vague.
4. **Write CQs.** Number them `CQ_NN.1`, `CQ_NN.2`… with identifier / question / expected outcome / result / based-on-example. Each CQ must be answerable from the MS examples alone.
5. **Write GoT.** List only classes / object properties / data properties that will appear in `TBOX.ttl`. External terms use `prefix:LocalName` with a short definition. **Do not** list any named individual that only appears in ABox.
6. **Design the modelet.** Open `modelet.graphml` in yEd using Graffoo stencils. Keep it ≤ 9 entities. Export PNG to `modelet.png`. If useful, run `scripts/ttl_to_graphml_classes.py` after the TBox stabilizes to sync the diagram.
7. **Author TBox.** Turtle, with the project prefixes. Every class/property needs `rdfs:label` using `prefix:LocalName` for externals and a plain label for `triple:*`. Add `rdfs:comment` in at least English. Align with external ontologies using `skos:exactMatch` / `rdfs:subClassOf`.
8. **Author ABox.** One instance per MS Example. Use URIs under `https://gotriple.eu/<collection>/<slug>`. Every entity should be typed (`a SomeClass`). Respect the identifier / keyword / language / place patterns — if in doubt, open `patterns/` and follow the relevant `.ttl`.
9. **Write SPARQL (SQ).** In `formal-competency-questions.md`, one section per CQ with: natural-language restatement, the SPARQL query (with all `PREFIX` declarations), expected result mirroring the ABox.
10. **Run the three tests.** See §5.
11. **Commit.** A single commit for T_n: `samod(NN): phase 1 — define test case <name>`.

## 4. Phase 2 — Merge

Goal: integrate modelet_N into the current consolidated model and keep the whole BoT passing.

1. Inspect `ontology/triple.ttl` and `ontology/modules/serializations/*.ttl` for entities that semantically overlap with modelet_N. Typical overlaps: identifier patterns, agents, concepts, dates — resolve to the existing name.
2. **Rename in iteration N** if collapsing is needed. Update `TBOX.ttl`, `ABOX.ttl`, the SPARQL, the GoT and the diagram.
3. Run merge:
   ```bash
   source scripts/venv/bin/activate
   cd scripts
   python merge_iterations.py --output ../ontology/triple.ttl
   ```
   The default path is legacy (`triple-ontology.ttl`) — always pass `--output` explicitly.
4. Re-run **formal** tests (model / data / query) on every T_i in `development/`. If any T_i fails because entity names changed, refactor that T_i's ABox / SPARQL to the new names (Phase 2 *allows* changing older test cases; Phase 1 does not).
5. Regenerate the per-module serializations and check the invariants:
   ```bash
   python scripts/check_model.py      # one comment per term, triple: terms documented, no range on foreign properties
   python scripts/build_modules.py    # ontology/modules/serializations/*.ttl are generated, never hand-edited
   ```
   A module's only hand-written part is its sidecar `ontology/modules/serializations/<M>.metadata.ttl`:
   the module's own title/description/abstract, plus the terms it must carry that are not reachable
   from the class through the model and the shapes.
6. Commit: `samod(NN): phase 2 — merge into consolidated model`.

## 5. Phase 3 — Refactor

Apply these checks across the whole BoT:

- Every TBox class/property carries `rdfs:label` (`prefix:LocalName` for externals) and `rdfs:comment` in English.
- External alignments present via `skos:exactMatch` / `closeMatch` / `rdfs:subClassOf` / `owl:equivalentClass` where appropriate (do *not* assert equivalence lightly — use exactMatch for SKOS concepts, equivalentClass only when semantics truly coincide).
- Controlled-vocabulary individuals follow the SKOS pattern (ConceptScheme + Concepts, `skos:inScheme`, external match).
- Ontology-level metadata block in `ontology/triple.ttl` updated: `owl:versionInfo`, `owl:versionIRI`, `owl:priorVersion`, `dcterms:modified`, `schema:version`, `schema:citation`. See `CLAUDE.md` for the full property list.
- `CHANGELOG.md` updated with the new iteration's additions / breaking changes.
- Re-run **all** tests (formal + rhetorical) on all T_i.
- Commit: `samod(NN): phase 3 — refactor and align`.

## 6. Running the three tests

Minimum commands (venv active, run from repo root):

```bash
# Parse / consistency smoke test per iteration
python - <<'PY'
from rdflib import Graph
g = Graph()
g.parse("development/NN/TBOX.ttl", format="turtle")
g.parse("development/NN/ABOX.ttl", format="turtle")
print(f"Triples: {len(g)}")
PY

# Run every SPARQL query from the iteration's formal-competency-questions.md
# (extract the queries or keep a sidecar .rq file per CQ; see references/validation.md)
```

For the *rhetorical* dimension, validation is human: read the MS + ABox side by side and ask, "would a new reader understand the model from these names alone?" If not, rename before closing Phase 3.

Detailed validation commands and a parse-loop for running every iteration's SPARQL: see `references/validation.md`.

## 7. Pitfalls seen in this repo

- **Glossary leak.** Do not put ABox individuals in `glossary-of-terms.md`. Only TBox names.
- **Wrong merge target.** `merge_iterations.py` with no arguments writes to `triple-ontology.ttl`, *not* the canonical `triple.ttl`. Always pass `--output`.
- **`schema:` version confusion.** The current ontology declares `@prefix schema: <https://schema.org/>` (HTTPS). Match that exactly when writing ABox.
- **Stringy fillers for typed properties.** `schema:publisher`, `schema:provider`, `schema:spatialCoverage`, `schema:inLanguage`, `schema:keywords` all have *class* ranges (`foaf:Person`/`Organization`, `schema:Place`, `schema:Language`, `schema:DefinedTerm`). Never use a literal where an instance is required.
- **Identifier modeling.** Never mint an identifier subclass: `triple:ID`, `triple:PID`, `triple:OriginalIdentifier`, `triple:DOI` and the others were retired in 3.0.0. Write `[ a datacite:Identifier ; datacite:usesIdentifierScheme <scheme> ; litre:hasLiteralValue "…" ]`, always asserting the scheme. The value carrier is `litre:hasLiteralValue` from `http://www.essepuntato.it/2010/06/literalreification/` — `datacite:hasIdentifierValue` does not exist in the DataCite ontology.
- **Cluster naming.** `triple:Cluster` + `triple:inCluster`. No `DocumentCluster` / `belongsToDocumentCluster`.
- **Labels for external references.** Always `prefix:LocalName` — never humanized strings like "Creative Work (Schema.org)".

## 8. References

- `references/templates.md` — ready-to-paste skeletons for the 7 iteration files.
- `references/validation.md` — formal test commands and SPARQL-harvest script.
- `references/gaps.md` — detailed rationale for each project fill-in of a SAMOD gap.
- `references/metadata.md` — the ontology metadata block for standalone serializations, and the version-management rules.
- `CLAUDE.md` in repo root — canonical project conventions.
- `SAMOD-METHODOLOGY.md` in repo root — project-flavored methodology summary.
- Peroni, S. (2016). *SAMOD: an agile methodology for the development of ontologies.* https://essepuntato.it/samod/ · DOI `10.6084/m9.figshare.3189769`.
