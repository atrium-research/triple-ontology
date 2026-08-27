---
title: Original Values
terms: originalInLanguage originalAdditionalType originalConditionOfAccess originalLicense originalDatePublished originalSource dc:language dc:type dc:rights dc:date dc:source dcterms:source dcterms:provenance dcterms:ProvenanceStatement
---

### 9.1. Preamble

GoTriple normalizes what it harvests: a provider's free-text `"artículo"`
becomes `ct:typ_article`, a `"Frei zugänglich"` becomes
`coa:acr_open-access`. Normalization is what makes the corpus searchable — and
it is lossy by nature. The original-values family exists so that **nothing the
provider said is lost**: beside every normalized statement, the raw value
survives, verbatim, as a plain literal.

The naming is a rule, not a list: *original* + the normalized field name.
`schema:inLanguage` has `triple:originalInLanguage`, the platform's
`additionalType` field has `triple:originalAdditionalType`,
`triple:hasConditionOfAccess` has `triple:originalConditionOfAccess`, and so on
— a reader who knows the normalized property can derive the original one.

### 9.2. The Six Original Properties

<!-- figure: figures/original-values.svg — embed when drawn -->

| original property | shadows | DC super-property |
|---|---|---|
| `triple:originalInLanguage` | `schema:inLanguage` | `dc:language` |
| `triple:originalAdditionalType` | the content type (§8) | `dc:type` |
| `triple:originalConditionOfAccess` | `triple:hasConditionOfAccess` | `dc:rights` |
| `triple:originalLicense` | `triple:hasLicense` | `dc:rights` |
| `triple:originalDatePublished` | `schema:datePublished` | `dc:date` |
| `triple:originalSource` | the provenance chain (§3.3) | `dc:source` |

Every original property is a sub-property of the corresponding **Dublin Core
Elements** term (`dc:`, the 1.1 namespace) — and the choice of the legacy
namespace is deliberate. DCMI itself keeps the Elements set for exactly this
use: uninterpreted, free-range literal metadata. The raw string a provider
shipped is precisely that, so `dc:language`, `dc:type`, `dc:rights`,
`dc:date`, `dc:source` describe it honestly — while the *normalized*
statements live under the typed `dcterms:` hierarchy (§8.3). The two-namespace
split mirrors the raw/normalized split of the data itself.

### 9.3. Provenance

Two DCMI terms complete the picture on the provenance side. `dcterms:source`
points at the system the record was harvested from — the typed counterpart of
the free-text `triple:originalSource`. `dcterms:provenance` attaches a
`dcterms:ProvenanceStatement`: a statement of changes in custody of the record
that matter for its authenticity and interpretation.

### 9.4. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 9.5. Integrity Conditions

The original properties are deliberately unconstrained: they accept whatever
the provider shipped, as `xsd:string` literals — a value that would violate a
shape would defeat their purpose. The only rule is directional: an original
property never carries a normalized value, and a normalized property never
carries a raw one.

### 9.6. Example

A record whose provider declared its metadata in German:

```turtle
<https://w3id.org/gto/document/example> a triple:Document ;
    schema:inLanguage [ a schema:Language ; schema:name "de" ] ;
    triple:originalInLanguage "Deutsch" ;
    triple:hasConditionOfAccess <https://gotriple.eu/ontology/condition-of-access/acr_open-access> ;
    triple:originalConditionOfAccess "Frei zugänglich" ;
    schema:datePublished "2005-01-01"^^xsd:date ;
    triple:originalDatePublished "Januar 2005" .
```
