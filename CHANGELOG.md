# Changelog - TRIPLE Ontology Development

This file tracks all changes and additions to the TRIPLE ontology following the SAMOD methodology.

## Format

Each entry follows this structure:
- **Date**: When the change was made
- **Iteration**: Which iteration was affected
- **Type**: [Addition | Modification | Refactoring | Documentation]
- **Description**: What was changed and why
- **Author**: Who made the change

---

## [Unreleased]

### 2026-08-10 - Breaking: vocabulary concepts move to their production key, identifier nodes retired

**Type**: Refactoring (breaking — every controlled-vocabulary IRI changes)

**Iteration**: none; `vocabularies/`, `patterns/`, and the ABOXes of iterations 07, 17, 18 and 19

**Description**:
Every concept carried two IRIs: the concept itself, named after its English label, and an empty `datacite:Identifier` node named after the key the platform actually emits — `disc:musicology_and_performing_arts` beside `disc:musiq`, `ct:article` beside `ct:typ_article`, `acc:open_access` beside `acc:acr_open-access`. Checked over 4,000 documents from `api.gotriple.eu`: in all four vocabularies **the identifier's local name is exactly the value production emits**. The concept lived at the IRI nobody uses, and the IRI everyone uses was a dead end.

The concept now lives at the production key. Mapping a harvested record becomes string concatenation — namespace + value — with no lookup table and no join. The cost is the stutter in `ct:typ_article` and `lic:lic_cairn`, accepted deliberately: production is not internally consistent (see below), and only a verbatim key keeps concatenation working for every value rather than most of them.

**The identifier nodes were also invalid.** `tsh:IdentifierShape` requires every `datacite:Identifier` to carry exactly one `datacite:usesIdentifierScheme` and one `litre:hasLiteralValue`; all 73 nodes had neither. Running the shapes over the vocabularies produced 146 violations — nothing had reported them because `scripts/validate.py` covered only the iteration ABOXes and `examples/`. It now covers `vocabularies/serializations/ttl/*.ttl` as well, and all six files conform.

**`other` and `undefined` keep their bare form.** Production emits them without a prefix — never `acr_other`, `typ_undefined`, `lic_other` — across all three fields and every one of the 4,000 documents. Their identifiers in the vocabulary said otherwise, so for those six concepts it is the identifier that was wrong, and the identifier is what disappears.

**The code survives as `skos:notation`.** Until now the code existed nowhere as a literal: it was only the local name of the dead-end IRI, recoverable solely by string surgery on an IRI. `?c skos:notation "musiq"` now answers directly.

**SKOS labelling on every concept.** `skos:prefLabel` mirrors `rdfs:label` and `skos:definition` mirrors `rdfs:comment` — added, not substituted. SKOS-aware consumers (thesaurus browsers, semantics.gr) read the SKOS properties and saw unnamed concepts; pyLODE and generic RDF tools read `rdfs:label`/`rdfs:comment` and would lose the display name if those were dropped. The mirroring applies to the individuals only: the bridge classes and `skos:closeMatch` itself keep their plain annotations.

**The 27 disciplines have a definition for the first time.** None of the 81 individuals in the vocabulary carried an `rdfs:comment`, in the vocabulary whose IRIs are now the least self-explanatory. One-sentence scope notes were drafted in English, in the style of the other three vocabularies; they are new editorial content and want review. The five concepts whose labels exist only in English (`ct:typ_semantic-artefact`, `ct:typ_sound`, `ct:typ_video`, `acc:acr_embargoed-access`, `acc:acr_metadata-only-access`), and the missing `de` and `it` labels on ContentType, AccessCondition and License, are left as they are: translations of a multilingual controlled vocabulary are the consortium's, not this repository's.

**The 54 Dewey proxies left the Discipline vocabulary.** They were typed `triple:Discipline`, which asserted that "Dewey class 78 (Music)" is one of GoTriple's disciplines and inflated the vocabulary from 27 members to 81. They are now `skos:Concept` in their own scheme at `https://gotriple.eu/ontology/triple/ddc`, with IRIs built from the notation (`ddc:78`, `ddc:930.1`), the label split out of the packed string `"Dewey Decimal Classification: 78 (Music)"` into `rdfs:label "Music"@en` plus `skos:notation "78"`. The scheme resource itself is redeclared: it had been removed in `f223b29` together with the other `skos:ConceptScheme` declarations, leaving 54 `rdfs:isDefinedBy` pointing at nothing for eight months. They stay local proxies because there is nowhere to point: `dewey.info` does not respond at all, `id.oclc.org/worldcat/ddc/780` and `classify.oclc.org` return 404 — OCLC withdrew its DDC linked-data service and no dereferenceable DDC IRI exists.

**36 of the 54 DDC notations are truncated and were left alone.** A DDC number has at least three digits: Music is 780, not 78. Normalising mechanically also collides — `ddc_12` is labelled "Philosophy of Humanity" and would become `120`, which already exists with the official caption "Epistemology, causation, humankind". Correcting them is content work against a licensed classification, so the notations are carried over unchanged and the defect is stated in the scheme's own `rdfs:comment` rather than hidden.

**Also**: `vann:preferredNamespacePrefix` in the five vocabulary sidecars declared `discipline`, `contenttype`, `accesscondition`, `license`, `projecttype` while the files themselves bind `disc:`, `ct:`, `acc:`, `lic:`, `pt:` — aligned to the prefixes actually in use.

**Regenerated**: `build/` (six vocabularies now, `ddc` included) and the HTML documentation for all six with the patched pyLODE. The consolidated model and the six entity module serializations are byte-for-byte unaffected — verified by graph isomorphism, since no vocabulary concept appears in them.

**Crosswalk**

**Discipline** (27 concepts)

| before | after |
|---|---|
| `disc:archaeology_and_prehistory` | `disc:archeo` |
| `disc:architecture_and_space_management` | `disc:archi` |
| `disc:art_and_art_history` | `disc:art` |
| `disc:biological_anthropology` | `disc:anthro-bio` |
| `disc:classical_studies` | `disc:class` |
| `disc:communication_sciences` | `disc:info` |
| `disc:cultural_heritage_and_museology` | `disc:museo` |
| `disc:demography` | `disc:demo` |
| `disc:economies_and_finances` | `disc:eco` |
| `disc:education` | `disc:edu` |
| `disc:environmental_studies` | `disc:envir` |
| `disc:gender_studies` | `disc:genre` |
| `disc:geography` | `disc:geo` |
| `disc:history` | `disc:hist` |
| `disc:history,_philosophy_and_sociology_of_sciences` | `disc:hisphilso` |
| `disc:law` | `disc:droit` |
| `disc:linguistics` | `disc:lang` |
| `disc:literature` | `disc:litt` |
| `disc:management` | `disc:manag` |
| `disc:methods_and_statistics` | `disc:stat` |
| `disc:musicology_and_performing_arts` | `disc:musiq` |
| `disc:philosophy` | `disc:phil` |
| `disc:political_science` | `disc:scipo` |
| `disc:psychology` | `disc:psy` |
| `disc:religions` | `disc:relig` |
| `disc:social_anthropology_and_ethnology` | `disc:anthro-se` |
| `disc:sociology` | `disc:socio` |

**ContentType** (23 concepts)

| before | after |
|---|---|
| `ct:article` | `ct:typ_article` |
| `ct:bibliography` | `ct:typ_bibliography` |
| `ct:blog_post` | `ct:typ_blog-post` |
| `ct:book` | `ct:typ_book` |
| `ct:book_part` | `ct:typ_book-part` |
| `ct:conference` | `ct:typ_conference` |
| `ct:dataset` | `ct:typ_dataset` |
| `ct:image` | `ct:typ_image` |
| `ct:learning_object` | `ct:typ_learning-object` |
| `ct:manuscript` | `ct:typ_manuscript` |
| `ct:map` | `ct:typ_map` |
| `ct:other` | `ct:other` *(unchanged)* |
| `ct:periodical` | `ct:typ_periodical` |
| `ct:preprint` | `ct:typ_preprint` |
| `ct:report` | `ct:typ_report` |
| `ct:review` | `ct:typ_review` |
| `ct:semantic_artefact` | `ct:typ_semantic-artefact` |
| `ct:software` | `ct:typ_software` |
| `ct:sound` | `ct:typ_sound` |
| `ct:text` | `ct:typ_text` |
| `ct:thesis` | `ct:typ_thesis` |
| `ct:undefined` | `ct:undefined` *(unchanged)* |
| `ct:video` | `ct:typ_video` |

**AccessCondition** (10 concepts)

| before | after |
|---|---|
| `acc:all_rights_reserved` | `acc:acr_all-rights-reserved` |
| `acc:closed_access` | `acc:acr_closed-access` |
| `acc:embargoed_access` | `acc:acr_embargoed-access` |
| `acc:free_access` | `acc:acr_free-access` |
| `acc:metadata_only_access` | `acc:acr_metadata-only-access` |
| `acc:open_access` | `acc:acr_open-access` |
| `acc:other` | `acc:other` *(unchanged)* |
| `acc:public_domain` | `acc:acr_public-domain` |
| `acc:restricted_access_or_use` | `acc:acr_restricted-access-or-use` |
| `acc:undefined` | `acc:undefined` *(unchanged)* |

**License** (13 concepts)

| before | after |
|---|---|
| `lic:cairn` | `lic:lic_cairn` |
| `lic:clarin-aca` | `lic:lic_clarin-aca` |
| `lic:clarin-res` | `lic:lic_clarin-res` |
| `lic:clarin_pub` | `lic:lic_clarin-pub` |
| `lic:creative_commons` | `lic:lic_creative-commons` |
| `lic:elra_licences` | `lic:lic_elra` |
| `lic:meta-share` | `lic:lic_meta-share` |
| `lic:microsoft_public_licence` | `lic:lic_ms-pl` |
| `lic:microsoft_reciprocal_licence` | `lic:lic_ms-rl` |
| `lic:open_data` | `lic:lic_open-data` |
| `lic:open_source` | `lic:lic_open-source` |
| `lic:other` | `lic:other` *(unchanged)* |
| `lic:undefined` | `lic:undefined` *(unchanged)* |

The 54 DDC proxies move from `disc:ddc_<code with underscores>` to `ddc:<notation>`: `disc:ddc_78` → `ddc:78`, `disc:ddc_930_1` → `ddc:930.1`.

**Author**: Alessandro Bertozzi


### 2026-08-10 - Addition: the Cairn licence, and what a 9,949-document check found

**Type**: Addition

**Iteration**: none; `vocabularies/serializations/ttl/License.ttl`

**Description**:
Every value the GoTriple API emits for `conditions_of_access`, `license` and `additional_type` was checked against the vocabulary that is supposed to contain it, over a sample of 9,949 documents drawn from ten queries. Three findings, one of which is fixed here.

**`lic_cairn` was missing** — 82 occurrences, from Isidore (59), HAL and Isidore (10) and BASE and Isidore (3), always normalised from an original value of `"Cairn"`. Added as `lic:lic_cairn`: the terms of use of the Cairn.info platform, which are the publisher's own conditions rather than a standard open licence, so no external alignment. With it, `conditions_of_access` and `license` are fully covered: every value in production has a concept.

**`typ_audio` is a normalisation bug, not a missing concept.** Two documents, both from Canal-U, both with `original_document_types: ["Sound"]` — and the vocabulary already has `ct:typ_sound`, identifier `typ_sound`, aligned to COAR `c_18cc` (Sound). Adding `typ_audio` would mint a duplicate of a concept that exists. It belongs in the normalisation pipeline, not here.

**Two identifier conventions coexist in production, and this is the one to watch.** For every concept the API emits the concept's *identifier* — `acr_open-access`, `lic_creative-commons`, `typ_article` — except for `other` and `undefined`, where it emits the *local name*, while their identifiers would be `acr_other`, `acr_undefined`, `lic_other`, and so on. It is not rare: across the sample, `other` and `undefined` account for 4,901 and 3,458 values on access conditions, 524 and 9,433 on licences, 2,097 and 68 on types. Any mapping that resolves values by identifier alone will silently drop them. Recorded here because it is a fact about the data that the ontology cannot fix on its own.

**Author**: Alessandro Bertozzi


### 2026-08-10 - Decision: w3id IRIs for the resources, one named graph per document

**Type**: Documentation (decision record — nothing in the repository implements it yet)

**Iteration**: none yet; affects every ABOX and the published data

**Description**:
Recorded here because it was agreed in conversation and written nowhere. Verified against a real QLever instance before writing it down, because two of the assumptions turned out to be wrong.

**Two namespaces, on purpose.** The ontology keeps `https://gotriple.eu/ontology/triple/` — the request was explicit — because that is the namespace of the *terms*: `triple:Document`, `triple:hasContentType`. The *resources* move to `https://w3id.org/gto/`. They are different kinds of thing with different lifecycles: the term namespace is versioned and stable by contract, while resource IRIs are minted continuously and must survive independently of an ontology release. The exemplar ABOXes currently mint 74 resources inside the term namespace (`…/ontology/triple/document_1` next to `…/ontology/triple/Document`), which is the anomaly this removes.

**The pattern**:

    https://w3id.org/gto/{type}/{reference}

- `gto` is the authority segment. It is free — checked — and registering it means a pull request to `perma-id/w3id.org`. Longest lead time of anything here and the least reversible: the prefix is forever.
- `{type}` is the entity type spelled out: `document`, `dataset`, `media`, `semantic-artefact`, `project`, `profile`. Not abbreviated — `doc` is reserved by the UKGovLD pattern for "the document *about* the thing", a different referent.
- `{reference}` is the ARK name **without the NAAN**, so `<https://w3id.org/gto/document/x54g7>` and `"ark:/12345/x54g7"` share their last segment by construction. Minted independently they would drift; the rule is what keeps them tied, and it is checkable in SPARQL.

The `id` / `doc` distinction and its 303 are **deferred, not rejected**. The object IRI does not change when they arrive; only the HTTP behaviour does.

**One named graph per document, named after the document.** The graph that holds a document's assertions carries **the document's own IRI** — no suffix, no separate record resource:

    GRAPH <https://w3id.org/gto/document/x54g7> {
        <https://w3id.org/gto/document/x54g7> a triple:Document ; … }

The requirement it answers is deletion: one URI, one operation, the whole subgraph gone. Naming the graph after the document means the thing to delete and the handle to delete it with are the same string, with no mapping to build or look up. The URI then denotes both the document and its graph, which is a real ambiguity — but the same one already accepted by not separating object from record, and SPARQL keeps the two roles apart positionally, so no query is ever ambiguous.

**Three containment rules, without which the deletion is not clean**:
- Everything the document asserts lives **inside its graph**, enrichment annotations included. An `oa:Annotation` in a separate graph would survive the delete and point at a document that no longer exists.
- Identifiers are **blank nodes**. They have no identity of their own, they live in the document's graph and disappear with it — which is the argument for not giving them IRIs at all.
- The **default graph holds the ontology and the vocabularies only**. Put a document index there and `DROP GRAPH` will not touch it, which is the two-step deletion this design exists to avoid.

**A known limit, and it is deliberate.** Deleting a document removes what *it* asserts, not the references other graphs make *to* it — a `schema:mentions` from another document, a cluster that listed it. Those survive as dangling IRIs. They are assertions belonging to other records, and removing them silently would edit someone else's data.

**Verified on QLever** (`adfreiburg/qlever`, build 65f84b4), which is the store in use — nine tests on a fixture with two documents, blank-node identifiers, an annotation, and ontology plus vocabulary in the default graph:
- the default graph is the **union** of the named graphs: a query with no `GRAPH` clause finds a document that lives inside one. The existing competency questions keep working unchanged after partitioning — this was the finding that could have multiplied the work and did not;
- the same IRI works as graph name and as subject in one query, and `SELECT DISTINCT ?g WHERE { GRAPH ?g { ?g a triple:Document } }` lists the document graphs by exploiting the coincidence;
- `PUT ?graph=<uri>` replaces the graph integrally — the stale annotation disappeared with it — and `DELETE ?graph=<uri>` removed document, identifier and annotation in one call, leaving the other document and the default graph untouched;
- `--persist-updates` keeps updates across a restart, in `<index>.update-triples`. Without it they are in memory only and a restart loses everything harvested since the last index build.
- Operational notes: updates need `?access-token=`; the Docker image needs `-u $(id -u):$(id -g)` or the index builder cannot write.

**Turtle is enough — no quad format needed.** QLever's index builder accepts `ttl`, `nt` and `nq` only, so TriG is not an option, but `-g / --default-graph` assigns a graph per input file: a plain Turtle file loaded with `-g https://w3id.org/gto/document/x54g7` lands in that named graph, verified. The repository stays entirely in Turtle; partitioning is a loading parameter, not a serialization change.

**Still open**: whether the 74 exemplar resources in the ABOXes are migrated to this form. They would show the real shape instead of a parody of it — the argument that moved the thesaurus concepts to their `semantics.gr` IRIs — but it touches 19 iterations and every expected result naming `triple:document_1`.

**Backlog**: registering `gto` on w3id (start early), a real NAAN in place of the `12345` placeholder, resolvable links from `triple:resolverTemplate`, and iteration 20 for record-level metadata. That last one is where the accepted ambiguity resurfaces: saying when a document was harvested is, written naively, indistinguishable from saying when the document changed. It will force the choice between a distinct IRI for the graph and a separate metadata graph — not before.

