---
title: Documents
terms: Document schema:CreativeWork schema:headline schema:abstract schema:datePublished schema:author schema:creator schema:contributor schema:publisher schema:provider aggregator schema:keywords schema:DefinedTerm schema:creativeWorkStatus schema:comment schema:dateCreated schema:dateModified schema:inLanguage schema:Language schema:spatialCoverage schema:temporalCoverage schema:Place
---

### 3.1. Preamble

A `triple:Document` is the platform's **record of a scholarly resource** — an
article, a book, a chapter, a report — harvested from one of GoTriple's source
systems. The class deliberately models the *record*, not the abstract work: two
providers describing the same publication yield two documents, and their
relationship is stated explicitly by the deduplication link (§11), never by
merging the records.

The descriptive core is pure Schema.org: title (`schema:headline`), abstract,
publication date, authors (`schema:author`, whose super-property
`schema:creator` keeps generic CreativeWork queries working), publisher. Three
agent roles that are easily conflated are kept apart:

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

### 3.2. Record, not Manifestation

In FRBR terms a GoTriple document is *not* a manifestation — and not an
expression or a work either. FRBR distinguishes the *work* (the intellectual
creation: "the article" as an idea), its *expressions* (each realization of it:
the preprint, the accepted manuscript, the version of record, a translation),
the *manifestations* that embody an expression (the publisher's typeset PDF,
the HTML rendering, the repository copy of the accepted manuscript), and the
*items* — single exemplars, meaningful for physical carriers and degenerate for
digital ones.

An aggregated record sits on no fixed rung of that ladder, because every
provider describes at its own granularity. A repository deposit bundles
expression-level facts (which version was deposited) with manifestation-level
ones (the file and its format); a journal record describes the version of
record — an expression — yet identifies it with manifestation-cut identifiers
(an ISBN names one embodiment; a DOI is usually minted per version of record,
sometimes per format); a bibliographic source may describe at work level with
no file in sight. Even a single field changes level from record to record:
`schema:datePublished` is a manifestation fact in the publisher's record and an
expression fact on a preprint server.

The model therefore refuses the choice: `triple:Document` models the *record*
the provider actually shipped, and commits to no FRBR level. The refusal is
visible in the alignments (§13). The one `skos:exactMatch` is
`crm:E31_Document` — CIDOC's document *about* something, which is precisely
what a metadata record is. FaBiO, which is FRBR-based, is aligned only with
`skos:closeMatch` (`fabio:ScholarlyWork`): an exact alignment would inherit
FaBiO's Work-level placement and assert exactly the distinction the harvested
data cannot support.

The consequence surfaces in deduplication (§11): `triple:isDuplicateOf` states
that two records describe the same resource *for discovery*, not that they are
FRBR-identical. Linked records may straddle rungs — the preprint deposit and
the version of record are different expressions, the publisher's page and the
repository copy of the same version different manifestations — and the platform
links them all the same, because a user asking for "the paper" wants one
answer. Nothing is merged away in the process: each record keeps its
identifiers (§5) and its original values (§9), which is where the
level-bearing evidence (version statements, formats, ISBNs) survives for any
consumer who does want to reconstruct a Work–Expression–Manifestation stack on
top of the graph.

### 3.3. The Life of a Record

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

Two timestamps frame the record itself, as opposed to the resource it
describes: `schema:dateCreated` is when the record entered the platform,
`schema:dateModified` its last update. `schema:datePublished` belongs to the
resource — the publication date the provider declared.

### 3.4. Titles, Abstracts and Languages

`schema:headline` and `schema:abstract` are language-tagged literals, and a
document may carry one per language: the original title next to its
translations. Two document-level flags qualify them: `triple:detectedLanguage`
records that the language was inferred rather than declared, and
`triple:machineTranslatedLanguage` that a translation was produced by machine
(§10) — both are deliberately document-level, since the platform does not track
them per field. The language of the *content* is stated with `schema:inLanguage`, whose value
is a `schema:Language` instance — never a bare string; what the provider
originally declared survives in `triple:originalInLanguage` (§9).

### 3.5. Coverage

What the content is *about* in space and time is stated with two CreativeWork
properties: `schema:spatialCoverage`, whose value is a `schema:Place` (an
instance, possibly just named), and `schema:temporalCoverage`, a literal
following the Schema.org conventions (a year, an ISO 8601 interval such as
`"2019/2020"`). Coverage is a document-level facility — any record may carry
it; datasets add the DCAT-specific bounding box on top of it (§4).

### 3.6. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 3.7. Integrity Conditions

Stated as SHACL in
[`shapes/entity.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/entity.shapes.ttl);
the salient ones:

1. Every document carries the two platform identifiers — internal id and ARK —
   and any number of external ones (§5).
2. The identifier schemes expected on a document form a known list (internal,
   ARK, original, DOI, Handle, ISSN, ISBN, and the three URL roles); a scheme
   outside it is legal but usually signals a mapping error.
3. Titles and abstracts are language-tagged literals; the same document may
   carry one per language (machine translations are flagged, see §10).

### 3.8. Example

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

### 3.9. Notes

**Why headline and not name.** Schema.org offers both; the model reserves
`schema:name` for things (projects, places, defined terms) and uses
`schema:headline` for the title of creative works, mirroring the platform's own
`headline` field. Agents are named with `foaf:name` (§6).
