---
title: Introduction
terms:
---

### 1.1. Background and Motivation

[GoTriple](https://www.gotriple.eu) is a multilingual discovery platform for the
Social Sciences and Humanities (SSH): it aggregates documents, datasets, projects
and researcher profiles from heterogeneous European sources, normalizes them
through its processing pipeline, and enriches them with automatic classification,
entity extraction and machine translation. The TRIPLE Ontology is the data model
of that platform in semantic form: it states what a GoTriple record *is* — which
entities exist, which properties describe them, which controlled vocabularies
their values come from — so that the aggregated data can be published, queried
and reused as a knowledge graph.

The ontology deliberately **reuses before it mints**: the descriptive backbone is
[Schema.org](https://schema.org), agents are [FOAF](http://xmlns.com/foaf/spec/),
identifiers follow the [DataCite Ontology](http://purl.org/spar/datacite),
datasets borrow from [DCAT](https://www.w3.org/TR/vocab-dcat-3/), annotations from
the [Web Annotation Vocabulary](https://www.w3.org/TR/annotation-vocab/). A term
of our own (`triple:` namespace) exists only where no external term says the right
thing — and each such term records why it exists.

### 1.2. One Model, Six Vocabularies

The ontology ships as **one consolidated model** plus **six controlled
vocabularies**, published side by side under the same root:

| Artefact | Namespace | Prefix |
|---|---|---|
| TRIPLE model (this document) | `https://gotriple.eu/ontology/triple/` | `triple:` |
| Discipline | `https://gotriple.eu/ontology/discipline/` | `disc:` |
| ContentType | `https://gotriple.eu/ontology/content-type/` | `ct:` |
| ConditionOfAccess | `https://gotriple.eu/ontology/condition-of-access/` | `coa:` |
| License | `https://gotriple.eu/ontology/license/` | `lic:` |
| ProjectType | `https://gotriple.eu/ontology/project-type/` | `pt:` |
| DDC proxies | `https://gotriple.eu/ontology/ddc/` | `ddc:` |

Concept IRIs inside the vocabularies use the **production key verbatim**
(`disc:musiq`, `ct:typ_article`, `coa:acr_open-access`): the local name of a
concept is exactly the value the GoTriple API emits for it, so mapping a record
to the graph is namespace + key, with no lookup table. The full minting rules are
in `URI-CONVENTIONS.md` in the ontology repository.

### 1.3. Methodology

The model is developed with [SAMOD](https://essepuntato.it/samod/) (Simplified
Agile Methodology for Ontology Development): every piece was introduced by an
iteration with a motivating scenario, competency questions and a tested exemplar
dataset. The iterations — twenty-one at the time of writing — are the reasoned
record of the model: each design decision can be traced to the scenario that
motivated it and to the queries that verify it.

### 1.4. How to Read This Document

The document is organized in thematic chapters, each describing one area of the
model: its terms, the constraints that hold there, and worked examples. A term
entry shows the IRI, the definition, the formal axioms and, where useful, a usage
note and an example. Superscript badges mark the kind of term:
<sup class="type-c">c</sup> class, <sup class="type-op">op</sup> object property,
<sup class="type-dp">dp</sup> datatype property, <sup class="type-ni">ni</sup>
named individual.

Terms borrowed from external ontologies are labelled with their prefixed name
(`schema:headline`, `foaf:name`) and documented **contextually**: the comment
describes how GoTriple uses the term, while the authoritative definition remains
with the source ontology. The thematic chapters are the narrative of the model;
the **full definition of every term** lives in the reference sections at the
bottom of the document (Classes, Object Properties, Datatype Properties, Named
Individuals), where each chapter's Vocabulary list points. The complete
namespace table closes the document.

### 1.5. Examples

Examples are given in [Turtle](https://www.w3.org/TR/turtle/). The subjects that
appear in them (`https://w3id.org/gto/document/…`) follow the IRI policy of the
platform's knowledge graph; entity names such as `document_1` are exemplar data
from the SAMOD iterations, not production records.

### 1.6. Conformance

The OWL axioms in this document state what the terms *mean*; they are
deliberately light on cardinality. What a conformant GoTriple record **must**
carry is expressed separately, as [SHACL](https://www.w3.org/TR/shacl/) shapes
(`shapes/` in the repository): integrity conditions cited in the chapters below
refer to those shapes. This split keeps the open-world semantics of the ontology
clean while giving the platform a closed-world validation profile.