**Author**: Alessandro Bertozzi

### 2026-08-10 - Fix: stop narrowing other people's properties

**Type**: Refactoring

**Iteration**: 01, 03, 04, 06, 07, 10, 11, 12, 14; all entity modules

**Description**:
`scripts/check_model.py` was introduced with 39 pre-existing violations of its own third rule — never assert `rdfs:domain`, `rdfs:range` or `rdfs:subPropertyOf` on a term outside the `triple:` namespace — parked in a baseline file, because telling a harmless restatement of the source vocabulary from a real narrowing needs the source vocabularies. So they were fetched: schema.org, DCMI Terms, DCAT, ADMS, SIOC, OA, DataCite, the literal reification ontology and FRAPO, and every one of the 39 was compared against what its own vocabulary declares.

**Twenty-eight were narrowings and are gone.** Schema.org states its ranges as a *disjunction* — `rangeIncludes` — so pinning one value excludes the others: `schema:datePublished rdfs:range xsd:date` cut out DateTime, `schema:temporalCoverage rdfs:range xsd:string` cut out DateTime and URL, `schema:inLanguage rdfs:range schema:Language` cut out Text, `schema:organizer rdfs:range schema:Organization` cut out Person. `litre:hasLiteralValue` was pinned to `xsd:string` where the SPAR ontology says `rdfs:Literal`; `schema:mentions` was given `owl:Thing` where Schema.org says `schema:Thing` — a different IRI; and two axioms were pure invention, `frapo:isOutputOf rdfs:range triple:Project` and `schema:author rdfs:subPropertyOf schema:creator`, neither of which appears in FRAPO or Schema.org. Every one of these properties already carries an `owl:allValuesFrom` restriction on the classes that use it, which is where a value constraint belongs; the only exception was `schema:email`, which now has one on `schema:ContactPoint`.

**Eleven were restatements and stay**, each verified against its source: the three DataCite axioms on `hasIdentifier` and `usesIdentifierScheme`, `oa:motivatedBy`, `adms:representationTechnique`, `dcat:bbox`, `dcat:theme` and `sioc:topic` under `dcterms:subject`, `dcterms:provenance`, and the two Schema.org properties whose `rangeIncludes` holds a single value, `contactPoint` and `spatialCoverage`. Repeating what the source says adds nothing to the world and keeps each iteration readable on its own. The baseline file is now that verified list, not a list of debt.

Consolidated model down from 1698 to 1596 triples. 155 competency questions run with 0 errors; the ten in-scope ABOXes conform to the shapes; the model satisfies its four invariants; modules and documentation regenerated with no broken anchor.

**Author**: Alessandro Bertozzi


### 2026-08-10 - Toolchain: the modules become generated, and the model gets its invariants

**Type**: Refactoring / Documentation

**Iteration**: 02, 03, 10, 12; all entity modules; new `scripts/check_model.py` and `scripts/build_modules.py`

**Description**:
Of the artefacts in the chain, `ontology/modules/serializations/*.ttl` was the only one that was both a copy and a source: the consolidated model is produced by `merge_iterations.py`, the HTML pages by pyLODE, the compiled vocabularies by `build.py` — the six modules were typed twice, by hand. Measured against the model they had drifted by some 300 assertions, mostly comments and labels the model had and the modules did not, and since pyLODE reads the *module*, those were the comments the published documentation was missing. Two rounds of hand-repair in a single day made the point.

**The rule first.** The samod skill gains a "One home per term" section. The duplication *between iterations* stays — `triple:Document` is declared in fifteen of them because each must run its three tests on `TBOX + ABOX` alone, with no imports — but the annotation of a term is written in exactly one iteration, the one that introduces it; every other iteration declares only what its own tests need; no `rdfs:domain`, `rdfs:range` or `rdfs:subPropertyOf` is ever asserted on a term outside the `triple:` namespace; and the vocabulary individuals an ABox uses are declared locally, or the iteration's queries return nothing.

**`scripts/check_model.py`** enforces four invariants on the consolidated model, each of which had been broken at least once before it was written: one comment per term and language; every `triple:` term labelled and commented; no new global axiom on a foreign term (the 39 that predate the rule are recorded in `check_model_baseline.txt`, annotated as restatements of the source ontology or as narrowings to be moved into a restriction — shrink that file, do not grow it); every term referenced as a superclass, a range or inside a restriction is itself declared.

That fourth rule found twelve terms that the model used but never declared — `dcat:Dataset` as the superclass of `triple:Dataset`, `dcterms:subject` above `sioc:topic`, `mod:SemanticArtefact`, `schema:creator` — which is why the modules had to declare them by hand. They are now declared, with a label and the source definition, in the iteration that uses them (02, 03, 10, 12).

**`scripts/build_modules.py`** turns the modules into output. A module is the class, its direct neighbours in the model — one hop: two pull in the neighbours' neighbours and the module grows from seventy terms to a hundred and ten — the terms the SHACL shapes targeting that class mention, and the handful listed in the new sidecar `<M>.metadata.ttl`, which also holds the module's own title, description and abstract. Every member is written with the description the model gives it; only the module's own class keeps its restrictions, because carrying another class's axioms would link to sections the page does not have. `--check` reports any module that differs from its projection.

The regenerated modules keep every term but `owl:Thing` and gain the annotations they were missing: Document 470 → 611 triples, Dataset 474 → 617, MediaObject 431 → 551, SemanticArtefact 424 → 564, Project 192 → 242, Profile 242 → 260. Two duplicate restrictions on `triple:MediaObject`, an artefact of hand-copying, disappear.

155 competency questions run with 0 errors; the ten in-scope ABOXes conform to the shapes; the model satisfies its four invariants; the eleven documentation pages have no broken internal anchor.

**Author**: Alessandro Bertozzi


### 2026-08-10 - Breaking: the TRIPLE thesaurus is cited, not copied — knowsAbout retired in favour of schema:about

**Type**: Refactoring (breaking)

**Iteration**: 07, 10, 11, 12, 18, 19 for the thesaurus model; 01, 02, 03, 04, 06, 14, 17 for the comment canonicalisation; all entity modules

**Description**:
The `knows_about` field of the data model revision was mapped onto a TRIPLE property, `triple:knowsAbout`, whose values were locally minted `schema:DefinedTerm` individuals with hand-copied labels. A query against the live API settled both halves of that as wrong.

**What the field actually contains.** `https://api.gotriple.eu/api/documents` returns, for every entry of `knows_about`, exactly two keys: `uri` and `labels`. Over a 200-document sample, 566 entries, 231 distinct concepts, **100% carrying a URI, 100% of them under `http://semantics.gr/authorities/SSH-LCSH/`**. That is the **TRIPLE Vocabulary**, an SSH multilingual subset of LCSH of about 3,375 `skos:Concept`, maintained by the TRIPLE consortium and published on semantics.gr by the National Documentation Centre (EKT), whose stated purpose is the automatic annotation of GoTriple publications. Its concepts dereference to real RDF: `skos:prefLabel` in up to twelve languages, `skos:broader`/`narrower`, and a `skos:exactMatch` to the Library of Congress heading they derive from. The labels travel with the URI in the index because Elasticsearch needs them denormalised for the UI, not because they are GoTriple's data. The exemplar ABOXes now cite the concept — fourteen real ones, each verified by dereferencing it — instead of minting a local twin of it. The repository already referenced this vocabulary: `Discipline.ttl` aligns disciplines to it with `skos:closeMatch`.

**Which property carries it.** `schema:knowsAbout` is an epistemic relation between an *agent* and a topic — Schema.org declares it for Person and Organization and defines it as "suggesting possible expertise". A document does not know about something; it is about it. Iteration 18 had seen half of this and minted `triple:knowsAbout` as a sub-property of `schema:about`, but kept the misleading name, so the ontology ended up with `schema:knowsAbout` and `triple:knowsAbout` side by side meaning things of different genus. The sub-property also backfired in practice: the competency questions and the GoTriple store run without a reasoner, so data asserted on `triple:knowsAbout` was invisible to anyone querying `schema:about`. **`triple:knowsAbout` is retired**; the thesaurus concepts are asserted directly on `schema:about`, with `rdfs:range skos:Concept`. `schema:keywords` keeps the producer's keywords, which the API confirms are free text with no URI, and `sioc:topic` keeps the disciplines. Three fields of the data model, three standard predicates, no TRIPLE property. `schema:knowsAbout` survives on `triple:Profile` alone, where it is in domain because a profile is a person or an organization; the data model revision leaves that cell unmapped, so the choice is the ontology's own and is now recorded as such.

**Fixed at the same time**:
- `triple:SemanticArtefact` had no `knows_about` at all, though Table 6 of the revision prescribes it: added.
- `schema:knowsAbout` carried `rdfs:range skos:Concept`, a global assertion on a property we do not own whose real range is Text/Thing/URL, and which typed every profile keyword as a SKOS concept for free. Removed.
- `triple:Project` classified its disciplines with `schema:about` while Table 4 prescribes `sioc:topic`; moved, and `schema:about` on a project now means what it means everywhere else. `CQ_7.12` asked what a project "knows about" and now asks which thesaurus concepts were detected in it, with their LCSH heading.
- Iteration 18's exemplar recorded a `triple:confidence` on the keyword-tagging annotation; the API exposes a trust score for discipline classification only, never for `knows_about`. The property stays, the unfounded value goes.
- The reuse decision on external links is restated: a thesaurus concept carries `skos:exactMatch` to LCSH, asserted by the authority itself and correct because both sides are `skos:Concept`; `schema:sameAs` remains for a producer keyword pointing at a reference page such as Wikidata, which is not a SKOS concept.

**Disciplines too.** Iteration 07 classified its projects with eight locally minted `triple:topic_N` concepts labelled "Digital Humanities", "Migration Studies", "Ancient History" — the same vice the keywords had, applied to the taxonomy. They now point at the `Discipline` controlled vocabulary (`disc:methods_and_statistics`, `disc:sociology`, `disc:demography`, `disc:cultural_heritage_and_museology`, `disc:history`, `disc:philosophy`, `disc:classical_studies`), and the restriction on `triple:Project` ranges over `triple:Discipline` like every other content class. "Digital Humanities" and "Migration Studies" are not concepts of the 27-discipline taxonomy at all; the closest ones that are, are used instead. `CQ_7.1` and `CQ_7.4` now pick a language for the label, since the vocabulary is multilingual.

**The range on `schema:about` was an overreach and is gone.** Asserting `rdfs:range skos:Concept` on a Schema.org property says that *every* value of `schema:about`, everywhere, is a SKOS concept — on a property we do not own, and against Schema.org's own `rangeIncludes Thing`. It is the same mistake as the `rdfs:range` on `schema:knowsAbout` removed in this release. What stays on the classes is the `owl:allValuesFrom` restriction, which is how every other property is documented in this model — but it is documentation, not a check: under OWL it would *type* a stray Wikidata entity as a SKOS concept rather than report it. The check now lives where checks live: `tsh:ThesaurusConceptShape` requires the value of `schema:about` to be an IRI-identified `skos:Concept` (Violation) and reports at `sh:Info` any concept outside the SSH-LCSH namespace; `tsh:DisciplineShape` asks for a `triple:Discipline` on `sioc:topic` (Warning).

**One comment per term, and no more range assertions on properties we do not own.** Twenty terms carried two to four different `rdfs:comment` values in the consolidated model, because different iterations had annotated the same term independently and the merge unions them — `schema:author` had four, `schema:dateModified` four, `schema:contributor` four — and the documentation generator renders every one of them. Each now has a single text: the most informative variant, with the GoTriple-specific sentence merged in where one of the variants carried it. `dcterms:source` was the last term in the model with neither a label nor a comment; it has both. `schema:keywords` also asserted `rdfs:range schema:DefinedTerm`, narrowing a Schema.org property whose declared range includes Text and URL: removed, like the one on `schema:about` and the one on `schema:knowsAbout`. The `owl:allValuesFrom` restrictions stay on the classes as documentation of the expected value, and the check stays in SHACL — verified empirically with an OWL RL reasoner: on a graph where a document points at a Wikidata entity, the restriction silently **types** that entity as `skos:Concept` and reports nothing, because the model declares no disjointness axiom at all (`owl:disjointWith`, `owl:AllDisjointClasses`, `owl:complementOf`, `owl:disjointUnionOf`: zero occurrences). None of the 147 `allValuesFrom` restrictions in this model can fail; they can only add types.

Also fixed here: `development/04/ABOX.ttl` declared and used `<https://schema.org/definedTerm>` — lower-case `d`, an IRI that does not exist in Schema.org. Three keywords and a restriction on `foaf:Document` were typed on that phantom class; corrected to `schema:DefinedTerm`.

155 competency questions run with 0 errors; the ten in-scope ABOXes conform to the shapes; consolidated model at 1662 triples, modules and HTML documentation regenerated.

**Author**: Alessandro Bertozzi


### 2026-08-10 - Documentation: scenarios, glossaries and expected results realigned with the identifier model

**Type**: Documentation

**Iteration**: 01, 02, 05, 06, 07, 08, 10, 11, 12, 19; all module serializations and HTML pages

**Description**:
A review pass over everything the refactor left behind in prose. The motivating scenarios of iterations 01, 08 and 19 still described a "class-based approach" with "automatic schema inference through OWL restrictions" — none of which exists any more; they now state the single rule (every identifier is a `datacite:Identifier`, the scheme is the kind) and say where mandatoriness lives. Five glossaries listed retired classes instead of schemes. Iteration 05's glossary defined `Keywords` as "a place connected with the spatial topic" and has been rewritten in full, in the `prefix:LocalName` form the other iterations use.

**Scheme individuals that were used but never declared**: iterations 01, 05, 06, 07, 08 and 19 asserted schemes (`datacite:ark`, `datacite:doi`, `datacite:handle`, `datacite:issn`, `triple:internal_id_schema`, `triple:original_id_schema`) that their own TBOX did not declare, so the identifiers were dangling within the iteration and any query joining on a scheme label silently dropped rows. All are now declared with label and comment, and appear in the corresponding glossaries.

**Expected results were stale**, in some cases from long before this release: the query test is only worth running if its oracle is right. Every entity now carries three mandatory identifiers, which multiplies the rows of any query that joins on `datacite:hasIdentifier` — recomputed for iterations 07, 08, 10, 11 and 12. Iteration 10 also referenced individuals under the wrong name throughout (`dataset_001` for `dataset-001`).

**Defects found while checking, and fixed**:
- Eight competency questions (CQ_12.3–CQ_12.10) had been truncated out of iteration 12's file during the refactor; restored. CQ_12.8 still resolved the scheme through the retired class-pinning pattern (`owl:hasValue` on the identifier class) and is now a plain scheme join.
- Iteration 05's exemplar data never linked `document_56` to its authors nor `document_67` to its keywords, so CQ_5.2 and CQ_5.3 returned nothing; the informal questions expected individuals (`author_5`, `author_567`) that do not exist. Links added, names aligned.
- Iteration 07 used `prtype:network` and `prtype:research`, neither of which is a concept of the Project Type vocabulary; all four projects are grant-funded and now carry `prtype:funded`, declared locally as the other iterations declare the vocabulary concepts they use.
- Iteration 06's formal questions numbered two different queries `CQ_6.4`; the second is now `CQ_6.6` and has its informal counterpart.
- Iteration 02's CQ_2.10 asked for `owl:imports` that the model has never declared — the vocabularies are separate modules compiled by `scripts/build.py`. It now asks which vocabulary classes the metadata draws its values from.
- Iteration 11 carried two "original" identifiers per media object, one from the pre-refactor `datacite:local-resource-identifier-scheme` and one added during the conversion, both naming the same source; the redundant three are removed.
- Headers naming the wrong iteration (05 informal questions, 11 glossary).
- `scripts/merge_iterations.py` still bound `litre:` to `http://purl.org/spar/literal/` — the one place #47 had missed — so the consolidated model wrote `hasLiteralValue` as a full IRI with no prefix; it also bound `schema:` to the `http` form. Both corrected and the model re-merged.
- `datacite:local-resource-identifier-scheme` was still declared in five module serializations without a single use, with a comment claiming it carried the profile's internal id; removed.
- The `samod` skill still taught the retired model in its reference files: the ABOX template minted `a triple:ID`, and the identifier section of `gaps.md` described the three subclasses as current. Both rewritten around schemes and shapes.

