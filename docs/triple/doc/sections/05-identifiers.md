---
title: Identifiers
terms: datacite:Identifier datacite:IdentifierScheme datacite:hasIdentifier datacite:usesIdentifierScheme litre:hasLiteralValue datacite:ark datacite:doi datacite:handle datacite:isbn datacite:isni datacite:issn datacite:orcid datacite:researcherid datacite:uri internal_id_schema original_id_schema gotriple_id_schema idref_schema landing_page_url_schema full_text_url_schema source_url_schema
---

### 5.1. Preamble

One design decision governs this whole chapter: **there are no identifier
subclasses**. Every identifier on the platform is a plain
`datacite:Identifier`, and what *kind* of identifier it is — a DOI, an ORCID,
the internal id — is said by exactly one thing: its scheme. Adding a new kind
of identifier to the model means adding one scheme individual, never a class.

It was not always so: until release 3.0.0 the model carried a class per kind
(`triple:ID`, `triple:PID`, `triple:OriginalIdentifier`, `triple:DOI`, …),
classes that existed only to be nameable inside OWL cardinality axioms. They
were retired together: the schemes already made the distinction, and the
cardinalities moved to SHACL (§5.4), where they are checkable.

### 5.2. The Identifier Pattern

An identifier is a node of its own, never a bare string dangling from a
property. The entity points at it with `datacite:hasIdentifier`; the node is a
`datacite:Identifier` carrying exactly two things:

- `datacite:usesIdentifierScheme` — the scheme, an individual of
  `datacite:IdentifierScheme`. This is the discriminator: it is the only thing
  that tells one kind of identifier from another.
- `litre:hasLiteralValue` — the value, an `xsd:string` in canonical form,
  without a resolver prefix (`"10.4000/dh.1234"`, not
  `"https://doi.org/10.4000/dh.1234"`).

<!-- figure: figures/identifier-pattern.svg — embed when drawn -->

The value carrier deserves a note: it comes from the Literal Reification
vocabulary (`litre:`), *not* from DataCite — `datacite:hasIdentifierValue`,
which one might expect, does not exist in the DataCite ontology. The DataCite
ontology itself pairs `datacite:Identifier` with literal reification, and the
model follows it.

### 5.3. The Sixteen Schemes

Nine schemes are reused from the DataCite ontology, for the identifiers the
scholarly world already names: `datacite:doi`, `datacite:handle`,
`datacite:isbn`, `datacite:issn`, `datacite:ark`, `datacite:uri` for resources;
`datacite:orcid`, `datacite:isni`, `datacite:researcherid` for agents.

Seven schemes are minted by TRIPLE, for the identifiers only GoTriple can name:

- `triple:internal_id_schema` — the platform's internal identifier; every
  entity has exactly one.
- `triple:original_id_schema` — the identifier the record carried in the
  system it was harvested from; a document may have several, one per source.
- `triple:gotriple_id_schema` — the public GoTriple identifier of a profile.
- `triple:idref_schema` — IdRef, the French authority identifier for authors.
- `triple:landing_page_url_schema`, `triple:full_text_url_schema`,
  `triple:source_url_schema` — the three URL roles, discussed in §12: when a
  URL identifies a document's page, its full text or its source record, it is
  reified like any other identifier, distinguished by these schemes.

The platform's persistent identifier is an **ARK**: `datacite:ark` marks the
PID GoTriple mints for every entity (cf. FAIR principle F1).

### 5.4. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 5.5. Integrity Conditions

From
[`shapes/identifier.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/identifier.shapes.ttl)
and
[`shapes/entity.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/entity.shapes.ttl):

1. Every `datacite:Identifier` carries **exactly one scheme and exactly one
   value** — the two axioms of the pattern, stated as checkable shapes.
2. The five content classes (Document, Dataset, MediaObject, SemanticArtefact,
   Project) carry exactly one internal id, exactly one ARK, and at least one
   original identifier.
3. A Profile carries exactly one internal id and exactly one ARK — no original
   identifier: a registered user is born inside GoTriple.
4. The schemes *expected* on a document form a known list (internal, ARK,
   original, DOI, Handle, ISSN, ISBN, the three URL roles). The list is not
   closed: an unlisted scheme is legal but reported, because it usually
   signals a mapping error.

### 5.6. Example

The same document, identified three ways:

```turtle
<https://w3id.org/gto/document/example> a triple:Document ;
    datacite:hasIdentifier
        [ a datacite:Identifier ;
          datacite:usesIdentifierScheme triple:internal_id_schema ;
          litre:hasLiteralValue "ftopenedition:oai:books:1234" ] ,
        [ a datacite:Identifier ;
          datacite:usesIdentifierScheme datacite:ark ;
          litre:hasLiteralValue "ark:/12345/gt78901" ] ,
        [ a datacite:Identifier ;
          datacite:usesIdentifierScheme datacite:doi ;
          litre:hasLiteralValue "10.4000/books.1234" ] .
```
