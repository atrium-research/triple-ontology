---
title: The TRIPLE Data Model
terms:
---

### 2.1. Entities at a Glance

The model describes six kinds of platform entity. Four are **resources**
harvested from the providers; two are **first-class citizens of the platform**
built around them.

| Entity | Class | Described in |
|---|---|---|
| A scholarly document | `triple:Document` | §3 |
| A research dataset | `triple:Dataset` | §4 |
| An audio/video/image object | `triple:MediaObject` | §4 |
| A semantic artefact (ontology, vocabulary, …) | `triple:SemanticArtefact` | §4 |
| A research project | `triple:Project` | §7 |
| A researcher profile | `triple:Profile` | §6 |

Around them, a small cast of supporting nodes: **identifiers** (§5) reify every
external key a record carries; **grants and funding schemes** (§7) attach money
to projects; **annotations** (§10) carry what the enrichment pipeline detected;
the **bridge classes** (§8) type the concepts of the six controlled vocabularies.

### 2.2. Design Rationale

Five decisions shape everything else:

1. **Reuse first.** The backbone is Schema.org; FOAF names the agents; DataCite
   models the identifiers; DCAT the dataset distribution; OA the annotations.
   Terms of our own exist only where nothing external says the right thing —
   nineteen properties and eleven classes at the time of writing.
2. **A flat term space.** Every class and property lives directly under
   `…/ontology/triple/`; documentation chapters are an overlay and never appear
   in an IRI. The six vocabularies are siblings, not children, of the model.
3. **Identifiers are nodes, not strings.** Every external key — DOI, ORCID,
   internal id, landing-page URL — is a `datacite:Identifier` with a scheme and
   a literal value. There are no identifier subclasses: the scheme *is* the kind.
4. **A URL is handled by the role it plays** (§12): identifier of the record
   (reified), reference to another resource (IRI object), or access point
   (IRI object). Never a bare literal.
5. **Deduplication is one directed link** (§11): a duplicate points at its
   representative with `triple:isDuplicateOf`; there is no cluster node, and the
   cluster fields of the platform API are all derivable.

### 2.3. A Record at a Glance

A minimal document record, showing the pattern the chapters below unfold:

```turtle
@prefix triple:   <https://gotriple.eu/ontology/triple/> .
@prefix schema:   <https://schema.org/> .
@prefix datacite: <http://purl.org/spar/datacite/> .
@prefix litre:    <http://www.essepuntato.it/2010/06/literalreification/> .
@prefix disc:     <https://gotriple.eu/ontology/discipline/> .
@prefix ct:       <https://gotriple.eu/ontology/content-type/> .
@prefix coa:      <https://gotriple.eu/ontology/condition-of-access/> .
@prefix sioc:     <http://rdfs.org/sioc/ns#> .

<https://w3id.org/gto/document/example> a triple:Document ;
    schema:headline "Digital humanities and the archive"@en ;
    schema:author <https://w3id.org/gto/profile/example-author> ;
    schema:datePublished "2023-05-01"^^xsd:date ;
    datacite:hasIdentifier [
        a datacite:Identifier ;
        datacite:usesIdentifierScheme triple:internal_id_schema ;
        litre:hasLiteralValue "ftexample:oai:repo:12345" ] ;
    sioc:topic disc:hist ;
    triple:hasContentType ct:typ_article ;
    triple:hasConditionOfAccess coa:acr_open-access .
```

Everything in this snippet is defined in the chapters that follow: the document
core in §3, the identifier node in §5, the vocabulary links in §8.