**A second review pass, driven by two verification agents, turned up more prose that had never matched the model** — most of it older than this release:
- Iteration 03's glossary described a reified role/time pattern (`Role`, `Role in time`, `has role in documents`, `is held by`, `Agent`, `Producer`, `Primary Producer`, `Funder`) that has never existed: the model uses direct properties (`schema:author`, `schema:contributor`, `schema:publisher`, `schema:provider`, `triple:aggregator`, `schema:contactPoint`). Glossary rewritten, technical specification rewritten to say what is modelled and to record *why* there is no temporal collocation and no producer/funder role, example aligned to the ABOX, and the informal questions — three of which shared the identifier `CQ_3.1` and named agents that do not exist — rewritten against the real results. `CQ_3.7` became `CQ_3.6` (there was no `CQ_3.6`) and stopped selecting an unbound variable.
- Iteration 01's technical specification still promised "class-based identifiers", "`owl:someValuesFrom`" cardinality and "automatic schema inference", fifteen lines below the corrected explanation in the same file — and no such OWL restriction exists in the TBOX.
- Iteration 02's scenario described four hash-namespace vocabulary modules pulled in with `owl:imports`, a mechanism the model has never used.
- Iteration 04's example named a `temporal_topic_3` that does not exist (temporal coverage is a literal) and the informal questions answered `place_45` for `place_67`.
- Iteration 05's scenario named the authors of `document_56` `author_5` and `author_567`; the individuals are `person_456` and `person_78`.
- Iteration 06's glossary had the subsumption backwards, calling `triple:Profile` the superclass of `foaf:Person` and `foaf:Organization` when the axiom says the opposite.
- Iteration 09's glossary listed `Citation`, `Reference` and `Mention network`, none of which is a term of the model; iterations 12 and 14 were missing rows for terms that are.
- Iteration 12's glossary defined `schema:encodingFormat` as the representation technique, which is what `adms:representationTechnique` is for.
- Iteration 15's scenario called the new entity "John Smith" while the data said "New Author Name"; the data now says John Smith.
- Iteration 18 claimed the off-label `schema:knowsAbout` usage had been migrated everywhere; it had not on `triple:Project` in iteration 07, and the reason it stays is now written down.
- Informal competency questions systematically answered "all identifiers" with the DOI or the ISSN alone, dropping the mandatory triad the ABOXes now carry: regenerated from the actual query results in iterations 01, 03, 04, 06, 07, 08, 10, 11 and 12. Iteration 10 also referenced every dataset by the wrong IRI (`dataset_001` for `dataset-001`) and was missing the informal counterpart of `CQ_10.14`.
- Iteration 16's alignment table linked to hash-separated IRIs, the pre-2.1.0 form.

**Comments harmonised**: the same term annotated differently by different iterations produced two to four `rdfs:comment` values in the consolidated model, all of which the documentation generator renders. All identifier-related terms (`triple:Document`, `triple:internal_id_schema`, `triple:original_id_schema`, `datacite:ark`, `doi`, `handle`, `issn`, `hasIdentifier`, `usesIdentifierScheme`) now carry one canonical text across every iteration, and seven duplicates that differed only by a trailing full stop were normalised. The module serializations had drifted from the model on 38 comments — the six `original*` properties in every module that references them, `triple:knowsAbout`, the enrichment properties of `Document.ttl`, `dcat:theme`, `schema:MediaObject`, `schema:DefinedTerm`, `schema:funder` and the two `oa:` motivations — all realigned; `triple:aggregator` and `triple:inCluster` had no comment at all in `Document.ttl`, the module that is meant to document them. Twenty terms of external vocabularies still carry divergent wording between iterations (`schema:author`, `schema:datePublished`, `schema:contributor`, …); that is pre-existing drift and deserves its own pass.

The nine bridge terms documented in the previous entry (`triple:AccessCondition`, `triple:ContentType`, `triple:Discipline`, `triple:License`, `triple:ProjectType` and their four properties) had their comments only in the iteration TBOXes: propagated to all six module serializations and regenerated the eleven HTML pages with the patched pyLODE, plus the `ontology.ttl`/`.rdf`/`.jsonld` data files, which still carried version 2.2.0. Consolidated model re-merged (1695 triples, down from 1716 as the duplicate comment literals collapsed); `sparql/` mirror resynced. 155 competency questions run with 0 errors — 2 return the empty set by design — and the ten in-scope ABOXes still conform to the shapes.

**Author**: Alessandro Bertozzi


### 2026-08-10 - Breaking: identifiers move to pure DataCite, mandatoriness moves to SHACL

**Type**: Refactoring (breaking — release as 3.0.0)

**Iteration**: 01, 04, 05, 06, 07, 08, 10, 11, 12, 19; all entity modules; new `shapes/`

**Description**:
Three changes that belong together, because each one only makes sense once the others are done.

**The value carrier was pointing at nothing.** Every TTL declared `@prefix litre: <http://purl.org/spar/literal/>`, but `hasLiteralValue` is defined in `http://www.essepuntato.it/2010/06/literalreification/`. `http://purl.org/spar/literal` is only the *ontology IRI* — the target of `owl:imports` in the DataCite ontology — and we had turned it into a term namespace by appending a slash. Four independent sources agree on the correct one: the Literal Reification ontology itself, the DataCite ontology's own examples (84 uses), the SKG-IF SHACL shapes and JSON-LD context, and the OpenCitations core diagram, whose prefix legend spells it out. Nothing had caught it because a wrong prefix binding is not a syntax error: every file parsed and every competency question passed, since they all made the same mistake consistently. The breakage was only visible from outside — which is exactly where interoperability lives. Fixed in 56 files, 103 occurrences. Closes #47.

**All identifier subclasses are retired.** `triple:ID`, `triple:PID`, `triple:OriginalIdentifier`, `triple:DOI`, `triple:Handle`, `triple:ISBN`, `triple:ISSN` and `triple:URI` no longer exist. `datacite:Identifier` already requires exactly one `datacite:usesIdentifierScheme`, so the scheme is always present and always sufficient to say what kind of identifier something is; a class pinned to a single scheme with `owl:hasValue` only duplicates it. This is the same choice OpenCitations makes with this pattern — verified against its ontology, which declares no subclass of `datacite:Identifier` and eight scheme individuals. Adding a new kind of identifier now costs one individual, not a scheme plus a class. 79 exemplar instances were converted to assert their scheme explicitly, since it is no longer entailed by a class.

**Mandatoriness moves out of OWL and into SHACL.** The presence axioms went with the classes, and are replaced by a shapes graph in `shapes/`. The reason is not tidiness: OWL restrictions describe inferences, not constraints. Under open-world semantics a missing identifier is inferred to exist rather than reported, and `owl:qualifiedCardinality 1` over two distinct nodes concludes they are the same node instead of flagging an error — with no `owl:AllDifferent` on the scheme individuals, that could have collapsed `datacite:doi` and `datacite:handle`. The shapes state the same requirements in a form that is actually checked, with graded severity (`sh:Violation` mandatory, `sh:Warning` recommended, `sh:Info` expected), natural-language messages, and value patterns for ARK and DOI that OWL cannot express at all. `scripts/validate.py` runs them with `pyshacl`.

**Scope of the exemplar data**: the validator targets the iterations whose motivating scenario is about identifiers (01, 04, 05, 06, 07, 08, 10, 11, 12, 19), all of which now pass. The other iterations use documents as vehicles for teaching something else and carry deliberately partial instances; validating them against a publication profile would be a category error.

Also in this release: five identifier schemes that existed only in exemplar data (`h2020`, `erc`, `prin`, `fwf`, `getty`) were removed — the ADR mentions H2020 once, as an example of `funding_type` mapped to `schema:fundingScheme`, not as an identifier scheme; twelve `OriginalIdentifier` instances carried no scheme at all, violating an axiom of the SPAR ontology itself; and two identifiers in iteration 12 were declared twice with different values, violating the single-value axiom inherited from `litre:Literal`.

Consolidated ontology down from 1902 to 1704 triples. 155 competency questions run with 0 errors; all ten in-scope ABOXes conform to the shapes.

**Author**: Alessandro Bertozzi


### 2026-07-28 - Documentation: module pages now show what the identifier requirements are about

**Type**: Documentation

**Iteration**: all module HTML pages

**Description**:
The generated documentation was not communicating the identifier model at all. The customized pyLODE that produces `ontology/modules/html/<M>/index.html` never read `owl:onClass`, so the four qualified cardinality restrictions on `triple:Document` all rendered as a bare `datacite:hasIdentifier op exactly 1` — four identical lines, with `triple:ID`, `triple:PID` and `triple:OriginalIdentifier` dropped. Patched the generator (see `PATCHES.md` in the pyLODE fork, which is not under version control): qualified restrictions now carry the class they are qualified on, `owl:hasValue` IRI targets are rendered as links instead of quoted strings, and `skos:example` and `skos:scopeNote`/`skos:note` get their own "Example" and "Usage" sections on classes, properties and named individuals — previously no SKOS annotation on a property or an individual was collected at all, and those on classes ended up under the "External Alignment" heading. All 11 module pages regenerated: the 6 entity modules now show requirements such as `hasIdentifier exactly 1 Internal ID`, while the 5 vocabulary modules show no non-whitespace difference, confirming no regression. Dangling-anchor count unchanged.

This unblocks the term-level documentation of the identifier pattern: `rdfs:comment` for the definition, `skos:scopeNote` for the usage rule, `skos:example` for the Turtle snippet.

**Author**: Alessandro Bertozzi

### 2026-07-27 - Refactoring: one rule for identifiers — the scheme is the kind, the classes are the mandatory kinds

**Type**: Refactoring

**Iteration**: 01, 05, 06, 07, 08, 10, 11, 12, 19; all entity modules

**Description**:
The identifier pattern carried two overlapping typing layers grown at different times. `datacite:Identifier` already requires exactly one `datacite:usesIdentifierScheme`, so the scheme is always present and always sufficient to say what kind of identifier something is; a `triple:*` identifier class is therefore justified only where the model needs to name that kind inside a class-level axiom. That rule is now stated in `patterns/identifier-pattern.ttl` and applied throughout.

**Schemes**: `triple:ID` and `triple:OriginalIdentifier` both pinned `datacite:local-resource-identifier-scheme`, which cannot tell an identifier local to GoTriple from one local to the source system — the collision was the only reason those classes were load-bearing. `triple:ID` now pins the new `triple:internal_id_schema` and `datacite:local-resource-identifier-scheme` is dropped. `triple:OriginalIdentifier` deliberately pins **no** scheme: an original identifier can come from any source system and its scheme names that system (`triple:h2020_scheme`, `triple:prin_scheme`, `triple:fwf_scheme`, with the new `triple:original_id_schema` as generic fallback) — the previous pin conflicted with the source-specific schemes already used in iteration 07. This makes real the schemes the documentation had claimed since iteration 01; only `triple:pid_schema` remains retired, superseded by `datacite:ark`.

**Restrictions on entities**: the five `owl:allValuesFrom` unions on `datacite:hasIdentifier` (Document, Dataset, MediaObject, SemanticArtefact, Project) were logically vacuous — each listed `datacite:Identifier` alongside its own subclasses, so it constrained nothing beyond the property's `rdfs:range`, while reading like a closed list of admitted types. Worse, closing them naively would have made `triple:Document` unsatisfiable, since it separately required an ID, a PID and an OriginalIdentifier that the union did not list. All five are removed and replaced by presence axioms only: exactly one `triple:ID`, exactly one `triple:PID` and at least one `triple:OriginalIdentifier` (original identifiers are a list) on the four content classes and Project; `triple:ID` and `triple:PID` only on `triple:Profile`, which has no source system because registered users are created inside GoTriple; `triple:ID` alone on `triple:Cluster` and `foaf:OnlineAccount`, both platform-created. The optional identifier kinds an entity typically carries are documented in its `rdfs:comment` rather than constrained. `rdfs:range datacite:Identifier` is now declared in iteration 01 as the single global statement that every identifier goes through the DataCite relation and classes.

**Exemplar data**: the ABOXes of the iterations that model identifiers were brought into conformance (01, 05, 06, 07, 08, 10, 11, 12, 19); iterations that merely use documents as vehicles for another concern keep minimal instances, as SAMOD's data test is about the iteration's own modelet. This also fixed pre-existing defects: identifiers with no `litre:hasLiteralValue` at all (violating the `datacite:Identifier` axiom) in iterations 01, 05 and 06, two anonymous schemes `triple:identifier_schema_1`/`_2` and two bespoke `triple:agent_identifier_scheme`/`triple:account_identifier_scheme` now replaced by `triple:internal_id_schema`, and identifiers whose intended meaning was described in the motivating scenario but never modelled. Consolidated ontology re-merged, all six entity module serializations and HTML pages regenerated, `sparql/` mirror resynced; 138 competency questions run with 0 errors.

**Author**: Alessandro Bertozzi

### 2026-07-27 - Modification: triple:PID is an ARK, not a local resource identifier

**Type**: Modification

**Iteration**: 01, 07, 10, 11, 12

**Description**:
`triple:PID` — the persistent identifier minted and exposed by GoTriple — pinned its scheme to `datacite:local-resource-identifier-scheme` via `owl:hasValue`, the same scheme as `triple:ID` and `triple:OriginalIdentifier`. The identifier GoTriple mints is technically an ARK, so the restriction now pins `datacite:ark`, which also gives a purpose to the scheme individual added by #40 (until now it was declared but never wired to anything). `datacite:ark` is declared in iterations 01, 10, 11 and 12 alongside the PID class, and the ABOX exemplar values move from the `gotriple:<type>:<slug>` form to ARK form (`ark:/12345/...`, with a placeholder NAAN to be replaced by the real GoTriple one). Fixed at the same time two identifiers in iteration 07 that were typed `triple:PID` while carrying grant-programme schemes (`triple:h2020_scheme`, `triple:erc_scheme`) with values `H2020-863420` and `ERC-ADG-101052789`: those are funding-programme identifiers, not GoTriple-minted PIDs, and under the `hasValue` restriction they would have been entailed to use the wrong scheme; they are now plain `datacite:Identifier` instances distinguished by their own scheme.

**Author**: Alessandro Bertozzi

### 2026-07-27 - Addition: iteration 19 — Profile enrichment (issues #44, #46)

**Type**: Addition

**Iteration**: 19 (new); 06 (identifier cardinality relaxed)

**Description**:
New SAMOD iteration 19 implementing the Profile data model of the updated ADR 005 "GoTriple Data Model revision" (LUMEN WP4/T4.2, Table 3), tracked by issue #44. `triple:Profile` now carries: `foaf:givenName`/`foaf:familyName` (0..1 each), `schema:description` (union `rdf:langString`/`xsd:string`, cf. #43), the new `triple:pronouns` (`xsd:string`, 0..1), `schema:image` (profile photo URL, 0..1), `schema:url` (personal web pages), `foaf:topic_interest` with `triple:Discipline` values (chosen or auto-detected disciplines), `schema:knowsAbout` with `schema:DefinedTerm` values (thesaurus keywords — the Schema.org property is natively in-domain for Person/Organization, so no TRIPLE sub-property is needed here, unlike the creative-work case of iteration 18), `schema:knowsLanguage` with `schema:Language` values, `schema:affiliation` with `foaf:Organization` values, the new flags `triple:registeredUser` and `triple:openToCollaboration` (`xsd:boolean`, 0..1 each), and `schema:dateModified` for the last GoTriple update (date pattern). Identifiers (issue #46) reuse the existing DataCite pattern, keeping the four identifier fields of Table 3 apart by scheme: the internal Elasticsearch `id` as `triple:ID`, the GoTriple-minted `pid` as `triple:PID`, the `goTripleId` with the new `triple:gotriple_id_schema`, and the external person PIDs of `user_identifier` (ORCID, IdRef, ISNI) as plain `datacite:Identifier` instances, with the schemes `datacite:orcid`, `datacite:isni`, `datacite:researcherid` reused from the DataCite ontology plus the new `triple:idref_schema`. No dedicated identifier subclass is minted for person PIDs: in this model a subclass earns its place only when several kinds of identifier collide on one scheme (as `triple:ID` and `triple:OriginalIdentifier` do), whereas each of these schemes already identifies its kind one-to-one; the ADR's `PID_Type` is therefore satisfied by the scheme individuals rather than by a separate SKOS vocabulary. The identifier restriction on `triple:Profile` (iteration 06) is relaxed from exactly one to **at least one** identifier. `author_of` is intentionally not materialized (inverse of `schema:author`); `hasOccupation` is deferred until its controlled vocabulary is defined; `numberOfDocuments` and cluster counters stay out of scope (platform-computed). Consolidated `ontology/triple.ttl` re-merged (1914 triples), Profile module serializations and HTML documentation regenerated, `sparql/19.md` added (138 queries total, all executable).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Refactoring: patterns/ and examples/ aligned with the current model

**Type**: Refactoring

**Iteration**: patterns/ and examples/ folders

**Description**:
Brought the design-pattern catalog and the JSON-LD examples up to date with the 2.2.0 model. **Patterns**: fixed the legacy `triple#` namespace and undeclared prefixes (several files did not parse); usage examples now target the platform classes (`triple:Dataset` instead of `schema:Dataset`); the identifier pattern now shows the typed identifier subclasses (`triple:ID`/`PID`/`DOI`/...), the current scheme individuals and the URL-based schemes; the controlled-vocabularies pattern uses the per-vocabulary concept namespaces (`ct:article`, `acc:open_access`); the person-organization pattern documents the #42 decision (funder/sponsor on `schema:Grant`, never on documents); the date pattern notes the Document date properties from #39. Added two new patterns: `original-values-pattern.ttl` (iteration 17 hybrid dc: sub-property pattern) and `enrichment-annotation-pattern.ttl` (iteration 18 Web Annotation provenance with confidence). All 10 pattern files parse with rdflib. **Examples**: rewrote `examples/jsonld/document-complete-example.jsonld` on the current model (it still used the hash namespace, http schema.org, the dropped SPAR PRO role pattern, dcterms:title instead of schema:headline and pre-2.1.0 vocabulary URIs), now showcasing bridge-class vocabulary links, typed identifiers, original provider values, dates, structured keywords, topic/keyword annotations with confidence, cluster and project links; the JSON-LD parses to 128 triples. jsonld README snippets updated accordingly.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Refactoring: sparql/ folder rebuilt as a mirror of the iteration competency questions

**Type**: Refactoring

