# Motivating Scenario (Iteration 8)

## Name
Document Identifier Types Extension

## Description

### General description

Scholarly documents in the GoTriple platform are identified through various standardized identifier schemes, each serving specific purposes within the academic publishing ecosystem. While the ontology already supports the concept of document identifiers (established in Iteration 01), there is a need to explicitly specify and support the most common identifier types used in academic publishing.

The four primary identifier types being implemented are:

1. **DOI (Digital Object Identifier)**: A persistent identifier widely used for journal articles, conference papers, datasets, and other digital objects. DOIs provide a permanent link to the resource location and are maintained by the International DOI Foundation. Implemented as the `datacite:doi` identifier scheme.

2. **ISSN (International Standard Serial Number)**: An eight-digit identifier used to uniquely identify serial publications such as journals, magazines, and periodicals. ISSN helps distinguish between different serial publications and their various formats (print, electronic, etc.). Implemented as the `datacite:issn` identifier scheme.

3. **ISBN (International Standard Book Number)**: A numeric commercial book identifier assigned to books and book-like products. ISBNs are used by publishers, booksellers, libraries, and internet retailers for ordering and inventory management. Implemented as the `datacite:isbn` identifier scheme.

4. **Handle**: A persistent identifier system that provides a comprehensive infrastructure for managing digital objects. Handles are often used in institutional repositories and can resolve to the current location of a resource. Implemented as the `datacite:handle` identifier scheme.

By explicitly modeling these identifier schemes in the ontology, GoTriple can:
- Better categorize and validate document identifiers
- Facilitate interoperability with external scholarly systems
- Enable more precise querying based on identifier types
- Support proper citation and reference management

### Technical specification

Academic identifiers follow the DataCite pattern established in iteration 01: every identifier is a `datacite:Identifier` node carrying exactly one `datacite:usesIdentifierScheme` and exactly one `litre:hasLiteralValue`. The **scheme is what tells one kind of identifier from another** — there are no identifier subclasses in the ontology.

The four academic identifier schemes used in this iteration:

1. **DOI** — scheme `datacite:doi`. Digital Object Identifier, maintained by the International DOI Foundation. Value in the form `10.NNNN/suffix`, without the `https://doi.org/` resolver prefix.
2. **ISSN** — scheme `datacite:issn`. Eight-digit identifier of a serial publication.
3. **ISBN** — scheme `datacite:isbn`. Numeric identifier of a book or book-like product.
4. **Handle** — scheme `datacite:handle`. Persistent identifier from the Handle System, common in institutional repositories.

All four are declared as `owl:NamedIndividual` of `datacite:IdentifierScheme`, reused from the DataCite ontology rather than minted here. Adding a further identifier kind means declaring one more scheme individual — never a class.

The scheme is **always asserted explicitly in the data**: nothing is inferred. Documents are connected to their identifiers with `datacite:hasIdentifier`.

Which identifiers a document must carry — exactly one internal id, exactly one ARK PID, at least one original identifier — is expressed in `shapes/entity.shapes.ttl`, not as OWL axioms: OWL restrictions describe inferences rather than constraints, so a missing identifier would be inferred to exist instead of being reported.

## Example 1

`document_1` has identifier `identifier_1` which is a DOI. `identifier_1` uses the `datacite:doi` identifier scheme and has the literal value "10.1234/example.2024.001".

## Example 2

`document_45` has two identifiers:
- `identifier_23` which is an ISSN with value "1234-5678" (uses `datacite:issn`)
- `identifier_24` which is a DOI with value "10.5678/journal.2024.045" (uses `datacite:doi`)

## Example 3

`document_78` has identifier `identifier_90` which is a Handle with value "11234/5678-abcd-efgh" (uses `datacite:handle`).

## Example 4

`document_99` has identifier `identifier_110` which is an ISBN with value "978-3-16-148410-0" (uses `datacite:isbn`).
