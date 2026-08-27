---
title: Annotations and Enrichment
terms: oa:Annotation oa:Motivation oa:hasBody oa:hasTarget oa:motivatedBy oa:classifying oa:identifying oa:tagging dcterms:creator confidence isDiscarded detectedLanguage machineTranslatedLanguage schema:about schema:mentions schema:Thing
---

### 10.1. Preamble

Part of what the graph says about a record was never said by its provider: the
GoTriple pipeline classifies, tags, detects and translates. The model's rule
for machine-produced statements is **attributability** — a consumer must
always be able to tell enrichment from provider data, and to ask how confident
the machine was.

### 10.2. The Annotation Pattern

<!-- figure: figures/annotation-pattern.svg — embed when drawn -->

Enrichment provenance is recorded with the Web Annotation vocabulary. An
`oa:Annotation` connects `oa:hasTarget` (the enriched resource) with
`oa:hasBody` (the concept or term the pipeline assigned), and qualifies
itself:

- `oa:motivatedBy` — the reason, an `oa:Motivation`: `oa:classifying` for
  discipline assignments, `oa:tagging` for keyword assignments,
  `oa:identifying` for entity linking (the Graphia AI-extracted mentions).
- `dcterms:creator` — the agent responsible: for GoTriple enrichments, the
  pipeline itself (SKG-IF `associated_with`).
- `triple:confidence` — the trust score, a decimal between 0 and 1, as
  produced by the pipeline (SKG-IF `trust`).

The assignment itself (the `sioc:topic` or `schema:about` statement) is
asserted directly on the record, where queries expect it; the annotation is
the *provenance* of that assignment, attached beside it, not in its way.

### 10.3. Detected Subjects

`schema:about` carries what the enrichment pipeline detected the resource to
be about: concepts of the TRIPLE Vocabulary (SSH-LCSH), identified by their
own `semantics.gr` IRIs — GoTriple does not mint local copies of them.
`schema:mentions` is the weaker statement: the resource *refers to* a thing
without being about it. Both have the deliberately broad range of
`schema:Thing`, because the pipeline can detect entities of any kind.
`schema:about` is distinct from both classification axes of §8: `sioc:topic`
files the record under a discipline, `dcat:theme` preserves the provider's
category — `schema:about` says what the *content* turned out to concern.

### 10.4. Language Services

Two document-level flags qualify literals produced by the language services
(§3.4): `triple:detectedLanguage` records that the resource's language was
inferred by language detection rather than declared by the provider;
`triple:machineTranslatedLanguage` names a language whose title and abstract
versions were produced by machine translation. Both are document-level by
design — the platform does not track them per field.

### 10.5. Curation Flags

`triple:isDiscarded` marks an entity (an author, a keyword) that curation has
set aside: it stays in the graph — deleting it would break provenance — but
search and filtering must not use it.

### 10.6. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 10.7. Integrity Conditions

From
[`shapes/entity.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/entity.shapes.ttl):

1. The value of `schema:about` is a `skos:Concept` identified by its own IRI —
   never a locally minted term, never a literal.
2. A concept outside the TRIPLE Vocabulary namespace
   (`semantics.gr/authorities/SSH-LCSH/`) is legal but reported: it usually
   signals a mapping error.
3. `triple:confidence` is a decimal in [0, 1].

### 10.8. Example

A discipline assignment with its provenance:

```turtle
<https://w3id.org/gto/document/example>
    sioc:topic <https://gotriple.eu/ontology/discipline/musiq> ;
    schema:about <http://semantics.gr/authorities/SSH-LCSH/example-concept> .

[] a oa:Annotation ;
    oa:hasTarget <https://w3id.org/gto/document/example> ;
    oa:hasBody <https://gotriple.eu/ontology/discipline/musiq> ;
    oa:motivatedBy oa:classifying ;
    dcterms:creator <https://www.gotriple.eu/> ;
    triple:confidence 0.87 .
```
