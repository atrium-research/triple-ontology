# SAMOD gaps — rationale for this project's fills

The SAMOD paper (Peroni 2016) is deliberately silent on many implementation choices so the methodology can fit any team. This file records *why* the TRIPLE repo made the choices it did, so that a future iteration doesn't accidentally contradict an ADR-level decision.

For each gap we list: **SAMOD says** → **TRIPLE does** → **Why**.

---

## 1. RDF serialization

- **SAMOD says:** any syntax (N3, RDF/XML, Turtle, JSON-LD).
- **TRIPLE does:** Turtle only for TBox, ABox, vocabularies, metadata, patterns. RDF/XML appears only as legacy input to `scripts/convert_vocabularies_to_ttl.py`.
- **Why:** Turtle is the most readable in diffs and the easiest to hand-edit during Phase-1 iteration.

## 2. Reasoner

- **SAMOD says:** any (examples: Pellet, HermiT).
- **TRIPLE does:** Protégé for DL-level consistency checking during authoring; `rdflib` (optionally `owlrl`) for programmatic smoke tests during CI-style validation.
- **Why:** no heavyweight triplestore is required and `rdflib` is already a dependency of `merge_iterations.py`.

## 3. Query engine

- **SAMOD says:** any SPARQL 1.1 engine (examples: Jena, Sesame).
- **TRIPLE does:** `rdflib`'s in-memory `Graph.query`.
- **Why:** ABox sizes per iteration are tiny (tens to hundreds of triples). A standalone triplestore would be overkill.

## 4. Graphical notation

- **SAMOD says:** any (UML, E/R, Graffoo), all optional.
- **TRIPLE does:** Graffoo stencils authored in yEd; `.graphml` as source, PNG export tracked.
- **Why:** Graffoo maps 1:1 to OWL and is the notation used in SAMOD examples; yEd is free and handles the Graffoo palette directly.

## 5. Iteration directory layout

- **SAMOD says:** nothing about file layout.
- **TRIPLE does:** exactly seven files per `development/NN/` (MS, ICQ, GoT, TBOX, ABOX, FCQ, modelet). Nothing else.
- **Why:** predictability. Anyone can diff two iterations and immediately see where the change lives.

## 6. Labels for external ontology references

- **SAMOD says:** labels should be "in at least one language" for documentation.
- **TRIPLE does:** `rdfs:label "prefix:LocalName"@en` — never humanized strings like "Creative Work (Schema.org)".
- **Why:** consistency and clarity when the label appears in diagrams or generated HTML; avoids "which namespace is this from?" ambiguity.

## 7. Glossary scope (TBox only)

- **SAMOD says:** `GoT` is a set of term-definition pairs "in domain language"; does not pin the boundary.
- **TRIPLE does:** the glossary contains only names that appear in `TBOX.ttl`. ABox-only individuals (exemplars) are never listed.
- **Why:** the glossary documents the model, not the data. Listing ABox individuals makes the glossary rot as soon as examples change.

## 8. Controlled-vocabulary pattern

- **SAMOD says:** reuse existing ontologies and patterns.
- **TRIPLE does:** all controlled vocabularies (`content_types`, `conditions_of_access`, `licenses`, `disciplines`, `project_types`) follow the SKOS pattern: `triple:vocabulary_name a skos:ConceptScheme` + `triple:prefix_concept-name a skos:Concept` with `skos:inScheme` and `skos:exactMatch` / `skos:closeMatch` to external KOS (COAR, Creative Commons, UNESCO, LCSH…). Sources live in `vocabularies/serializations/ttl/*.ttl` with `.metadata.ttl` sidecars. Compiled outputs land in `build/` via `scripts/build.py`.
- **Why:** one uniform shape across vocabularies; build step guarantees consistent metadata per vocabulary without hand-maintaining it.

## 9. Merge mechanics (Phase 2)

- **SAMOD says:** merge modelet with current model; collapse semantically-identical entities.
- **TRIPLE does:** `scripts/merge_iterations.py` walks every `development/NN/TBOX.ttl`, merges into one graph, adds ontology metadata, writes Turtle. Collapse is handled by shared entity IRIs — if two iterations reuse the same IRI, they merge automatically. Collapse by *renaming* is a manual pre-step before running the script.
- **Why:** merging is deterministic and reproducible. The script default writes to `ontology/triple-ontology.ttl` for legacy reasons; always pass `--output ../ontology/triple.ttl` to overwrite the canonical file.

