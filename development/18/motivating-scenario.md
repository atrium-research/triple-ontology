# Motivating Scenario (Iteration 18)

## Name
Enrichment Metadata - Topic Confidence, Structured Keywords and Language Detection

## Description

### Context
The GoTriple pipeline (SCRE) does not merely aggregate metadata: it **enriches** it. Documents are automatically classified against the Discipline vocabulary (with a trust score produced by the classifier), keywords (`knows_about`) are extracted and linked to external knowledge bases with multilingual labels, the text language is detected when providers omit it, and titles and abstracts are machine-translated into additional languages.

The ontology (up to iteration 17) records the *results* of these enrichments (e.g. `sioc:topic` pointing to a Discipline) but not their *metadata*: how confident the classifier was, which URI and labels a keyword carries, which language was detected, and which title/abstract versions are machine translations. This information is required both for auditing the pipeline and for exporting to SKG-IF, whose `provenance` objects carry `associated_with` and `trust` (see `mapping_spec/gotriple-to-skg-if-mapping.md`). This iteration covers the remaining checklist items of issue [#38](https://github.com/atrium-research/triple-ontology/issues/38) (items 1, 3 and 4).

### Objective
1. **Topic confidence**: represent the classifier's trust score for each Discipline assignment.
2. **Structured keywords**: represent `knows_about` entries as first-class terms with a URI and multilingual labels, instead of plain strings.
3. **Language detection and machine translation**: record the language detected by the pipeline and which title/abstract language versions are machine-translated.

## Design Decision: Web Annotation for enrichment provenance

The confidence of an enrichment is a statement *about a statement* ("the assignment of discipline D to document X has trust 0.87"). Among the candidate patterns — RDF-star, RDF reification, a dedicated qualified-relation class, PROV-O activities — this iteration adopts the **W3C Web Annotation model** (`oa:Annotation`), for these reasons:

- `oa:classifying` is the motivation defined by the W3C precisely for "classifying the Target as something", and `oa:tagging` for keyword tagging; machine-generated annotations are within the model's scope.
- Iteration 15 already uses `oa:Annotation` (with `oa:identifying`) for NER mentions: enrichments of the same nature use one consistent pattern.
- Domain/range conformance was verified against the official OA vocabulary: `oa:hasTarget`/`oa:hasBody` have domain `oa:Annotation` and no range constraint; `oa:motivatedBy` ranges over `oa:Motivation`, and both `oa:classifying` and `oa:tagging` are `oa:Motivation` individuals.
- Real-world precedent: text-mining outputs are published as Web Annotations (e.g. Europe PMC).
- Alternatives were rejected because: RDF-star is not supported by the OWL toolchain of this project; plain RDF reification has weak semantics; a bespoke qualified-relation class would mint new terms to replicate what OA standardizes; PROV-O models the process rather than the single assignment and makes queries heavier.

The pattern is **two-level**: the direct triple (`sioc:topic`, `schema:about`) remains for simple queries; the `oa:Annotation` carries the provenance (confidence, creator). The two levels are kept consistent by the pipeline.

Two further reuse decisions, also verified against the official vocabularies:

- The `knows_about` field of the data model revision carries the concepts of the TRIPLE Vocabulary (SSH-LCSH), a multilingual SSH subset of LCSH maintained by the TRIPLE consortium and published on semantics.gr that the enrichment service detected in the resource. The GoTriple API returns them as `{uri, labels}`: the identity is the concept's own URI (`http://semantics.gr/authorities/SSH-LCSH/sh2008122106`), the labels are a denormalised copy for the index. The ontology therefore points at the concept itself with **`schema:about`** (range `skos:Concept`) and mints nothing locally. `schema:knowsAbout` is deliberately **not** used here: Schema.org defines it as an epistemic relation between an *agent* and a topic — a document does not know about something, it is about it. It stays on `triple:Profile`, which is a person or an organization.

- External links depend on what the value is. A **thesaurus concept** already carries, at the authority, a `skos:exactMatch` to the LCSH heading it derives from, and that is the correct relation because both sides are `skos:Concept`. A **producer keyword** (`schema:keywords`, a `schema:DefinedTerm`) that happens to point at an external reference page such as Wikidata uses **`schema:sameAs`** (domain `Thing`, range `URL`) instead: `skos:exactMatch` would entail typing a Wikidata entity as a SKOS concept, which it is not.

## Technical Specification
- `triple:confidence` - `owl:DatatypeProperty`, domain `oa:Annotation`, range `xsd:decimal`; the trust score of the enrichment, between 0 and 1.
- `schema:about` - reused with `rdfs:range skos:Concept`; carries the TRIPLE thesaurus concepts detected in the resource. No TRIPLE property is minted: the earlier `triple:knowsAbout` is retired in 3.0.0.
- A thesaurus concept is cited, not copied: `<http://semantics.gr/authorities/SSH-LCSH/shNNNNNNNN> a skos:Concept` with its `skos:prefLabel` and the `skos:exactMatch` to the LCSH heading it derives from. `schema:keywords` keeps carrying the producer's own keywords, which are free text and have no URI.
- `triple:detectedLanguage` - `owl:DatatypeProperty`, range `xsd:string`; the language tag identified by the pipeline's language-detection service.
- `triple:machineTranslatedLanguage` - `owl:DatatypeProperty`, range `xsd:string` (0 or more); each value is the language tag of the title/abstract versions produced by machine translation. The plain language of each version remains the language tag of the literal; the provider's raw language value is `triple:originalLanguage` (iteration 17). This assumes title and abstract share their translation status per language; should per-string granularity ever be needed, a text-version reification would replace this property.
- Topic assignments keep the direct `sioc:topic` triple and add an `oa:Annotation` with `oa:hasTarget` (the resource), `oa:hasBody` (the Discipline concept), `oa:motivatedBy oa:classifying`, `triple:confidence` and `dcterms:creator` (the GoTriple pipeline, covering SKG-IF `associated_with`). Keyword annotations use `oa:motivatedBy oa:tagging`.

## Examples
- A French article on digital methods in SSH is classified under the *Methods and Statistics* discipline with trust 0.87; the annotation records the score and GoTriple as creator. Its title and abstract exist in French (original), English and Portuguese (machine-translated); the language detector identified `fr`. The enrichment service detected the thesaurus concept *Digital humanities* (`http://semantics.gr/authorities/SSH-LCSH/sh2008122106`, `skos:exactMatch` to LCSH `sh2008122106`) and attached it with an `oa:tagging` annotation; the GoTriple API exposes no trust score for keyword detection, so the annotation records only its creator.
- An English political-science survey report is classified under *Political Science* with trust 0.55 and carries the thesaurus concept *Attitude (Psychology)* (`.../sh85009407`). Nothing is machine-translated.