**Iteration**: 16 (CQ fix); sparql/ folder

**Description**:
The `sparql/` folder (7 files covering iterations 01-07) had drifted from the model: legacy `triple#` namespace, queries using the dropped SPAR PRO role pattern (`pro:isDocumentContextFor`) and the removed `triple:alsoKnownAs` property, wrong iteration headers. Rebuilt it as a complete mirror of the current `development/NN/formal-competency-questions.md` for all 18 iterations, with a README stating the sync rule (edit the iteration file, then re-copy). Also fixed the malformed CQ_16.5 in iteration 16 (`?tripleClass (?p) fabio:Work` is invalid SPARQL — a variable cannot appear in a property path). All 153 queries verified executable with rdflib against their iteration's TBox+ABox (153/153 pass).

**Author**: Alessandro Bertozzi

## [2.2.0] - 2026-07-10

### 2026-07-10 - Release 2.2.0

**Type**: Refactoring / Documentation

**Description**:
Minor release collecting the issue-closure work of 2026-07-10 (issues #31, #32, #35, #36, #38, #39, #40, #41, #42, #43 — see the entries below): SAMOD iterations 17 (original provider values) and 18 (enrichment metadata), the #39 gap closure against the LUMEN ADR 005, vocabulary alignments and multilingual labels, and the HTML documentation fixes. Release chores: bumped `owl:versionInfo` to 2.2.0 and `dcterms:modified` in `ontology/metadata.ttl` (adding `owl:priorVersion` 2.1.0) and in all module serializations; fixed the stale hash-based `vann:preferredNamespaceUri` in `ontology/metadata.ttl` to the canonical slash form; `scripts/merge_iterations.py` now reads the ontology metadata from `ontology/metadata.ttl` (single source of truth, shared with `build.py`) instead of a hardcoded 1.0.0 block, so `ontology/triple.ttl` carries the full, current metadata; vocabularies rebuilt and all module serializations (ttl/rdf/jsonld) and HTML documentation pages regenerated at 2.2.0.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Documentation: module HTML pages regenerated

**Type**: Documentation

**Iteration**: All modules

**Description**:
Regenerated the `index.html` documentation pages of all 11 modules (Document, Dataset, MediaObject, SemanticArtefact, Project, Profile, ContentType, AccessCondition, License, Discipline, ProjectType) with the customized pyLODE pipeline, so they reflect the current module serializations: iterations 17-18 (original provider values, enrichment metadata), the issue #39 gap closure (dates on Document, `triple:originalSource`, `dcat:theme`, `adms:representationTechnique`, the populated ProjectType vocabulary), the `semantic_artefact` concept (#35), the COAR closeMatch additions (#31) and the multilingual labels (#41). The inner-`#` percent-encoding of anchor fragments (issue #32) was re-applied after regeneration, and all internal anchors were verified to resolve (the only unresolved targets are external datatypes such as `xsd:date`, a pre-existing generator behavior unchanged from the previous pages).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: Project Type vocabulary concepts (issue #39)

**Type**: Addition

**Iteration**: Controlled vocabularies

**Description**:
The Project Type vocabulary (`vocabularies/serializations/ttl/ProjectType.ttl`) contained only the concept scheme with no concepts, while the LUMEN ADR 005 prescribes a controlled vocabulary for the `additional_type` field of Projects. Added the seven concepts listed in the ADR: `pt:funded`, `pt:non_funded`, `pt:crowdfunded`, `pt:citizen_science`, `pt:community_based`, `pt:legacy`, `pt:institutional`, each with an English label and definition, following the existing vocabulary pattern. Compiled output regenerated with `build.py`; ProjectType module serializations (ttl/rdf/jsonld) updated. Part of the issue [#39](https://github.com/atrium-research/triple-ontology/issues/39) gap closure.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: dcat:theme on Dataset; adms:representationTechnique and schema:mentions on SemanticArtefact (issue #39)

**Type**: Addition

**Iteration**: 10, 12

**Description**:
Remaining minor gaps from the issue [#39](https://github.com/atrium-research/triple-ontology/issues/39) analysis against the LUMEN ADR 005 tables. Iteration 10: added `dcat:theme` (`rdfs:subPropertyOf dcterms:subject`, range `skos:Concept`) on `triple:Dataset` for the provider-assigned classification, distinct from `sioc:topic` which carries the automatically assigned TRIPLE disciplines. Iteration 12: added `adms:representationTechnique` (range `skos:Concept`, new `adms:` prefix, e.g. the ADMS representation-technique concept for SKOS) and the missing `schema:mentions` restriction on `triple:SemanticArtefact`, aligning it with the other content classes. ABoxes exemplify both (EU data-theme SOCI; ADMS SKOS representation technique). Merged into `ontology/triple.ttl`; Dataset and SemanticArtefact module serializations updated.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: originalSource and original_* restrictions on all content classes (issue #39)

**Type**: Addition

**Iteration**: 17

**Description**:
Extension of iteration 17 ("Original Provider Values") following the gap analysis of issue [#39](https://github.com/atrium-research/triple-ontology/issues/39) against the LUMEN ADR 005 tables. Added `triple:originalSource` (`rdfs:subPropertyOf dc:source`, `xsd:string`), preserving the source statement exactly as received from the provider (e.g. a journal issue string) before processing into the normalized `dcterms:source` or the URL-based identifiers — the same hybrid sub-property pattern of the other five original properties. The `original_*` restrictions, previously declared only on `triple:Document`, are now declared on `triple:Dataset`, `triple:MediaObject` and `triple:SemanticArtefact` as prescribed by the ADR tables (`original_source` is not defined for Dataset in the ADR, so Dataset carries only the other five). New competency question CQ_17.5 and a dataset example in the ABox. Merged into `ontology/triple.ttl`; Document, Dataset, MediaObject and SemanticArtefact module serializations updated.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: datePublished and dateModified restrictions on Document (issue #39)

**Type**: Addition

**Iteration**: 01

**Description**:
The gap analysis against the LUMEN ADR 005 "GoTriple Data Model revision" (issue [#39](https://github.com/atrium-research/triple-ontology/issues/39)) confirmed that `triple:Document` had no publication/modification date modeling: `schema:datePublished` was declared (iteration 03) but carried no restriction on Document, while Dataset, MediaObject and SemanticArtefact already follow the date pattern. Added `schema:datePublished` (`date_published` field) and `schema:dateModified` (`last_modified_timestamp` field) to iteration 01 ("TRIPLE Document - Core Metadata Model") with the standard date-pattern restrictions (`owl:allValuesFrom xsd:date` + `owl:maxCardinality 1`, both optional); dates exemplified in the ABox and covered by the new competency question CQ_1.20. Merged into `ontology/triple.ttl`; Document module serializations updated. Note: `date_created` is intentionally not added to Document — the ADR defines it only for Dataset, SemanticArtefact and MediaObject, which already have it.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: Iteration 18 — Enrichment metadata (issue #38, part 2)

**Type**: Addition

**Iteration**: 18 (new); 10, 11 (knowsAbout migration)

**Description**:
New SAMOD iteration `development/18` ("Enrichment Metadata") covering the remaining checklist items of issue #38. **Topic confidence**: discipline assignments keep the direct `sioc:topic` triple and gain an `oa:Annotation` provenance layer (`oa:hasTarget`, `oa:hasBody`, `oa:motivatedBy oa:classifying`, `dcterms:creator`) carrying the new `triple:confidence` (`xsd:decimal`, the SKG-IF `trust`); keyword annotations use `oa:motivatedBy oa:tagging` — the same Web Annotation pattern already used for NER mentions in iteration 15, with the design rationale and rejected alternatives (RDF-star, plain reification, bespoke qualified relation, PROV-O) documented in the motivating scenario. **Structured keywords**: new `triple:knowsAbout rdfs:subPropertyOf schema:about` (range `schema:DefinedTerm`, with language-tagged `schema:name` labels and optional `schema:sameAs` URI); introduced because `schema:knowsAbout` is declared only for Person/Organization — its pre-existing off-label use on `triple:Dataset` (iteration 10) and `triple:MediaObject` (iteration 11) was migrated, converting the string values in their ABoxes to `schema:DefinedTerm` individuals. **Language detection/translation**: new `triple:detectedLanguage` and `triple:machineTranslatedLanguage` (`xsd:string`) on `triple:Document`. All external usages verified against the official OA, SKOS, schema.org, SIOC vocabularies. All five formal competency questions pass; merged into `ontology/triple.ttl`; Document, Dataset and MediaObject module serializations updated. Together with iteration 17 this completes issue [#38](https://github.com/atrium-research/triple-ontology/issues/38).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: Iteration 17 — Original provider values (issue #38, part 1)

**Type**: Addition

**Iteration**: 17 (new)

**Description**:
New SAMOD iteration `development/17` ("Original Provider Values - Provenance of Harvested Metadata") covering the `original_*` checklist item of issue #38. Introduces five optional datatype properties on `triple:Document` that preserve the metadata values exactly as received from source providers, before SCRE normalization: `triple:originalType`, `triple:originalLanguage`, `triple:originalDatePublished`, `triple:originalLicense`, `triple:originalConditionsOfAccess` (all `xsd:string`). Each is declared `rdfs:subPropertyOf` the corresponding Dublin Core Elements 1.1 term (`dc:type`, `dc:language`, `dc:date`, `dc:rights`) — the hybrid reuse-by-subsumption pattern already used for `triple:hasLicense`/`triple:hasContentType` — so generic Dublin Core consumers see the raw values through standard `dc:` terms while the license/access-condition distinction is preserved internally. Normalized counterparts remain on `triple:hasContentType`, `schema:inLanguage`, `schema:datePublished`, `triple:hasLicense`, `triple:hasAccessCondition`. All four formal competency questions pass; merged into `ontology/triple.ttl` and added to the Document module serializations. The `modelet.graphml` is generated from the TBox; the PNG export will be produced with yEd in the issue #34 pass. Addresses the second and (already satisfied) fifth checklist items of [#38](https://github.com/atrium-research/triple-ontology/issues/38).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: Multilingual labels from the Hackathon spreadsheet (issue #41)

**Type**: Addition

**Iterations**: 01, 06, 07, 10, 11, 12 (class labels) + vocabularies

**Description**:
Added Portuguese, Polish and French `rdfs:label`s from the Hackathon results ("GoTriple Ontology Labels" spreadsheet):
- **Discipline**: added @pt and @pl to all 27 concepts (existing @de/@en/@fr/@it labels kept — the pre-existing French labels differ from the Hackathon ones and were preserved).
- **Content Type**: added @pt/@pl/@fr to all 20 concepts in the sheet.
- **Access Condition**: added @pt/@pl/@fr to all 8 concepts in the sheet.
- **License**: added @pt/@pl/@fr to 12 concepts; the "CAIRN" row has no corresponding concept in the vocabulary and was skipped.
- **Core classes**: added @pt/@pl/@fr labels to `triple:Document`, `triple:Project`, `triple:Dataset`, `triple:MediaObject` ("Multimedia"), `triple:SemanticArtefact` and `triple:Profile` in their owning iterations and module serializations (also fixed the missing @en tag on the Semantic Artefact label). The "Author" and "Software" rows of the classes sheet were skipped (no corresponding class: authors are `foaf:Person`/`triple:Profile`, software is the `ct:software` concept already translated).
Rebuilt vocabularies, regenerated `ontology/triple.ttl` and refreshed all module serializations (TTL, RDF/XML, JSON-LD). Closes [#41](https://github.com/atrium-research/triple-ontology/issues/41).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Fix: Leftover namespace-migration debris in ABox files of iterations 09, 10, 11

**Type**: Modification

**Description**:
Removed dangling `eu/ontology/triple/1.0.0> .` line fragments (remnants of the removed `owl:versionIRI` declarations from the 2.1.0 namespace migration) in `development/09/ABOX.ttl`, `development/10/ABOX.ttl` and `development/11/ABOX.ttl`, and added the missing `sioc:` prefix declaration in `development/10/ABOX.ttl`. These files did not parse, so the SAMOD data tests of iterations 09–11 could not run. All 32 TBox/ABox files now parse cleanly.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Documentation: Removed redundant "Vocabulary" from vocabulary titles (issue #36)

**Type**: Documentation

**Description**:
The documentation link tree listed the controlled vocabularies with a redundant "Vocabulary" suffix in their titles ("Content Type Vocabulary", "Discipline Vocabulary", "License Vocabulary", "Project Type Vocabulary" — Access Condition had already been normalized). Removed the suffix from `dcterms:title` in the vocabulary metadata sidecars, rebuilt with `build.py`, refreshed the module serializations (TTL, RDF/XML, JSON-LD) and patched `<title>`/`<h1>` in the corresponding `index.html` pages. Closes [#36](https://github.com/atrium-research/triple-ontology/issues/36).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Fix: Broken fragment anchors in the module HTML documentation (issue #32)

**Type**: Documentation

**Description**:
The generated module documentation pages used raw entity URIs as fragment anchors (`href="#<URI>"`). For external terms whose URI itself contains a `#` (e.g. `skos/core#Concept`, `oa#Annotation`, `rdf-syntax-ns#langString`), the resulting link contained a second unencoded `#`, which is invalid and breaks in-page navigation. Percent-encoded the inner `#` as `%23` in 196 anchors across the 11 module `index.html` pages (element `id`s stay raw: browsers percent-decode the fragment before ID matching). Closes [#32](https://github.com/atrium-research/triple-ontology/issues/32).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Modification: Completed COAR access_rights mapping of the Access Condition vocabulary (issue #31)

**Type**: Modification

**Description**:
Completed the alignment of `triple:conditions_of_access` with the COAR Access Rights vocabulary. All four COAR concepts were already mapped via `skos:exactMatch` (`open_access` → c_abf2, `restricted_access_or_use` → c_16ec, `embargoed_access` → c_f1cf, `metadata_only_access` → c_14cb); added `skos:closeMatch` for the remaining access-flavored local concepts: `closed_access` → c_14cb (following the OpenAIRE closedAccess ↔ COAR metadata-only convention) and `free_access` → c_abf2 (gratis vs libre distinction, hence closeMatch). `all_rights_reserved`, `public_domain`, `other` and `undefined` are rights/licensing statements with no COAR access-rights counterpart and remain unmapped. Rebuilt and refreshed the AccessCondition module serializations. Closes [#31](https://github.com/atrium-research/triple-ontology/issues/31).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: "Semantic artefact" concept in the Content Type vocabulary (issue #35)

**Type**: Addition

**Description**:
Added `ct:semantic_artefact` ("Semantic artefact") to the Content Type controlled vocabulary (`vocabularies/serializations/ttl/ContentType.ttl`) with `skos:closeMatch` to the COAR Resource Type `semantic artefact` (GSZA-Y7V7), plus its `ct:typ_semantic-artefact` identifier individual, following the existing vocabulary pattern. Rebuilt with `build.py` and refreshed the ContentType module serializations (TTL, RDF/XML, JSON-LD). The module `index.html` still lists the previous concepts and will be regenerated with issue #34. Closes [#35](https://github.com/atrium-research/triple-ontology/issues/35).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Fix: datacite:hasIdentifer/usesIdentiferScheme typos in iteration 01 test data

**Type**: Modification

**Iterations**: 01 (and 02 diagram)

**Description**:
Fixed the misspelled predicates `datacite:hasIdentifer` (in `development/01/ABOX.ttl`, `development/01/formal-competency-questions.md`, `sparql/01.md`, and the modelet diagrams of iterations 01 and 02) and `datacite:usesIdentiferScheme` (in the iteration 01 formal CQs): the ABox data did not satisfy the TBox restrictions and the queries only worked because they shared the same typo. Also repaired the scrambled `triple:document_45` block in the ABox, which used `hasIdentifer` for its `dc:type` concept and `usesIdentifierScheme` for its identifiers; it now reads `dc:type triple:type_7` and `datacite:hasIdentifier triple:identifier_67, triple:identifier_678`. PNG diagram exports still show the old label and will be regenerated with issue #34.

**Author**: Alessandro Bertozzi

### 2026-07-10 - Modification: Relaxed range of schema:headline and schema:abstract (issue #43)

**Type**: Modification

**Iterations**: 01, 10, 11, 12

**Description**:
Relaxed every `rdf:langString` constraint on `schema:headline` and `schema:abstract` to the union datatype `owl:unionOf (rdf:langString xsd:string)`, so that titles and abstracts arriving from providers without language metadata remain valid without fabricating language tags. Changed both the global `rdfs:range` axioms and the class restrictions (`owl:someValuesFrom` on `triple:Document` and `triple:SemanticArtefact`, `owl:allValuesFrom` on `triple:Dataset` and `triple:MediaObject`). The issue text mentions the Document module, but `rdfs:range` is a global axiom and the same constraint was declared in the Dataset, MediaObject and SemanticArtefact iterations/modules, so all occurrences were updated for coherence. Existing `rdf:langString` data remains valid; document-level language stays available via `schema:inLanguage`. Updated the four module serializations and regenerated `ontology/triple.ttl`. Closes [#43](https://github.com/atrium-research/triple-ontology/issues/43).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Addition: datacite:ark admitted as identifier scheme (issue #40)

**Type**: Addition

**Iteration**: 08

**Description**:
Added `datacite:ark` (Archival Resource Key, defined by the SPAR DataCite ontology) as an `owl:NamedIndividual` of `datacite:IdentifierScheme` in `development/08/TBOX.ttl`, alongside `datacite:doi`, `datacite:issn`, `datacite:isbn` and `datacite:handle`. Updated the iteration 08 glossary, the Document module serializations, and regenerated `ontology/triple.ttl`. Identifiers can now use ARK via `datacite:usesIdentifierScheme datacite:ark`. Closes [#40](https://github.com/atrium-research/triple-ontology/issues/40).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Modification: Removed schema:funder from triple:Document (issue #42)

**Type**: Modification

**Iteration**: 03

**Description**:
Removed the `schema:funder` property declaration and the corresponding restriction on `triple:Document` from `development/03/TBOX.ttl`, since project funding is now modelled via `frapo:isOutputOf` linking documents to projects (grants keep their `schema:funder` from iteration 07). Updated CQ_3.1 in `development/03/formal-competency-questions.md` and `sparql/03.md`, the Document module serializations, and regenerated `ontology/triple.ttl`. Closes [#42](https://github.com/atrium-research/triple-ontology/issues/42).

**Author**: Alessandro Bertozzi

### 2026-07-10 - Fix: Unbound default prefix broke merge of iterations 03 and 04

**Type**: Modification

**Description**:
Fixed leftover bare `:` prefix usages from the 2.1.0 namespace migration (`:aggregator` in `development/03/TBOX.ttl`, `:Document` in `development/04/TBOX.ttl`, several individuals in `development/01/ABOX.ttl`). The undeclared prefix made `rdflib` fail to parse those files, and `merge_iterations.py` silently skipped them (errors are only logged): the consolidated `ontology/triple.ttl` was missing all axioms from iterations 03 and 04 (Document actor restrictions such as `schema:author`, `schema:publisher`, `triple:aggregator`, and the keywords/spatial/temporal coverage restrictions). Replaced bare `:` with the `triple:` prefix and regenerated `ontology/triple.ttl` (1303 → 1432 triples).

**Author**: Alessandro Bertozzi

## [2.1.0] - 2025-12-24

### 2025-12-24 - Refactoring: Global Terms Namespace Standardization

**Type**: Refactoring

**Description**:
Standardized the ontology namespace URI from `https://gotriple.eu/ontology/triple#` to `https://gotriple.eu/ontology/triple/` (slash separator instead of hash) to align with best practices and resolve URI generation consistency issues.

**Details**:
- **Namespace Change**: Updated `TRIPLE` namespace URI to use a trailing slash `/` across the entire project.
- **Development Iterations**: Updated all 16 iterations in `development/` (TBox and ABox) to use `triple:` prefix and slash-based URIs. Removed redundant `@base` and `owl:Ontology` declarations from development files.
- **Source Vocabularies**: Standardized all vocabularies in `vocabularies/serializations/ttl/` to use the new namespace and removed manual ontology headers (delegated to build script).
- **Ontology Modules**: Updated all module serializations in `ontology/modules/serializations/` to consistent `triple:` prefix usage.
- **Build Script**: Updated `scripts/build.py` to generate headers with the correct slash-based namespace.
- **Merge Script**: Updated `scripts/merge_iterations.py` to use the correct `TRIPLE` namespace definition.
- **Main Ontology**: Consolidate `ontology/triple-ontology.ttl` now uses consistent `triple:` prefix for all TRIPLE-defined entities.

**Author**: Alessandro Bertozzi

### 2025-12-23 - Refactoring: Vocabulary Standardization and Modularization

**Type**: Refactoring / Enhancement

**Description**:
Standardized vocabulary file names, implemented the "Bridge Classes" pattern for better modularity, fixed prefix usage, and established strict imports in the main ontology file.

**Details**:
- **Renaming**: Renamed all vocabulary files to PascalCase to match their class definitions:
  - `disciplines.ttl` -> `Discipline.ttl`
  - `license.ttl` -> `License.ttl`
  - `conditions_of_access.ttl` -> `AccessCondition.ttl`
  - `content_types.ttl` -> `ContentType.ttl`
- **New Vocabulary**: Created `ProjectType.ttl` for project types.
- **Bridge Classes**: Defined bridge classes (e.g., `triple:Discipline`) directly within each vocabulary file to make them self-contained.
- **Prefix Fixes**: Corrected `Discipline.ttl` to use the `disc:` prefix for individuals and identifiers, replacing incorrect `owl:` usage.
- **Descriptions**: Replaced `skos:definition` with `rdfs:comment` for consistency and added descriptions to all vocabulary concepts.
- **Ontology Imports**: Updated `ontology/triple.ttl` to explicitly import all modular vocabularies and declare the `disc:` prefix.
- **Restrictions**: Fixed `sioc:topic` restrictions in `ontology/triple.ttl` to correctly reference `triple:Discipline`.

**Author**: Alessandro Bertozzi

### 2025-12-22 - Bugfix: Ontology Consistency

**Type**: Bugfix / Refactoring

**Description**:
Resolved inconsistencies in property definitions and relaxed redundant restrictions on `triple:Document`.

**Details**:
- **Bugfix**: Corrected `datacite:usesIdentifierScheme` in Iteration 10 (`development/10/TBOX.ttl`) which acted as `dcat:distribution` due to a copy-paste error.
- **Refactoring**: Removed redundant and conflicting `owl:allValuesFrom triple:Profile` restriction on `schema:author` in `triple:Document` (Iteration 06 and consolidated ontology). Now relies on the broader `foaf:Person` or `foaf:Organization` union.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Vocabularies Simplification

**Type**: Refactoring

**Description**:
Removed `skos:ConceptScheme` definitions and `skos:inScheme` assertions from all controlled vocabularies to simplify the model. Reset `project_types.ttl` to an empty state.

**Details**:
- **Refactoring**: Removed concept scheme elements from:
  - `conditions_of_access.ttl`
  - `content_types.ttl`
  - `disciplines.ttl`
  - `license.ttl`
- **Enhancement**: Added reference classes definition (`triple:AccessCondition`, `triple:ContentType`, `triple:Discipline`, `triple:License`) to all vocabulary individuals.
- **Refactoring**: Removed redundant `skos:Concept` type assertion from vocabulary individuals, as they are now typed with specific subclasses of `skos:Concept`.
- **Revert**: Cleared `project_types.ttl` content.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Addition: Project Type Controlled Vocabulary

**Type**: Addition

**Description**:
Implemented a controlled vocabulary for Project Types to classify projects (e.g., Research, Training, Network) and integrated it into Iteration 07.

**Details**:
- **Vocabulary**: Created `project_types.ttl` with SKOS concepts.
- **TBOX (Iteration 07)**:
  - Imported `project_types.ttl`.
  - Defined `triple:ProjectType` (Bridge Class) and `triple:hasProjectType` property.
  - Added restriction to `triple:Project`.
- **ABOX (Iteration 07)**: Added `triple:hasProjectType` assertions to example projects.
- **Documentation**: Updated Motivating Scenario, Glossary, and Competency Questions.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Geographic Properties and Publisher Cardinality

**Type**: Refactoring

**Description**:
Removed deprecated geographic properties and relaxed publisher cardinality constraints to improve flexibility and consistency.

**Details**:
- **Geographic Properties**: Removed `schema:geo` and `schema:GeoShape` from Iterations 04 (Places), 10 (Datasets), 11 (Multimedia), and 12 (Semantic Artefact).
- **Publisher Cardinality**: Removed `owl:maxCardinality 1` restriction on `schema:publisher` for `triple:Document` (Iteration 03), allowing multiple publishers.
- **ABOX Cleanup**: Updated `triple:place-northern-italy` in Iteration 11 to be `schema:Place` instead of `schema:GeoShape`.
- **Glossary**: Removed `schema:GeoShape` definitions.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Iterations 10 & 12 - Licensing Bridge Classes

**Type**: Refactoring / Addition

**Description**:
Extended the "Bridge Classes" pattern to Iteration 10 (Datasets) and Iteration 12 (Semantic Artefact), ensuring consistent rights and licensing metadata modeling across all resource types.

**Details**:
- **Dataset (Iteration 10)** & **Semantic Artefact (Iteration 12)**:
  - **TBOX**: Added `triple:License`, `triple:AccessCondition` classes and `triple:hasLicense`, `triple:hasAccessCondition` properties. Added restrictions to main classes.
  - **ABOX**: Added license/access instances and assertions to example resources.
  - **Documentation**: Updated Motivating Scenarios, Glossaries, and added Competency Questions checking for rights metadata.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Iteration 11 - Multimedia Licensing Alignment

**Type**: Refactoring

**Description**:
Refactored Iteration 11 (Multimedia) to align with the "Bridge Classes" pattern introduced in Iteration 02, replacing legacy string-based properties with semantic references.

**Details**:
- **TBOX**:
  - Added `triple:License` and `triple:AccessCondition` bridge classes.
  - Defined `triple:hasLicense` and `triple:hasAccessCondition` properties.
  - Added restrictions to `triple:MediaObject`.
- **ABOX**:
  - Replaced `schema:license` and `schema:conditionsOfAccess` string literals with URI references to new Bridge Class instances.
  - Instantiated specific licenses (e.g., `triple:cc_by_nc_nd_4_0`) and access conditions (e.g., `triple:open_access`).
- **Documentation**:
  - Updated `formal-competency-questions.md` SPARQL queries and expected results.
  - Updated `informal-competency-questions.md` expected results.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Iteration 02 - Bridge Classes and Concept Scheme Removal

**Type**: Refactoring

**Description**:
Refactored Iteration 02 to implement a "Bridge Classes" pattern for controlled vocabularies and simplified the ontology by removing `skos:ConceptScheme`.

**Details**:
- **Bridge Classes**: Defined local classes (`triple:License`, `triple:AccessCondition`, `triple:Discipline`, `triple:ContentType`) that subclass both `skos:Concept` and relevant Dublin Core classes.
- **Properties**:
  - `triple:hasLicense` (subPropertyOf `dcterms:license`)
  - `triple:hasAccessCondition` (subPropertyOf `dcterms:accessRights`)
  - `triple:hasContentType` (subPropertyOf `dcterms:type`)
  - `sioc:topic` (subPropertyOf `dcterms:subject`, removed global range)
- **Restrictions**: Added local `owl:Restriction`s to `triple:Document` for all four properties to enforce typing.
- **Simplification**: Removed `skos:ConceptScheme` definitions and `skos:inScheme` assertions entirely; grouping is now handled via Bridge Classes.
- **Documentation**: Updated `motivating-scenario.md`, `glossary-of-terms.md`, and renumbered Competency Questions (2.1-2.10).

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Removal of schema:additionalType

**Type**: Refactoring

**Description**:
Completely removed `schema:additionalType` property from all iterations of the TRIPLE ontology to resolve inconsistencies and simplify the model.

**Details**:
- Removed TBOX definitions and restrictions from Iterations 01, 02, 10, 11, 12, and consolidated ontology.
- Removed ABOX assertions from all example individuals.
- Removed related competency questions and documentation patterns.
- Verified 0 remaining occurrences in the codebase.

**Author**: Alessandro Bertozzi

---

### 2025-12-21 - Addition: Iteration 13 - CIDOC-CRM and SSHOC-RO Alignment

**Type**: Addition

**Description**:
Implemented Iteration 13 to align TRIPLE ontology classes with CIDOC-CRM and SSHOC-RO using intensional mappings (`skos:exactMatch` and `skos:closeMatch`).

**Details**:
- **Mappings**:
  - `triple:Document`: `cidoc:E31_Document`, `sshocro:SHE8_Publication`
  - `triple:Project`: `cidoc:E7_Activity` (close), `sshocro:SHE3_SSH_Project` (exact)
  - `triple:Dataset`: `sshocro:SHE1_Dataset`
  - `triple:MediaObject` & `triple:SemanticArtefact`: `cidoc:E90_Symbolic_Object` (close)
- **Files**: Updated all files in `development/13/` to reflect these alignments.

**Author**: Alessandro Bertozzi

---

### 2025-12-21 - Addition: Iteration 16 - SKG-IF Alignment

**Type**: Addition

**Description**:
Added Iteration 16 to formally align TRIPLE ontology classes with the SKG-IF (Scientific Knowledge Graph Interoperability Framework) using mappings to FaBiO, FRAPO, and FOAF.

**Details**:
- **New Iteration**: `development/16/`
- **Mappings**:
  - `triple:Document` matches `fabio:ScholarlyWork`
  - `triple:Dataset` matches `fabio:Dataset`
  - `triple:SemanticArtefact` close match `fabio:Work`
  - `triple:MediaObject` close match `fabio:Work`
  - `triple:Profile` matches `foaf:Agent`
  - `triple:Project` close match `frapo:Grant`
- **Documentation**: Added motivating scenario, glossary, and competency questions.

**Author**: Alessandro Bertozzi

---

### 2025-12-21 - Enhancement: Project and Dataset Metadata Extensions

**Type**: Enhancement / Addition

**Description**:
Added contact points to all main ontology entities. Extended Dataset model with DCAT distribution, provenance support, and spatial bounding box properties.

**Details**:

**Iteration 10 (Datasets)**:
- **New Properties**:
  - `dcat:distribution` (Range: `dcat:Distribution`)
  - `dcat:bbox` (Range: `rdfs:Literal`)
  - `dcterms:provenance` (Range: `dcterms:ProvenanceStatement`)
- Added `schema:contactPoint` property

**Iteration 07 (Projects)**:
- Added `schema:contactPoint` property

**Cross-Cutting Changes**:
- Added `schema:contactPoint` to all other main resource types:
  - Iteration 03 (Documents)
  - Iteration 11 (MediaObject/Multimedia)
  - Iteration 12 (Semantic Artefacts)

**Author**: Alessandro Bertozzi

**Commits**:
- a9bddf1 - "add provenance, bbox adn distribution to dataset"
- 6c2f0f6 - "add contact point to project and add dcat distribution to dataset"
- 2115257 - "add contact point to all entities of the ontology"

---

### 2025-12-19 - Refactoring: Project and Dataset Metadata Alignment

**Type**: Refactoring / Addition

**Description**:
Aligned Iteration 07 (Projects) with new metadata requirements and refined identifier usage. Identified Iteration 10 (Datasets) and began metadata alignment. Refactored Iteration 01 to standardise schema.org prefix usage.

**Details**:

**Iteration 07 (Projects)**:
- **Refined Identifiers**:
  - Restricted `datacite:hasIdentifier` to `triple:ID`, `triple:PID`, `triple:OriginalIdentifier`
  - Removed `triple:DOI` and `triple:Handle` from Project restrictions
- **Added Metadata**:
  - `schema:organizer` (Range: `schema:Organization`)
  - `schema:knowsAbout` (Range: `skos:Concept`)
  - `schema:mainEntityOfPage` (Range: `schema:URL`)
  - `schema:inLanguage` (Range: `schema:Language`)
  - `schema:dateCreated`, `schema:dateModified` (Range: `xsd:date`, maxCardinality 1)
- **Files Aligned**: TBOX, ABOX, Motivating Scenario, Glossary, Competency Questions updated

**Iteration 10 (Datasets)**:
- Identified Iteration 10 as the "Dataset" definition iteration
- Added `schema:mainEntityOfPage` with `schema:URL` range
- Performed gap analysis for missing metadata fields

**Iteration 01 (Core)**:
- Refactored property definitions to preferentially use `schema:` prefix (e.g., `schema:inLanguage`, `schema:abstract`, `schema:headline`)

**Author**: Alessandro Bertozzi

---

### 2025-12-12 - Refactoring: Controlled Vocabularies Simplification

**Type**: Refactoring

**Description**:
Simplified controlled vocabularies by removing `datacite:IdentifierScheme` and `datacite:usesIdentifierScheme` from all vocabulary files. Identifiers are now declared as simple `datacite:Identifier` instances without scheme references.

**Details**:
- Removed `datacite:usesIdentifierScheme` property from all identifier declarations
- Removed `datacite:IdentifierScheme` class declarations
- Removed individual identifier scheme instances (`:documentType_identifier`, `:conditionsOfAccess_identifier`, `:licenses_identifier`, `:disciplines_identifier`)
- Fixed `:other` and `:undefined` concept identifiers to follow naming pattern (`:typ_other`, `:acr_other`, `:lic_other`, etc.)
- Maintained all SKOS concept definitions and external vocabulary mappings

**Files Modified**:
- `vocabularies/serializations/ttl/content_types.ttl` - Added `:video` and `:image` concepts (COAR c_12ce, c_c513), removed identifier schemes
- `vocabularies/serializations/ttl/conditions_of_access.ttl` - Removed identifier schemes
- `vocabularies/serializations/ttl/license.ttl` - Removed identifier schemes
- `vocabularies/serializations/ttl/disciplines.ttl` - Removed identifier schemes

**Rationale**:
The identifier scheme pattern added unnecessary complexity to controlled vocabularies. Since vocabularies use a consistent internal identifier pattern and rely on SKOS for semantic alignment with external vocabularies, the explicit scheme declaration was redundant.

**Author**: Alessandro Bertozzi

---

### 2025-12-12 - Refactoring: Iteration 06 Profile Model Simplification

**Type**: Refactoring

**Description**:
Major refactoring of Iteration 06 (Author Profile and User Account) to simplify the profile model by restructuring class hierarchy, removing name decomposition, eliminating "claim" terminology, and removing disambiguation references.

**Details**:

**Phase 1 - Class Hierarchy Restructuring**:
- Changed `triple:Profile` from subclass of `foaf:Person` to superclass
- Made `foaf:Person` and `foaf:Organization` subclasses of `triple:Profile`
- Profiles can now represent either persons or organizations
- Maintained `owl:equivalentClass` between `foaf:Person` and `schema:Person`
- No equivalence between `foaf:Organization` and `schema:Organization` (not overlapping)

**Phase 2 - Name Property Simplification**:
- Removed `schema:givenName` and `schema:familyName` properties
- Profiles now use only `schema:name` (full name string)
- Added cardinality restriction: exactly 1 `schema:name` required per profile
- Updated all ABOX examples to remove name decomposition
- Removed CQ_6.6 (family name query) and renumbered remaining queries

**Phase 3 - Terminology Normalization**:
- Replaced "claim/claimed/unclaimed" terminology with "associate/associated/unassociated"
- Updated all documentation, competency questions, and comments
- More neutral terminology that describes relationship without ownership implications

**Phase 4 - Identifier Requirement**:
- Added cardinality restriction: exactly 1 `datacite:Identifier` required per profile
- Ensures all profiles have unique identifiers

**Phase 5 - Disambiguation Reference Removal**:
- Removed all references to "also known as" relationships between profiles
- Removed concept of "original profile" vs derived profiles
- Simplified disambiguation section in motivating scenario
- No formal property for linking profile variations (previously removed `triple:alsoKnownAs`)
- Updated all examples to remove disambiguation references

**Files Modified**:
- `development/06/TBOX.ttl` - Restructured class hierarchy, added restrictions, removed properties
- `development/06/ABOX.ttl` - Removed givenName/familyName, updated all comments
- `development/06/motivating-scenario.md` - Simplified examples and technical specification
- `development/06/glossary-of-terms.md` - Updated class definitions and property descriptions
- `development/06/informal-competency-questions.md` - Removed CQ_6.4, updated all questions, renumbered
- `development/06/formal-competency-questions.md` - Removed queries, updated descriptions, renumbered

**Final Profile Model**:
- `triple:Profile` (superclass) with restrictions:
  - Exactly 1 `datacite:Identifier`
  - Exactly 1 `schema:name` (xsd:string)
  - Maximum 1 `foaf:account` (foaf:OnlineAccount)
- `foaf:Person` (subclass of triple:Profile)
- `foaf:Organization` (subclass of triple:Profile)

**Competency Questions**: Reduced from 7 to 5 questions (removed CQ_6.4 "original profile" and CQ_6.6 "family name query")

**Rationale**:
Simplified the profile model to focus on core functionality: profiles (person or organization) can be associated with user accounts. Removed complex disambiguation modeling and name decomposition that added unnecessary complexity without formal semantic representation.

**Author**: Alessandro Bertozzi

---

### 2025-12-12 - Documentation: Update README.md

**Type**: Documentation

**Description**:
Updated main README.md to provide clearer project overview and structure.

**Author**: Alessandro Bertozzi

**Commit**: 8bba21d - "update README"

---

### 2025-12-11 - Refactoring: Iterations Renumbering

**Type**: Refactoring

**Description**:
Changed iteration numbering to establish consistent sequence for new resource type iterations.

**Details**:
- Renumbered iterations to maintain logical progression
- Ensures proper iteration ordering in SAMOD development cycle

**Author**: Alessandro Bertozzi

**Commit**: becc9b5 - "change iterations numeration"

---

### 2025-12-10 - Enhancement: Clean TBOX Definitions and Add Controlled Vocabularies

**Type**: Enhancement

**Description**:
Removed redeclarations of imported external ontology classes and properties; added conditions of access and content types vocabularies directly to development iterations.

**Details**:
- Cleaned TBOX files across iterations by removing redundant declarations of Schema.org, FOAF, Dublin Core properties
- Added complete controlled vocabulary definitions for:
  - Conditions of Access (from iteration 09)
  - Content Types (formerly Document Types, from iteration 02)
- Improved ontology modularity and reduced duplication

**Files Modified**:
- Multiple TBOX files across development iterations
- Controlled vocabulary definitions consolidated in iterations 02 and 09

**Author**: Alessandro Bertozzi

**Commit**: c188ead - "remove redeclarations of imported class and properties; add conditions of access and content types"

---

### 2025-12-09 - Documentation: Add Ontology Visualization

**Type**: Documentation

**Description**:
Added GraphML format ontology visualization for enhanced documentation and structural overview.

**Details**:
- Created ontology visualization in GraphML format (yEd compatible)
- Provides visual representation of complete ontology structure
- Enables graph-based analysis and documentation

**Files Created**:
- Ontology visualization in GraphML format

**Author**: Alessandro Bertozzi

**Commit**: 7db2c25 - "add ontology visualization in graphml"

---

### 2025-12-08 - Tooling: Vocabulary Serialization Script

**Type**: Tooling / Automation

**Description**:
Created script to convert vocabulary serializations from RDF/XML to Turtle format.

**Details**:
- New Python script for converting RDF format vocabularies
- Supports automated conversion from RDF/XML to TTL
- Enhanced vocabulary management tooling

**Files Created**:
- Vocabulary conversion script
- New vocabulary serializations in TTL format

**Author**: Alessandro Bertozzi

**Commit**: b0867ab - "add new vocab serializations and script for converting in ttl format from rdf"

---

### 2025-12-07 - Enhancement: Add Vocabularies to Repository

**Type**: Addition

**Description**:
Added controlled vocabularies directly to repository for better accessibility and version control.

**Details**:
- Added complete controlled vocabulary files
- Includes all SKOS ConceptSchemes used in the ontology
- Improves vocabulary governance and traceability

**Files Created**:
- Vocabulary files added to repository structure

**Author**: Alessandro Bertozzi

**Commit**: 00ddd51 - "added vocabularies to repo"

---

### 2025-12-06 - Refactoring: Reorganize Serialization Directory

**Type**: Refactoring

**Description**:
Moved TRIPLE ontology serializations to current directory structure for better organization.

**Details**:
- Reorganized serialization files location
- Moved from nested structure to current directory
- Added MOD namespace binding in merge_graphs function

**Files Modified**:
- Serialization file locations updated
- `scripts/merge_iterations.py` - Added MOD namespace binding

**Author**: Alessandro Bertozzi

**Commits**: 
- db017f8 - "move triple serializations in current dir"
- 6a6d535 - "Add MOD namespace binding in merge_graphs function"

---

### 2025-12-05 - Refactoring: Remove triple:alsoKnownAs Property

**Type**: Refactoring

**Description**:
Removed the `triple:alsoKnownAs` property from the Profile model to simplify author profile management and disambiguation.

**Details**:
- **Iteration 06**: Removed `triple:alsoKnownAs` object property definition and restriction from Profile class
- Updated Profile model to rely solely on `foaf:account` for profile claiming mechanism
- Removed associated competency questions (CQ_6.5, CQ_6.7) and renumbered remaining questions
- Updated ABOX examples to remove alsoKnownAs usage

**Files Modified**:
- `development/06/TBOX.ttl` - Removed triple:alsoKnownAs property definition and Profile restriction
- `development/06/ABOX.ttl` - Removed triple:alsoKnownAs usage from profile examples
- `development/06/glossary-of-terms.md` - Removed triple:alsoKnownAs term definition
- `development/06/motivating-scenario.md` - Removed alsoKnownAs reference
- `development/06/formal-competency-questions.md` - Removed CQ_6.5 and CQ_6.7, renumbered CQ_6.8→CQ_6.6, CQ_6.9→CQ_6.7

**Rationale**:
Simplified profile model by removing complex disambiguation relationships, relying on the simpler claiming mechanism via user accounts for profile management.

**Author**: Alessandro Bertozzi

---

### 2025-11-30 - Refactoring: Major Ontology Architectural Changes

**Type**: Refactoring

**Description**:
Major refactoring introducing class-based identifier types, removing dc:type for content types, implementing controlled vocabularies pattern, and switching subject property from dc:subject to sioc:topic.

**Details**:

**Phase 1 - Identifier Architecture (Nov 25-28)**:
- Implemented class-based identifier types instead of scheme-based pattern:
  - Created `triple:DOI`, `triple:ISSN`, `triple:ISBN`, `triple:Handle`, `triple:ID`, `triple:PID`, `triple:OriginalIdentifier` classes
  - Each identifier class is subclass of `datacite:Identifier`
  - Uses `datacite:usesIdentifierScheme` for scheme references
  - Consolidated schemes to use `datacite:local-resource-identifier-scheme` for local identifiers
  - Extended identifier support to all main entities (Document, Dataset, MediaObject, SemanticArtefact, Project)
- Fixed typos: `usesIdentiferScheme` → `usesIdentifierScheme`
- Added `litre:hasLiteralValue` property with cardinality restrictions
- Distinguished between PID, ID, and OriginalIdentifier for documents

**Phase 2 - Content Types Refactoring (Nov 20-22)**:
- Renamed "Document Types" to "Content Types" across all iterations
- Removed `dc:type` for content type classification
- Updated all TBOX, ABOX, glossaries, and competency questions
- Ensured consistency across all 14 iterations

**Phase 3 - Controlled Vocabularies Pattern (Nov 18-19)**:
- Implemented SKOS-based controlled vocabularies pattern
- Created modular vocabulary files with owl:imports declarations
- Added comprehensive vocabulary documentation
- Standardized ConceptScheme and Concept definitions

**Phase 4 - Subject Property Migration (Nov 15-17)**:
- Replaced `dc:subject` with `sioc:topic` across entire ontology
- Updated all iterations, documentation, and SPARQL queries
- Ensures consistency in subject/topic modeling

**Phase 5 - Schema.org Property Restrictions (Nov 10-14)**:
- Removed rdfs:domain restrictions from Schema.org properties
- Fixed owl:allValuesFrom for schema:mentions property
- Updated rdfs:range for schema:headline and schema:abstract to rdf:langString
- Added cardinality restrictions to date patterns
- Replaced schema:identifier with DataCite pattern across iterations 4, 12-14
- Added constraints to MediaObject, SemanticArtefact, and Dataset

**Phase 6 - Resource Type Classes (Nov 5-8)**:
- Created triple:Project and triple:Dataset classes in TRIPLE namespace
- Created triple:MediaObject class (removed schema-specific subclass)
- Added mod:SemanticArtefact with proper prefix binding
- Updated all class references and documentation

**Phase 7 - Patterns and Status (Nov 1-4)**:
- Created patterns directory for reusable ontology patterns
- Added schema:mentions property pattern for CreativeWork references
- Implemented schema:creativeWorkStatus pattern for Dataset, MediaObject, SemanticArtefact
- Added date cardinality restrictions

**Files Modified**: 100+ files across all iterations

**Files Created**:
- `patterns/` directory with reusable ontology patterns
- Class definition files for new TRIPLE namespace classes
- Updated vocabulary module files

**Rationale**:
These changes establish a more robust, consistent, and interoperable ontology architecture:
- Class-based identifiers provide stronger typing and clearer semantics
- Schema.org properties offer better web integration than Dublin Core
- TRIPLE namespace classes ensure proper ontology ownership
- Controlled vocabularies pattern enables better vocabulary governance
- Removal of domain restrictions allows flexible property reuse

**Author**: Alessandro Bertozzi

**Commits**: 
- 92a0049 - "Implement class-based identifier types"
- 0792f9c - "Updated ABOX and TBOX ontologies to define new identifier classes"
- 92d7ea3 - "Refactor identifier schemes to use datacite prefixes"
- b525216 - "Extension to other doi entities"
- b67ae57 - "extend support to pid, internal_id and original id to other entites"
- 92988c9 - "align URL description pattern; add distinction between pid, id and original id"

- 2a13e43 - "Rename Document Types to Content Types"
- 0707a04 - "Add controlled vocabularies pattern"
- abc9a76 - "Add owl:imports declarations"
- 39a0697 - "Replace dc:subject with sioc:topic"
- 5d56f08 - "Refactor project and dataset classes to use triple:Project and triple:Dataset"
- 180010b - "add to multimedia triple:MediaObject"
- 09d6a18 - "Add mod:SemanticArtefact prefix"
- a393d8c - "Remove rdfs:domain restrictions for schema properties"
- 5429ade - "fix owl:allValuesFrom for schema:mentions property"
- 8b71040 - "Update rdfs:range for schema:headline and schema:abstract"
- 0f04d30 - "Add litre:hasLiteralValue property"
- eef6813 - "Add schema:mentions property and status pattern"
- a393af0 - "add cardinality restriction to date patterns"
- 4a83413 - "add patterns dir"
- 7eb9db9 - "Replace schema:identifier with DataCite pattern"
- 775bac1 - "Update iterations 12-13: add keywords support"
- bac6917 - "Remove skos:exactMatch and skos:closeMatch annotation properties"
- 28a3c47 - "Refactor vocabulary terms"
- 53f9840 - "remove dc:type"
- c43c2cd - "improve prefix management in merge script"
- 9e60f00 - "Add deduplication of OWL restrictions in merge_iterations script"

---

### 2025-12-05 - Enhancement: Standardize Identifier Schemes with DataCite (SUPERSEDED)

**Type**: Enhancement (SUPERSEDED BY NOV 30 REFACTORING)

**Description**:
~~Consolidated all local identifier types (ID, PID, OriginalIdentifier) to use the standardized `datacite:local-resource-identifier-scheme` instead of individual schemes.~~

**Note**: This change was part of the larger identifier architecture refactoring completed on November 30, 2025 (see above).

**Details**:
- **Iterations 01, 12, 13, 14**: Updated `triple:ID`, `triple:PID`, `triple:OriginalIdentifier` classes to use `datacite:local-resource-identifier-scheme`
- Removed individual schemes: `triple:internal_id_schema`, `triple:pid_schema`, `triple:original_id_schema`
- Fixed typo: `usesIdentiferScheme` → `usesIdentifierScheme` in iteration 01 ABOX
- Cleaned up TBOX and ABOX definitions across all affected iterations

**Files Modified**:
- `development/01/TBOX.ttl` - Updated classes and added datacite:local-resource-identifier-scheme
- `development/01/ABOX.ttl` - Fixed typo and cleaned up schema references
- `development/12/TBOX.ttl` - Updated classes and removed old schemas
- `development/12/ABOX.ttl` - Removed old schema definitions
- `development/13/TBOX.ttl` - Updated classes and removed old schemas
- `development/13/ABOX.ttl` - Updated schema references
- `development/14/TBOX.ttl` - Updated classes and removed old schemas

**Rationale**:
Aligns with DataCite standards for local resource identifiers, providing consistency and interoperability across the platform's identifier system.

**Author**: Alessandro Bertozzi

---

### 2025-12-05 - Enhancement: Add dcterms:isReferencedBy to MediaObject and Dataset

**Type**: Enhancement  

**Description**:
Added `dcterms:isReferencedBy` property with restrictions to MediaObject and Dataset classes for consistency with SemanticArtefact.

**Details**:
- **Iteration 12 (Dataset)**: Added restriction `allValuesFrom triple:Document` for `dcterms:isReferencedBy` property
- **Iteration 13 (MediaObject)**: Added `dcterms:isReferencedBy` property definition and restriction `allValuesFrom triple:Document`

**Files Modified**:
- `development/12/TBOX.ttl` - Added dcterms:isReferencedBy restriction to Dataset class
- `development/13/TBOX.ttl` - Added dcterms:isReferencedBy property definition and restriction to MediaObject class

**Rationale**:
Ensures consistent citation modeling across all resource types (Document, SemanticArtefact, MediaObject, Dataset) allowing any resource to be referenced by scholarly documents.

**Author**: Alessandro Bertozzi

---

### 2025-12-05 - Refactoring: Remove Producer Role

**Type**: Refactoring

**Description**:
Removed the "producer" role from the ontology across all SAMOD iterations to simplify the role model.

**Details**:
- **Iteration 03**: Removed `schema:producer` object property and `triple:primaryProducer` property; removed associated restrictions on Document class
- **Iteration 13**: Removed `schema:producer` property and restriction on MediaObject class; updated competency questions, glossary, and ABOX examples

**Files Modified**:
- `development/03/TBOX.ttl` - Removed producer property definitions and restrictions
- `development/13/TBOX.ttl` - Removed schema:producer property and MediaObject restriction
- `development/13/glossary-of-terms.md` - Removed schema:producer term definition
- `development/13/informal-competency-questions.md` - Updated CQ_13.6 to remove producer references
- `development/13/formal-competency-questions.md` - Updated CQ_13.6 SPARQL query to exclude producer
- `development/13/ABOX.ttl` - Removed producer instances from multimedia examples

**Rationale**:
Simplified role model by removing the distinction between producer and other content creation roles, maintaining only essential roles like author, publisher, and provider.

**Author**: Alessandro Bertozzi

---

### 2025-11-10 - Extension: New Resource Type Iterations (12-14)

**Type**: Addition

**Description**:
Added three new iterations to extend the ontology beyond documents to other SSH research resource types: Dataset, Multimedia, and Semantic Artefact.

**New Iterations**:
- **Iteration 12**: Dataset - Research datasets as distinct resource type with comprehensive metadata
- **Iteration 13**: Multimedia - Audio-visual and interactive content (images, videos, audio)
- **Iteration 14**: Semantic Artefact - Ontologies, vocabularies, knowledge graphs, and semantic resources

**Details**:

**Iteration 12 - Dataset**:
- Created `triple:Dataset` class as subclass of schema:Dataset
- Properties: title, abstract, version, encoding format, spatial/temporal coverage, keywords, subjects
- Identifier support: DOI, Handle, ID, PID, OriginalIdentifier
- URL support: landing page, download, source
- Access conditions and license information
- Publisher, provider, and funder relationships
- Publication dates and language support
- Added dcterms:isReferencedBy for citation relationships

**Iteration 13 - Multimedia (MediaObject)**:
- Created `triple:MediaObject` class for audio-visual content
- Properties: title, abstract, encoding format, duration, content size
- Media type classification: image, video, audio, interactive
- Comprehensive identifier and URL support
- Creator, publisher, provider roles
- Subject coverage (keywords, topics, spatial, temporal)
- Access conditions and licensing
- Added dcterms:isReferencedBy for citations
- Removed schema:producer role for simplification

**Iteration 14 - Semantic Artefact**:
- Created `triple:SemanticArtefact` class for ontologies and semantic resources
- Properties: title, abstract, version, namespace URI, preferred prefix
- Semantic resource types: ontology, vocabulary, taxonomy, knowledge graph
- Identifier support following DataCite pattern
- URL patterns for landing page, downloadable files, source repositories
- Creator and publisher information
- Subject classification and keywords
- Temporal and spatial coverage
- License and access conditions

**Common Patterns Across Iterations**:
- DataCite identifier pattern for DOI, Handle, ID, PID, OriginalIdentifier
- URL as DataCite identifier (not schema:url)
- Multilingual metadata support (rdf:langString)
- Controlled vocabularies for types, access conditions, licenses, disciplines
- Schema.org alignment for interoperability
- Comprehensive competency questions with SPARQL tests

**Files Created**:
- `development/12/` - Complete Dataset iteration (motivating scenario, CQs, TBOX, ABOX, glossary)
- `development/13/` - Complete MediaObject iteration (motivating scenario, CQs, TBOX, ABOX, glossary)
- `development/14/` - Complete SemanticArtefact iteration (motivating scenario, CQs, TBOX, ABOX, glossary)

**Rationale**:
GoTriple platform aggregates diverse SSH research outputs beyond traditional documents. These iterations provide formal models for datasets, multimedia resources, and semantic artifacts, enabling comprehensive discovery and interoperability.

**Author**: Alessandro Bertozzi

**Commits**:
- ec5e2b0 - "add iteration 14: Semantic Artifacts"
- aa46c64 - "add iterations 13"
- 6ae4307 - "add iteration 12 for Dataset"
- 82c68d3 - "add iterations draft for new class"
- 11b1e57 - "Add new ontology iteration and update existing ontology definitions"

---

### 2025-11-07 - Restructuring: Iterations Planning and Organization

**Type**: Planning

**Description**:
Initial planning and restructuring for iterations 12-16, creating templates and organizational structure for new resource types.

**Details**:
- Drafted iteration structures for Dataset, Multimedia, Semantic Artefact
- Planned CIDOC-CRM alignment iteration
- Removed release and refactoring plan documents (moved to .gitignore)

**Author**: Alessandro Bertozzi

**Commits**:
- b61a757 - "delete release plan"
- ea3722f - "remove refactoring plan and add to .gitignore"

---

### 2025-10-23 - Refactoring: Minor TBOX Cleaning

**Type**: Refactoring

**Description**:
Minor cleanup of TBOX files across multiple iterations to remove redundant class definitions and improve ontology structure consistency.

**Details**:
- **Iteration 01**: Simplified property definitions and removed redundant comments
- **Iteration 03**: Removed duplicate class definitions that were inherited from external vocabularies
- **Iteration 04**: Removed 40 lines of redundant class and property definitions already defined in previous iterations
- **Iteration 06**: Simplified class definitions by removing redundant property restrictions

**Design Decision**:
Following SAMOD best practices, each iteration should focus only on its specific modelet without re-declaring classes and properties already established in previous iterations. This reduces duplication and improves maintainability.

**Files Modified**:
- `development/01/TBOX.ttl` - 12 lines modified (formatting improvements)
- `development/03/TBOX.ttl` - 9 lines removed (redundant definitions)
- `development/04/TBOX.ttl` - 40 lines removed (redundant definitions)
- `development/06/TBOX.ttl` - 19 lines removed (redundant restrictions)

**Net Changes**: -70 deletions, +10 insertions

**Author**: Alessandro Bertozzi

---

### 2025-10-23 - Refactoring: Remove foaf:Agent Class

**Type**: Refactoring

**Description**:
Removed the unused `foaf:Agent` intermediate class, directly using `foaf:Person` and `foaf:Organization` instead to simplify the class hierarchy.

**Details**:
- **Removed class**: `foaf:Agent` was serving as an unnecessary intermediate class
- **Updated class hierarchy**:
  - `foaf:Person` now directly subclasses `schema:Person` with `schema:name` restriction
  - `foaf:Organization` now directly subclasses with `schema:name` restriction
  - Both classes maintain the same cardinality constraint: exactly 1 `schema:name` (xsd:string)
- **ABOX updates**: Simplified instance declarations in iterations 03 and 06
- **Documentation updates**: Updated glossary files to reflect the simplified class structure
- **Rationale**: FOAF already provides `foaf:Person` and `foaf:Organization` which are standard and well-adopted. The intermediate `foaf:Agent` class added complexity without semantic benefit.

**Files Modified**:
- `.gitignore` - Added Python cache exclusions
- `development/03/TBOX.ttl` - Removed `foaf:Agent` class, moved restrictions to `foaf:Person` and `foaf:Organization`
- `development/03/ABOX.ttl` - Simplified agent instances
- `development/06/TBOX.ttl` - Removed `foaf:Agent` class, moved restrictions to `foaf:Person` and `foaf:Organization`
- `development/06/ABOX.ttl` - Simplified agent instances
- `development/06/glossary-of-terms.md` - Removed `foaf:Agent` term definition
- `development/07/glossary-of-terms.md` - Updated class hierarchy documentation

**Net Changes**: +32 insertions, -60 deletions

**Author**: Development team

---

### 2025-10-23 - Iteration 01: Addition of Core Descriptive Metadata and URL Identifiers

**Type**: Addition

**Description**:
Enhanced Iteration 01 with essential descriptive metadata properties (title, abstract, format) and comprehensive URL identifier support using DataCite pattern for consistency.

**Details**:

**Part 1 - Core Descriptive Metadata**:
- **New properties added**:
  - `schema:headline` - Document title (multilingual, rdf:langString)
  - `schema:abstract` - Document abstract/summary (multilingual, rdf:langString)
  - `schema:encodingFormat` - File format as MIME type (xsd:string)
- **TBOX updates**: Added three new data properties with cardinality restrictions on `triple:Document`
- **ABOX examples**:
  - `document_1` with bilingual title/abstract (English & French) + PDF format
  - `document_31` with English title/abstract + HTML format
- **Competency questions**: Added 5 new questions (CQ_1.8 to CQ_1.12) with corresponding SPARQL queries
- **Coverage impact**: 70.8% (17/24) → 83.3% (20/24)

**Part 2 - URL Identifier Support**:
- **New IdentifierSchemes**:
  - `triple:landing_page_url` - Landing page with metadata and descriptive information
  - `triple:full_text_url` - Direct access to full document content
  - `triple:source_url` - Original publication location or source repository
- **Design decision**: Used DataCite Identifier pattern instead of Schema.org direct properties (`schema:url`, `schema:mainEntityOfPage`, `schema:isBasedOnURL`) to maintain consistency with DOI, ISBN, ISSN, Handle identifiers
- **ABOX examples**: Added 3 URL identifiers to `document_1`:
  - Landing page: https://hal.archives-ouvertes.fr/hal-12345
  - Full text: https://hal.archives-ouvertes.fr/hal-12345/document
  - Source: https://journals.openedition.org/dh/12345
- **Competency questions**: Added 2 new questions (CQ_1.13, CQ_1.14) with SPARQL queries for URL retrieval
- **Coverage impact**: 83.3% (20/24) → **95.8% (23/24)**

**Files Modified**:
- `development/01/TBOX.ttl` - Added 3 data properties with restrictions
- `development/01/ABOX.ttl` - Added 3 IdentifierSchemes + 3 URL identifiers + metadata examples
- `development/01/motivating-scenario.md` - Updated technical specification and Example 1
- `development/01/informal-competency-questions.md` - Added 7 new questions (CQ_1.8 to CQ_1.14)
- `development/01/formal-competency-questions.md` - Added 7 SPARQL queries
- `development/01/glossary-of-terms.md` - Added 6 new terms

**Rationale**:
The DataCite approach for URLs ensures architectural consistency, strong typing, and alignment with scholarly publishing standards used by major SSH repositories (HAL, Zenodo, OpenAIRE). This pattern allows distinguishing between different URL types while maintaining the same structure as academic identifiers.

**Author**: Development team

---

### 2025-10-23 - Iteration 06: Refactoring to Remove PRO Ontology References

**Type**: Refactoring

**Description**:
Completely refactored Iteration 06 to remove all references to the PRO (Publishing Roles Ontology) and updated the author profile model to use Schema.org and FOAF properties directly.

**Details**:
- **Removed PRO ontology**: Eliminated all references to `pro:RoleInTime`, `pro:withRole`, `pro:isHeldBy`, `pro:isDocumentContextFor`
- **Updated model**: Documents now link directly to author profiles using `schema:author` property
- **Profile claiming mechanism**: Profiles can be "claimed" or "unclaimed" based on presence of `foaf:account` property
- **Name decomposition**: Added `schema:givenName` and `schema:familyName` to all profiles for better name disambiguation
- **Realistic examples**: Replaced generic placeholder names with realistic examples:
  - Example 1: John Smith / J. Smith (name variation disambiguation)
  - Example 2: Maria Rossi with 3 variants (Maria Rossi, M. Rossi, Maria R. Rossi) + Pierre Dupont (unclaimed)
  - Example 3: Single user account claiming multiple profile variations
- **Documentation updates**:
  - Completely rewritten glossary (15 terms) removing PRO concepts
  - Updated motivating scenario with clear technical specification
  - Enhanced all 5 informal competency questions
  - Added new CQ_6.6 for givenName/familyName queries
  - Added new CQ_6.9 SPARQL query for filtering by family name
- **Updated formal competency questions**: All SPARQL queries now use `schema:author` instead of PRO patterns

**Files Modified**:
- `development/06/glossary-of-terms.md` - Completely rewritten (removed 6 PRO terms, added 15 correct terms)
- `development/06/motivating-scenario.md` - Technical specification and all 3 examples rewritten
- `development/06/informal-competency-questions.md` - All 5 questions updated + 1 new question added
- `development/06/ABOX.ttl` - Added givenName/familyName to all 5 profiles with realistic names
- `development/06/formal-competency-questions.md` - Updated expected results + 1 new SPARQL query
- `development/05/formal-competency-questions.md` - Removed PRO prefix, updated CQ_5.2
- `development/07/motivating-scenario.md` - Removed PRO pattern description

**Design Decision**:
Simplified author attribution by using direct `schema:author` links instead of complex role-in-time patterns. The claiming mechanism (presence/absence of `foaf:account`) provides clearer semantics for claimed vs unclaimed profiles.

**Competency Questions**: 9 total (was 8, added 1 for name decomposition)

**Author**: Development team

---

### 2025-10-23 - Iteration 07: Projects (Research Projects in SSH Domain) - Completion

**Type**: Addition

**Description**:
Completed Iteration 07 by extending and formalizing competency questions for SSH research projects, expanding TBOX/ABOX with comprehensive examples and full SPARQL test coverage.

**Details**:
- Extended motivating scenarios from basic project description to **4 comprehensive examples**:
  - TRIPLE-SSH project funded by Horizon 2020 (EU Commission)
  - National research project on migration studies (PRIN-funded)
  - Collaborative heritage documentation project (multi-funder: FWF + Getty Foundation)
  - ERC Advanced Grant on ancient philosophy
- Expanded informal competency questions from **3 to 10 questions** covering:
  - Project metadata retrieval (identifiers, dates, names, descriptions)
  - Multi-funder/sponsor analysis
  - Discipline/topic filtering and search
  - Duration calculations and temporal queries
  - Identifier scheme usage patterns
  - Organization funding analysis
  - Keyword frequency analysis
  - Full-text search across project fields
- Expanded formal competency questions from **3 basic to 10 comprehensive SPARQL queries**
  - Enhanced CQ_7.1: Complete metadata properties query with optional fields
  - Enhanced CQ_7.2: Funding grants with funder and sponsor details
  - New CQ_7.3: Multi-funder project identification
  - New CQ_7.4: Discipline-based project filtering (e.g., Digital Humanities)
  - New CQ_7.5: Project duration calculations
  - New CQ_7.6: Temporal filtering (projects active in specific period)
  - New CQ_7.7: Identifier scheme enumeration
  - New CQ_7.8: Organization funding patterns (multi-project funders)
  - New CQ_7.9: Keyword frequency analysis
  - New CQ_7.10: Full-text search in project metadata
- Completed TBOX.ttl with **170 lines** defining:
  - `schema:Project` class with comprehensive restrictions
  - Properties: `schema:about`, `schema:funder`, `schema:funding`, `schema:keywords`, `schema:sponsor`
  - Data properties: `schema:alternateName`, `schema:description`, `schema:startDate`, `schema:endDate`
  - Support classes: `schema:Grant`, `schema:DefinedTerm`
  - Cardinality constraints and value type restrictions
- Completed ABOX.ttl with **259 lines** containing:
  - 4 complete project instances with realistic metadata
  - 5 identifier schemes (H2020, PRIN, FWF, Getty, ERC)
  - 10 organizations (funders, sponsors, coordinating entities)
  - 5 grants with funder/sponsor relationships
  - 8 topics/disciplines (SKOS concepts)
  - 15 keywords (defined terms)
- Updated glossary with **26 terms** defining all classes and properties

**Design Patterns**:
- Used `schema:Grant` with `schema:funder` and `schema:sponsor` for funding relationships
- Projects can have multiple grants (multi-funder support)
- Temporal information via `xsd:date` typed literals
- Multilingual support for names, acronyms, descriptions (`rdf:langString`)
- Subject indexing via SKOS concepts and Schema.org DefinedTerms
- Reused DataCite identifier pattern from Iteration 01

**Files Modified**:
- `development/07/motivating-scenario.md` - Extended from 1 to 4 examples (+106 lines)
- `development/07/informal-competency-questions.md` - Expanded from 3 to 10 questions (+193 lines)
- `development/07/glossary-of-terms.md` - Refined and completed 26 term definitions (+51 lines change)
- `development/07/TBOX.ttl` - Created complete terminological box (+170 lines)
- `development/07/ABOX.ttl` - Created complete assertional box (+259 lines)
- `development/07/formal-competency-questions.md` - Expanded from 3 to 10 SPARQL queries (+298 lines)

**Artifacts Pending**:
- `development/07/modelet.graphml` (Graffoo diagram source)
- `development/07/modelet.png` (Visual diagram)

**Statistics**:
- Total changes: +1077 insertions, -70 deletions
- 6 files modified
- 10 competency questions with full SPARQL coverage
- 4 realistic project examples with complete metadata

**Author**: Development team

---

### 2025-10-23 - Refactoring: Introduction of triple:Document

**Type**: Refactoring

**Description**:
Major refactoring to introduce `triple:Document` class in the TRIPLE namespace with dual inheritance pattern, replacing incorrect usage of `foaf:Document` throughout all iterations.

**Details**:
- **Main Change**: Defined `triple:Document` as subclass of both `schema:CreativeWork` and `foaf:Document`
  - Establishes dual inheritance pattern for semantic interoperability
  - Resolves namespace ownership issues (TRIPLE ontology now owns its Document class)
  - Maintains compatibility with both Schema.org and FOAF vocabularies
- **Iteration 01**: Foundational `triple:Document` definition with labels, comments, and restrictions for document types, identifiers, and languages
- **Iteration 02**: Expanded controlled vocabularies with 4 complete examples (License, Access Conditions, Document Type, Discipline) including real external matches to COAR, Creative Commons, and Library of Congress; added 10 informal and 12 formal competency questions; corrected `skos:definition` from `owl:DatatypeProperty` to `owl:AnnotationProperty` (SKOS compliance)
- **Iteration 03**: Updated property domains and 2 document instances
- **Iteration 04**: Updated property domains and class definitions
- **Iteration 05**: Simplified to focus only on Cluster and isDiscarded functionality (removed redundant definitions from previous iterations following SAMOD best practices)
- **Iteration 06**: Added `triple:Document` with author profile restrictions, updated 5 document instances
- **Iteration 08**: Added `triple:Document` with `dc:type` restrictions, updated 2 document instances
- **Iteration 09**: Added `triple:Document` with `schema:conditionsOfAccess` restrictions, updated 3 document instances
- **Iteration 10**: Added `triple:Document` with `datacite:hasIdentifier` restrictions, updated 4 document instances, fixed 2 SPARQL queries
- **Iteration 11**: Resolved `schema:CreativeWork` conflict, updated 8 document instances, fixed 5 SPARQL queries

**Design Decision**:
Chose dual inheritance (`schema:CreativeWork` + `foaf:Document`) to maximize interoperability with both Schema.org (widely used for web semantics) and FOAF (standard for social networks and scholarly communications).

**Files Modified**: 31 files across 10 iterations
- TBOX files: 10 (iterations 01-06, 08-11)
- ABOX files: 10 (iterations 01-06, 08-11)
- Documentation files: 11 (motivating scenarios, glossaries, competency questions)

**Statistics**:
- Document instances updated: 22
- SPARQL queries corrected: 7
- Net changes: +1118 insertions, -664 deletions (+454 lines)

**Author**: Alessandro Bertozzi

---

## [2.0.0] - 2025-10-24

### 2025-10-24 - Version 2.0.0 Release: Complete Ontology Serialization and Enhanced Metadata

**Type**: Major Release

**Description**:
Major release introducing complete ontology serialization (version 2.0.0) with comprehensive metadata, proper authorship attribution, and enhanced documentation following semantic web best practices.

**Key Changes**:

1. **Complete Ontology Serialization**:
   - Created final merged ontology from 11 SAMOD iterations (development/01 through development/11)
   - Generated multiple serialization formats: TTL, OWL/XML, JSON-LD, N-Triples
   - Added comprehensive HTML documentation with interactive features

2. **Enhanced Metadata**:
   - Added proper authorship: Alessandro Bertozzi (creator), Luca De Santis & Silvio Peroni (contributors)
   - Included comprehensive Dublin Core metadata (title, description, license, rights, subjects, etc.)
   - Added VANN vocabulary annotations (preferred namespace prefix and URI)
   - Included DCAT keywords for better discoverability
   - Added bibliographic citations in both Dublin Core and Schema.org formats

3. **Version Management**:
   - Updated to version 2.0.0 across all metadata fields
   - Added `owl:priorVersion` reference to version 1.0.0
   - Consistent version numbering in `owl:versionInfo`, `owl:versionIRI`, and `schema:version`

4. **External Ontology Label Standardization**:
   - Implemented consistent `prefix:LocalName` format for all external ontology references
   - Updated CLAUDE.md with comprehensive guidelines for ontology metadata and serialization
   - Documented naming conventions for future development

5. **Technical Improvements**:
   - All annotation properties properly declared
   - Complete prefix declarations including vann: and dcat: vocabularies
   - Enhanced ontology structure with proper OWL2 compliance

**Files Added**:
- `ontology/2025-10-24/serializations/triple.ttl` (834 lines)
- `ontology/2025-10-24/serializations/triple.owl` (1360 lines)
- `ontology/2025-10-24/serializations/triple.jsonld` (1614 lines)
- `ontology/2025-10-24/serializations/triple.nt` (838 lines)
- `ontology/2025-10-24/html/index-en.html` (1384 lines)
- Complete HTML documentation with resources (CSS, JS, icons)

**Files Modified**:
- `CLAUDE.md` - Updated with comprehensive ontology metadata guidelines
- Removed legacy `ontology/triple-ontology.ttl` (639 lines)

**Net Changes**: +7150 insertions, -639 deletions

**Author**: Alessandro Bertozzi

**Commit**: 3ce0f35 - "add new complete serialization and documentation"

---

## [1.0.0] - 2025-10-22

### Release v1.0.0 - First Stable Release of TRIPLE Ontology

**Type**: Release

**Description**:
First stable release of the TRIPLE ontology, representing the complete ontology with all 7 original SAMOD iterations plus 4 extension iterations (08-11).

**Details**:
- Complete ontology package with development artifacts for 11 iterations
- Refactored diagrams (Graffoo notation) for all iterations
- Refactored SPARQL competency questions organized by iteration
- HTML documentation and controlled vocabularies
- Release includes:
  - `development/` directory with all 11 iterations (motivating scenarios, glossaries, TBOX/ABOX, competency questions, diagrams)
  - `diagrams/` directory with visual representations (01.png - 07.png)
  - `sparql/` directory with refactored competency questions (01.md - 07.md)
  - `serializations/` directory with consolidated ontology in Turtle format

**Technical Changes**:
- Updated release date to 2025-10-22
- Changed `owl:versionIRI` to `owl:versionInfo` for stable URI management
- Complete package structure for reproducibility and documentation

**Ontology Coverage**:
- **Core Features** (Iterations 01-07):
  1. Document basics (types, languages, identifiers, metadata)
  2. Controlled vocabularies (license, access conditions, document types, disciplines)
  3. Document roles (author, contributor, publisher, provider, funder)
  4. Subject coverage (temporal, spatial, keywords)
  5. Duplicate handling and discarded entities
  6. Author profiles and user accounts
  7. Projects (SSH research projects)

- **Extensions** (Iterations 08-11):
  8. Book part document type with COAR alignment
  9. Access conditions vocabulary with COAR alignment
  10. Document identifier types (DOI, ISSN, ISBN, Handle)
  11. Document mentions and references

**Release Artifacts**:
- `releases/2025-10-14/` directory with complete package
- `releases/2025-10-14/RELEASE-NOTES.md` with detailed release information
- 95 files packaged (TBOX, ABOX, diagrams, SPARQL queries, documentation)

**Author**: Development team

---

### 2025-10-06 - Documentation: JSON-LD Examples

**Type**: Documentation

**Description**:
Created examples directory with JSON-LD serialization examples demonstrating practical application of the TRIPLE ontology.

**Details**:
- Created `examples/` directory structure for data export examples
- Added comprehensive JSON-LD example demonstrating all ontology features:
  - Multilingual metadata (title, abstract in EN/FR)
  - Document types and access conditions with COAR mappings
  - Multiple identifier schemes (DOI, Handle)
  - Subject coverage (keywords, spatial, temporal, disciplines)
  - Role modeling (authors, publisher) with time intervals
  - Document mentions (citations, people, projects)
  - Cluster membership and discard flag
- Created JSON-LD reading guide explaining:
  - Key JSON-LD concepts (`@context`, `@id`, `@type`, `@value`, `@graph`)
  - How to read nested objects and arrays
  - Translation to RDF Turtle format
  - Validation and conversion tools
- Updated main `.gitignore` to exclude `CLAUDE.md`

**Files Created**:
- `examples/README.md` - Directory structure and purpose documentation
- `examples/jsonld/README.md` - JSON-LD reading guide
- `examples/jsonld/document-complete-example.jsonld` - Comprehensive document example

**Files Modified**:
- `.gitignore` - Added CLAUDE.md exclusion

**Purpose**:
- Reference implementations for data producers
- Test cases for ontology validation
- Templates for creating new data exports
- Practical documentation of ontology patterns

**Author**: Development team

---

### 2025-10-06 - Tooling: Ontology Merge Script

**Type**: Tooling / Automation

**Description**:
Created Python script to merge all TBOX files from development iterations into a single consolidated ontology file containing only the ontology structure (no instance data).

**Details**:
- Created `scripts/` directory with merge automation tooling
- Script merges all `TBOX.ttl` files from `development/` iterations (01-11)
- Skips `ABOX.ttl` files to exclude instance data
- Outputs consolidated ontology to `ontology/triple-ontology.ttl`
- Adds ontology metadata (version IRI, labels, comments, dates)
- Provides statistics about merged ontology:
  - Classes count
  - Object properties count
  - Data properties count
  - Total triples count
- Uses RDFlib for RDF graph manipulation
- Virtual environment support with `.gitignore` for Python artifacts
- Comprehensive documentation in `scripts/README.md`

**Current Output**:
- **File**: `ontology/triple-ontology.ttl`
- **Size**: 14KB, 372 lines
- **Content**: 331 triples (TBOX only)
  - 23 classes
  - 25 object properties
  - 7 data properties

**Files Created**:
- `scripts/merge_iterations.py` - Main merge script
- `scripts/requirements.txt` - Python dependencies (rdflib==7.0.0)
- `scripts/README.md` - Script documentation and usage guide
- `scripts/.gitignore` - Python/venv artifacts exclusion
- `ontology/triple-ontology.ttl` - Consolidated ontology output (TBOX only)

**Usage**:
```bash
# Default output to ../ontology/triple-ontology.ttl
python merge_iterations.py

# Custom output path
python merge_iterations.py --output /path/to/output.ttl
```

**Author**: Development team

---

### 2025-10-05 - Iteration 11: Document Mentions and References

**Type**: Addition

**Description**:
Added support for documents to mention other entities (documents, people, projects, organizations) using the Schema.org `schema:mentions` property.

**Details**:
- Implemented generic mentions functionality using `schema:mentions` property
- Documents can mention various types of entities:
  - **Other Documents** (`foaf:Document`) - citations and bibliographic references
  - **People** (`foaf:Person`) - researchers or scholars discussed in the text
  - **Projects** (`schema:Project`) - research projects referenced or evaluated
  - **Organizations** (`foaf:Organization`) - institutions or research centers mentioned
- Established explicit compatibility: `foaf:Document rdfs:subClassOf schema:CreativeWork`
- Also declared: `foaf:Person rdfs:subClassOf schema:Thing` and `foaf:Organization rdfs:subClassOf schema:Thing`
- Flexible range allows mentioning any type of entity while maintaining simplicity
- SPARQL queries can filter mentions by type when needed
- Enables:
  - Citation network analysis
  - Discovery of related resources
  - Context enrichment for documents
  - Cross-referencing across entity types

**Design Decision**:
Chose Schema.org generic `schema:mentions` (Opzione A) over specialized sub-properties for simplicity and maximum flexibility. Entity types are distinguished through SPARQL type filtering.

**Files Created**:
- `development/11/motivating-scenario.md`
- `development/11/informal-competency-questions.md`
- `development/11/glossary-of-terms.md`
- `development/11/TBOX.ttl`
- `development/11/ABOX.ttl`
- `development/11/formal-competency-questions.md`

**Artifacts Pending**:
- `development/11/modelet.graphml` (Graffoo diagram source)
- `development/11/modelet.png` (Visual diagram)

**Competency Questions**: 9 questions defined and tested
- CQ_11.1: Retrieve all entities mentioned by a document
- CQ_11.2: Get documents mentioned by a specific document
- CQ_11.3: Find documents mentioning a specific person
- CQ_11.4: List all projects mentioned in any document
- CQ_11.5: Get organizations mentioned by a document
- CQ_11.6: Retrieve people mentioned by a document
- CQ_11.7: Find documents that cite other documents
- CQ_11.8: Get mentioned entities with their types
- CQ_11.9: Count mentions per document (with aggregation)

**Author**: Development team

---

### 2025-10-04 - Iteration 10: Document Identifier Types Extension

**Type**: Addition / Extension

**Description**:
Extended the ontology to explicitly support the four primary identifier schemes used in academic publishing: DOI, ISSN, ISBN, and Handle.

**Details**:
- Formalized four standard identifier schemes as instances of `datacite:IdentifierScheme` following DataCite naming conventions:
  - **DOI** (`triple:doi`) - Digital Object Identifier for persistent identification of digital objects
  - **ISSN** (`triple:issn`) - International Standard Serial Number for serial publications
  - **ISBN** (`triple:isbn`) - International Standard Book Number for books and book-like products
  - **Handle** (`triple:handle`) - Handle System for persistent identifier infrastructure
- Each identifier scheme includes:
  - `rdfs:label` for human-readable name (e.g., "DOI"@en)
  - `rdfs:comment` for detailed description
- Each identifier (`datacite:Identifier`) must use exactly one scheme via `datacite:usesIdentifierScheme`
- Each identifier must have exactly one literal value via `litre:hasLiteralValue`
- Documents can have multiple identifiers of different types
- Added cardinality restrictions to ensure data integrity:
  - `datacite:Identifier` has exactly 1 `datacite:IdentifierScheme`
  - `datacite:Identifier` has exactly 1 literal value (xsd:string)
- Naming convention follows DataCite standards (simple names without "_scheme" suffix)
- Builds upon the identifier pattern established in Iteration 01

**Files Created**:
- `development/10/motivating-scenario.md`
- `development/10/informal-competency-questions.md`
- `development/10/glossary-of-terms.md`
- `development/10/TBOX.ttl`
- `development/10/ABOX.ttl`
- `development/10/formal-competency-questions.md`

**Artifacts Pending**:
- `development/10/modelet.graphml` (Graffoo diagram source)
- `development/10/modelet.png` (Visual diagram)

**Competency Questions**: 9 questions defined and tested
- CQ_10.1: Retrieve all DOI identifiers
- CQ_10.2: Get identifier scheme for specific identifier
- CQ_10.3: Find documents with DOI identifiers
- CQ_10.4: List all identifier schemes
- CQ_10.5: Get all identifiers and schemes for a document
- CQ_10.6: Retrieve literal value of specific identifier
- CQ_10.7: Find documents with ISBN identifiers
- CQ_10.8: Get identifiers and schemes for specific document
- CQ_10.9: Retrieve all identifiers with schemes and values

**Author**: Development team

---

### 2025-10-03 - Iteration 09: Access Conditions Vocabulary Extension and COAR Alignment

**Type**: Addition / Mapping

**Description**:
Extended the `conditions_of_access` controlled vocabulary by mapping and adding four COAR (Confederation of Open Access Repositories) access rights terms.

**Details**:
- Mapped existing GoTriple access conditions vocabulary to COAR Access Rights standard
- Added four access level terms with `skos:exactMatch` to COAR URIs:
  - **Embargoed Access** (`acc_embargoed-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_f1cf/`
  - **Metadata Only Access** (`acc_metadata-only-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_14cb/`
  - **Open Access** (`acc_open-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_abf2/`
  - **Restricted Access** (`acc_restricted-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_16ec/`
- Each term is a `skos:Concept` within the `triple:conditions_of_access` ConceptScheme
- Documents are linked to access conditions via `schema:conditionsOfAccess` property
- Ensures interoperability with global repository networks and scholarly infrastructures

**Files Created**:
- `development/09/motivating-scenario.md`
- `development/09/informal-competency-questions.md`
- `development/09/glossary-of-terms.md`
- `development/09/TBOX.ttl`
- `development/09/ABOX.ttl`
- `development/09/formal-competency-questions.md`

**Artifacts Pending**:
- `development/09/modelet.graphml` (Graffoo diagram source)
- `development/09/modelet.png` (Visual diagram)

**Competency Questions**: 7 questions defined and tested
- CQ_9.1: Retrieve documents with open access
- CQ_9.2: Identify vocabulary scheme for access terms
- CQ_9.3: Get all COAR external term mappings
- CQ_9.4: Get access condition for specific document
- CQ_9.5: List all access condition terms in vocabulary
- CQ_9.6: Retrieve documents with metadata-only access
- CQ_9.7: Get COAR external term for specific access condition

**Author**: Development team

---

### 2025-10-02 - Iteration 08: Book Part Document Type

**Type**: Addition

**Description**:
Added "Book part" document type to the Document Types controlled vocabulary.

**Details**:
- Created Iteration 08 following SAMOD methodology
- Added `typ_book-part` as a new `skos:Concept` in the `document_types` vocabulary
- Established `skos:exactMatch` alignment with COAR resource type: `https://vocabularies.coar-repositories.org/resource_types/c_3248/`
- Book part represents portions of books such as chapters, sections, or contributions to edited volumes
- Documents can be classified as book parts using `dc:type` property

**Files Created**:
- `development/08/motivating-scenario.md`
- `development/08/informal-competency-questions.md`
- `development/08/glossary-of-terms.md`
- `development/08/TBOX.ttl`
- `development/08/ABOX.ttl`
- `development/08/formal-competency-questions.md`

**Artifacts Pending**:
- `development/08/modelet.graphml` (Graffoo diagram source)
- `development/08/modelet.png` (Visual diagram)

**Competency Questions**: 5 questions defined and tested
- CQ_8.1: Retrieve documents with "Book part" type
- CQ_8.2: Identify vocabulary scheme for `typ_book-part`
- CQ_8.3: Get external term alignments
- CQ_8.4: Get document type for specific document
- CQ_8.5: List all document types in vocabulary

**Author**: Development team

---

### 2025-10-05 - Documentation Enhancement

**Type**: Documentation

**Description**:
Enhanced project documentation with SAMOD methodology guide.

**Details**:
- Created `SAMOD-METHODOLOGY.md` with detailed explanation of the three-phase SAMOD cycle

**Files Created**:
- `SAMOD-METHODOLOGY.md`

**Author**: Development team

---

## Previous Development (Iterations 01-07)

The initial seven iterations of the TRIPLE ontology were developed following SAMOD methodology, covering:

1. **Iteration 01**: GoTriple Document basics (types, languages, identifiers, metadata)
2. **Iteration 02**: Controlled vocabularies (license, access conditions, document types, disciplines)
3. **Iteration 03**: Document roles (author, contributor, publisher, provider, funder, etc.)
4. **Iteration 04**: Subject coverage (temporal, spatial, keywords)
5. **Iteration 05**: Duplicate handling (document clusters) and discarded entities (flagged authors/keywords)
6. **Iteration 06**: Author profiles and user accounts (disambiguation, claimed/unclaimed profiles)
7. **Iteration 07**: Projects (SSH research projects with metadata, roles, subjects)

**Base ontology established**:
- Namespace: `https://gotriple.eu/ontology/triple#`
- Format: RDF/Turtle
- External standards integrated: FOAF, Dublin Core, DataCite, Schema.org, SKOS, SPAR

---

## Notes

- All changes follow the SAMOD (Simplified Agile Methodology for Ontology Development) three-phase cycle
- Each iteration includes: motivating scenario, competency questions (informal and formal), glossary, TBOX, ABOX, and diagrams
- Competency questions are tested with SPARQL queries against instance data
- Visual documentation uses Graffoo notation for OWL ontologies
