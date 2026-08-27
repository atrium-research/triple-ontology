---
title: Classification and Controlled Vocabularies
terms: Discipline ContentType ConditionOfAccess License ProjectType hasContentType hasConditionOfAccess hasLicense hasProjectType sioc:topic dcterms:type dcterms:subject dcterms:accessRights dcterms:license dcterms:RightsStatement dcterms:LicenseDocument skos:Concept skos:prefLabel skos:definition
---

### 8.1. Preamble

Classification is a two-level design. The **vocabularies** — Discipline,
ContentType, ConditionOfAccess, License, ProjectType, plus the DDC proxies —
are published as sibling artefacts beside the model, each under its own
namespace (`https://gotriple.eu/ontology/discipline/`, …), each a SKOS concept
scheme. The **model** carries one bridge class per vocabulary and one property
to reach it. This chapter is about the bridge; the vocabularies' own pages
document the concepts.

One rule connects the platform to the graph: a concept's local name is the
**production key, verbatim** (`disc:musiq`, `ct:typ_article`,
`coa:acr_open-access`). Mapping a GoTriple record to a vocabulary concept is
namespace + key — no lookup table exists, by construction.

### 8.2. The Bridge Classes

<!-- figure: figures/classification-two-level.svg — embed when drawn -->

Each vocabulary has a class in the model naming its kind of concept:
`triple:Discipline`, `triple:ContentType`, `triple:ConditionOfAccess`,
`triple:License`, `triple:ProjectType`. All five are subclasses of
`skos:Concept` — a vocabulary term *is* a SKOS concept — and, where DCMI has
the corresponding notion, of its DCMI class too: `triple:ConditionOfAccess` ⊑
`dcterms:RightsStatement`, `triple:License` ⊑ `dcterms:LicenseDocument`. The
bridge classes let the model constrain a property's values ("the object of
`triple:hasLicense` is a `triple:License`") without importing the vocabulary.

### 8.3. The Linking Properties

Five properties attach a resource to the vocabularies, and each is declared a
sub-property of the generic DCMI notion it specializes:

| property | vocabulary | DCMI super-property |
|---|---|---|
| `triple:hasContentType` | ContentType | `dcterms:type` |
| `triple:hasConditionOfAccess` | ConditionOfAccess | `dcterms:accessRights` |
| `triple:hasLicense` | License | `dcterms:license` |
| `triple:hasProjectType` | ProjectType | `dcterms:type` |
| `sioc:topic` | Discipline | `dcterms:subject` |

The hierarchy is what makes generic queries work: a consumer who knows nothing
of TRIPLE can ask for `dcterms:subject` or `dcterms:type` and, under RDFS
entailment, receive the specialized statements. The discipline property is
`sioc:topic` — reused, not minted, because SIOC already says "the topic a
resource is filed under" (the GoTriple SSH taxonomy of 27 disciplines);
`dcat:theme`, also under `dcterms:subject`, stays distinct for the *provider's*
categories (§4.2).

### 8.4. The SKOS Layer

Inside the vocabularies every concept follows the same pattern:
`skos:prefLabel` for the display name (multilingual where the platform is),
`skos:definition` for the meaning, `skos:inScheme` for membership, and
`skos:exactMatch`/`skos:closeMatch` (§13) toward the external KOS each
vocabulary is aligned with — COAR for content types and access conditions,
Creative Commons and SPDX for licenses, UNESCO and LCSH for disciplines.

### 8.5. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 8.6. Integrity Conditions

From
[`shapes/entity.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/entity.shapes.ttl):

1. The value of `sioc:topic` should be a `triple:Discipline` of the GoTriple
   classification (warning severity: the platform tolerates, but reports).
2. The class restrictions on the `has*` properties are `owl:allValuesFrom`,
   asserted per class; the *checks* live in SHACL, because an allValuesFrom is
   an inference rule, not a validator — it would silently type a wrong value
   instead of reporting it.

### 8.7. Example

One document, classified along every axis:

```turtle
<https://w3id.org/gto/document/example> a triple:Document ;
    sioc:topic <https://gotriple.eu/ontology/discipline/musiq> ;
    triple:hasContentType <https://gotriple.eu/ontology/content-type/typ_book> ;
    triple:hasConditionOfAccess <https://gotriple.eu/ontology/condition-of-access/acr_open-access> ;
    triple:hasLicense <https://gotriple.eu/ontology/license/lic_creative-commons> .
```
