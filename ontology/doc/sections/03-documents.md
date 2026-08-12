---
title: Documents
terms: Document schema:CreativeWork schema:headline schema:abstract schema:datePublished schema:author schema:contributor schema:publisher schema:provider aggregator schema:keywords schema:DefinedTerm schema:creativeWorkStatus schema:comment
---

### 3.1. Preamble

A `triple:Document` is the platform's **record of a scholarly resource** — an
article, a book, a chapter, a report — harvested from one of GoTriple's source
systems. The class deliberately models the *record*, not the abstract work: two
providers describing the same publication yield two documents, and their
relationship is stated explicitly by the deduplication link (§11), never by
merging the records.

The descriptive core is pure Schema.org: title (`schema:headline`), abstract,
publication date, authors, publisher. Three agent roles that are easily
conflated are kept apart:

- `schema:publisher` — who published the *resource* (the journal, the press);
- `schema:provider` — the source system GoTriple harvested the record from
  (HAL, OpenEdition, …);
- `triple:aggregator` — the intermediary aggregator the record travelled
  through (BASE, Isidore), when there is one. This is the one term of this
  chapter minted by TRIPLE: no external property distinguishes the aggregator
  from the provider, and provenance queries need the distinction.

What a document is *about* is not in this chapter: disciplines, thesaurus
concepts and free keywords are three different things, and only the free
keywords (`schema:keywords`, typed `schema:DefinedTerm` because the producer's
tags carry no URI) belong to the descriptive core. Classification against the
controlled vocabularies is the subject of §8.

### 3.2. The Life of a Record

A document reaches the graph through a pipeline, and the model keeps every stage
visible rather than overwriting it:

1. **Harvest.** The record is collected from its `schema:provider` (HAL,
   OpenEdition, …), possibly through an intermediary `triple:aggregator`
   (BASE, Isidore). The identifier it carried at the source survives as a
   reified identifier with `triple:original_id_schema` (§5).
2. **Normalization.** Free-text values from the provider — type, language,
   licence, access statement, source, publication date — are normalized against
   the controlled vocabularies, and the *raw* values are preserved side by side
   in the `original*` property family (§9). Nothing is lost in translation: a
   consumer can always ask what the provider actually said.
3. **Enrichment.** The platform classifies the record against the SSH
   disciplines (`sioc:topic`), detects thesaurus concepts (`schema:about`) and
   named entities (§10), each detection carrying its confidence.
4. **Deduplication.** When several providers describe the same publication,
   one record is elected representative and the others point at it with
   `triple:isDuplicateOf` (§11). The records stay distinct: deduplication is a
   statement, not a merge.

### 3.3. Titles, Abstracts and Languages

`schema:headline` and `schema:abstract` are language-tagged literals, and a
document may carry one per language: the original title next to its
translations. Two document-level flags qualify them: `triple:detectedLanguage`
records that the language was inferred rather than declared, and
`triple:machineTranslatedLanguage` that a translation was produced by machine
(§10) — both are deliberately document-level, since the platform does not track
them per field. The language of the *content* is stated with `schema:inLanguage`;
what the provider originally declared survives in `triple:originalInLanguage`
(§9).

### 3.4. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 3.5. Integrity Conditions

Stated as SHACL in `shapes/entity.shapes.ttl`; the salient ones:

1. Every document carries the two platform identifiers — internal id and ARK —
   and any number of external ones (§5).
2. The identifier schemes expected on a document form a known list (internal,
   ARK, original, DOI, Handle, ISSN, ISBN, and the three URL roles); a scheme
   outside it is legal but usually signals a mapping error.
3. Titles and abstracts are language-tagged literals; the same document may
   carry one per language (machine translations are flagged, see §10).

### 3.6. Example

The TRIPLE record of a HAL article, descriptive core only:

```turtle
<https://w3id.org/gto/document/example> a triple:Document ;
    schema:headline "De l'esthétique au présent"@fr ;
    schema:abstract "Cet ouvrage examine…"@fr ;
    schema:datePublished "1998-01-01"^^xsd:date ;
    schema:author <https://w3id.org/gto/profile/example-author> ;
    schema:publisher [ a foaf:Organization ; foaf:name "De Boeck Supérieur"@fr ] ;
    schema:provider [ a foaf:Organization ; foaf:name "OpenEdition"@en ] ;
    triple:aggregator [ a foaf:Organization ; foaf:name "Isidore"@en ] ;
    schema:keywords [ a schema:DefinedTerm ; schema:name "aesthetics"@en ] .
```

### 3.7. Notes

**Record, not manifestation.** In FRBR terms a GoTriple document is *not* a
manifestation: providers describe at mixed granularities, and the platform does
not attempt to stack them into a Work–Expression–Manifestation hierarchy. The
only identity the model commits to is `crm:E31_Document` (§13) — a document
*about* something, which is exactly what a metadata record is.

**Why headline and not name.** Schema.org offers both; the model reserves
`schema:name` for things (projects, places, defined terms) and uses
`schema:headline` for the title of creative works, mirroring the platform's own
`headline` field. Agents are named with `foaf:name` (§6).
