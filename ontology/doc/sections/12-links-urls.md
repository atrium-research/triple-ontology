---
title: Links and URLs
terms: dcterms:references dcterms:isReferencedBy schema:isBasedOn schema:sameAs schema:mainEntityOfPage schema:URL
---

### 12.1. Preamble

URLs play three roles on the platform, and the model refuses to blur them:

- **Role A — identifier.** A URL that *identifies* an aspect of a record (its
  landing page, its full text, its source record) is a reified identifier
  (§5), distinguished by one of the three URL schemes. It is data *about* the
  record, harvested and versioned like any identifier.
- **Role B — reference.** A URL that points at *another resource* — a cited
  work, a source of derivation — is a plain link property with an IRI object.
- **Role C — access.** A URL through which *data is obtained* belongs to the
  DCAT distribution pattern (§4.2): `dcat:accessURL`, `dcat:downloadURL`.

One rule holds everywhere outside the identifier reification: **a URL is an
IRI, never a literal** — a string cannot be dereferenced, an IRI can.

### 12.2. The Three URL Schemes in Practice

The schemes of §5.3 carry the role-A links: `triple:landing_page_url_schema`
(the page a human should land on), `triple:full_text_url_schema` (where the
full text is), `triple:source_url_schema` (the record at the source system).
They are reified rather than asserted as plain properties because the platform
treats them exactly like its other identifiers: harvested per source,
potentially several per document, each needing its provenance kept.

### 12.3. Links Between Works

Citations are the DCMI pair: `dcterms:references` (this work cites that one)
and its declared inverse `dcterms:isReferencedBy`. Derivation is
`schema:isBasedOn`: the resource this work is derived from or adapts — the
reuse link of the platform.

### 12.4. External Identity

`schema:sameAs` points at a reference page that unambiguously identifies the
entity — a Wikidata item, an authority page. It complements the identifier
pattern: an ORCID is an identifier *value* under a scheme, a Wikidata page is
a *place on the web* asserting identity. `schema:mainEntityOfPage` is the
inverse-flavored link from a thing to the page that primarily describes it.
`schema:URL` is Schema.org's datatype class for URL values, present in the
model wherever a property declares a URL range.

### 12.5. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 12.6. Integrity Conditions

From
[`shapes/url.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/url.shapes.ttl):

1. `schema:url`, `schema:mainEntityOfPage`, `schema:isBasedOn`,
   `dcterms:references`, `dcat:accessURL`, `dcat:downloadURL` all carry IRIs,
   never literals.
2. Role-A URLs, being identifiers, follow the identifier shape instead: the
   URL string is the `litre:hasLiteralValue` of a reified identifier — the one
   place where a URL is legitimately a literal, because there it is a *value*,
   not a link.

### 12.7. Example

The three roles on one document:

```turtle
<https://w3id.org/gto/document/example> a triple:Document ;
    # role A: the landing page, as a reified identifier
    datacite:hasIdentifier [ a datacite:Identifier ;
        datacite:usesIdentifierScheme triple:landing_page_url_schema ;
        litre:hasLiteralValue "https://books.openedition.org/pur/1234" ] ;
    # role B: a citation and a derivation
    dcterms:references <https://w3id.org/gto/document/other> ;
    schema:isBasedOn <https://w3id.org/gto/dataset/example> .
```
