---
title: External Alignments
terms: skos:exactMatch skos:closeMatch foaf:Document crm:E31_Document crm:E7_Activity crm:E90_Symbolic_Object fabio:Work fabio:ScholarlyWork fabio:Dataset sshoc:SHE1_Dataset sshoc:SHE3_SSH_Project sshoc:SHE8_Publication
---

### 13.1. Preamble

The model reuses external terms everywhere, and it does so under one policy:
**no `owl:imports`**. Every borrowed term is materialized in the ontology
itself — declared with its type, labelled with its prefixed name
(`schema:headline`, `foaf:name`), and documented *contextually*: the comment
says how GoTriple uses the term, while the authoritative definition stays with
the source ontology, reachable through the term's own IRI. A consumer loads
one self-contained graph; no availability of a third-party server decides
whether the model is complete.

The same policy constrains what the model may *say* about a borrowed term:
local axioms only. No global `rdfs:domain`, `rdfs:range` or subsumption is
ever asserted on somebody else's term — a value constraint that GoTriple needs
is stated per class (`owl:allValuesFrom`) or in the SHACL profile, where it
checks instead of inferring.

### 13.2. The Mapping Properties

Alignments are stated with the two SKOS mapping properties, chosen by
strength. `skos:exactMatch` asserts interchangeability — used when the
external notion *is* the TRIPLE notion (a vocabulary concept and its COAR
counterpart; `triple:Document` and `crm:E31_Document`). `skos:closeMatch`
asserts similarity without identity — used when the external notion carries
commitments the TRIPLE data cannot support (§3.2). `owl:equivalentClass` is
used sparingly and deliberately: an equivalence is a two-way inference
license, and most reuse is one-way.

### 13.3. The Alignment Classes, Ontology by Ontology

**FOAF.** `triple:Document` is a subclass of `foaf:Document` — the plain,
commitment-free notion of a document, safe as a structural superclass.

**CIDOC CRM.** The one `skos:exactMatch` on the document class:
`crm:E31_Document` — a document *about* something, which is exactly what a
metadata record is (§3.2). `crm:E7_Activity` aligns `triple:Project` (a
project is an intentional activity), `crm:E90_Symbolic_Object` aligns
`triple:SemanticArtefact` (a formal representation is a symbolic object). The
CRM investigation is ongoing; deeper event-based modeling remains open.

**FaBiO.** FRBR-based, hence aligned with deliberate weakness (§3.2):
`triple:Document` is a `skos:closeMatch` of `fabio:ScholarlyWork` (with
`fabio:Work` above it), `triple:Dataset` of `fabio:Dataset`. Exact alignments
would inherit FaBiO's FRBR-level placement, which harvested records cannot
support.

**SSHOC Reference Ontology.** The domain siblings: `sshoc:SHE8_Publication`
for documents, `sshoc:SHE1_Dataset` for datasets, `sshoc:SHE3_SSH_Project`
for projects — all `skos:closeMatch`, connecting GoTriple to the SSH Open
Cluster's own model.

The vocabularies carry their own alignment layer with the same two properties:
COAR (content types, access conditions), Creative Commons and SPDX (licenses),
UNESCO and LCSH (disciplines), Dewey (the DDC proxies).

### 13.4. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 13.5. Notes

Alignment asserts no data constraints, so this chapter has no integrity
conditions and no exemplar snippet: its statements are the
`skos:exactMatch`/`skos:closeMatch` triples visible on each aligned term's
entry, and every external reference in an entry's External Alignment box links
out to the authority that defines it.