## 10. Identifier modeling

- **SAMOD says:** nothing domain-specific.
- **TRIPLE does:**
  - Subclasses of `datacite:Identifier`: only `triple:ID`, `triple:PID`, `triple:OriginalIdentifier` — the three kinds named in class-level axioms. All other kinds are plain `datacite:Identifier` distinguished by their scheme.
  - Value carrier: `litre:hasLiteralValue` (from `http://www.essepuntato.it/2010/06/literalreification/`).
  - Scheme named individuals: `datacite:doi`, `datacite:handle`, `datacite:isbn`, `datacite:issn`, `datacite:uri`, `datacite:local-resource-identifier-scheme`, plus project-specific `triple:full_text_url_schema`, `triple:landing_page_url_schema`, `triple:source_url_schema`, `triple:h2020_scheme`.
- **Why:** GoTriple aggregates heterogeneous sources. Typed subclasses let restrictions on `triple:Document` require *at least one* `triple:ID` and *at least one* `triple:PID`; `litre:hasLiteralValue` is the SPAR-standard carrier.

## 11. Duplicate-document clusters

- **SAMOD says:** nothing domain-specific.
- **TRIPLE does:** class `triple:Cluster` + property `triple:inCluster` (domain `triple:Document`, cardinality exactly 1). Any name like `DocumentCluster` or `belongsToDocumentCluster` is wrong — it does not exist in the ontology.
- **Why:** the deduplication layer of the GoTriple pipeline is an orthogonal concern; keeping `triple:Cluster` short and the property name neutral leaves room for non-Document clusters later.

## 12. Documentation output

- **SAMOD says:** any tool (examples: LODE).
- **TRIPLE does:** per-module HTML under `ontology/modules/html/<Module>/`.
- **Why:** publishing the ontology on https://gotriple.eu/ontology/triple requires static HTML; generating per-module pages avoids one huge monolithic document.

## 13. Ontology-level metadata

- **SAMOD says:** "document it" — at least labels / comments.
- **TRIPLE does:** the exhaustive block documented in `CLAUDE.md` → *Ontology Metadata and Serialization Guidelines*: `owl:versionInfo`, `owl:versionIRI`, `owl:priorVersion`, full `dcterms:*` (creator, contributor, publisher, license, rights, subject, language, format, created, modified, source, bibliographicCitation), `vann:preferredNamespacePrefix`, `vann:preferredNamespaceUri`, `schema:version`, `schema:citation`, `dcat:keyword`, `rdfs:seeAlso`.
- **Why:** the ontology is a citable research artifact — the metadata block satisfies both FAIR principles and the academic citation requirements.

## 14. Milestones

- **SAMOD says:** "released snapshot marking successful completion of a phase"; does not specify storage.
- **TRIPLE does:** Git commits. Suggested message format: `samod(NN): phase P — <short summary>` where `P ∈ {1,2,3}`. A finished iteration is three commits (one per phase).
- **Why:** Git history already exists; adding a parallel milestone tracker would duplicate state.

## 15. Test execution

- **SAMOD says:** formal and rhetorical tests at the end of each phase.
- **TRIPLE does:** formal = parse + optional owlrl closure + SPARQL runner (see `references/validation.md`); rhetorical = human review of MS ↔ ABox alignment and CQ expected-vs-actual.
- **Why:** keeps the CI surface small (just rdflib) while preserving the human judgement that SAMOD considers central.

---

## Things the project has *not* decided (still SAMOD-default)

These are explicit "not decided" points where a future iteration has freedom:

- Dependency management for imported ontologies — currently we *reference* external ontologies (Schema.org, FOAF, Dublin Core, DataCite, COAR, CIDOC CRM…) but do not `owl:imports` them.
- Governance for retiring old iterations — all iterations are kept forever as part of BoT.
- Automated HTML generation tool (LODE vs pyLODE vs WIDOCO) — the per-module HTML in `ontology/modules/html/` is present but the generator is not wired into the skill.
