# Motivating Scenario (Iteration 10)

## Name
Document Identifier Types Extension

## Description

### General description

Scholarly documents in the GoTriple platform are identified through various standardized identifier schemes, each serving specific purposes within the academic publishing ecosystem. While the ontology already supports the concept of document identifiers (established in Iteration 01), there is a need to explicitly specify and support the most common identifier types used in academic publishing.

The four primary identifier schemes being formalized are:

1. **DOI (Digital Object Identifier)**: A persistent identifier widely used for journal articles, conference papers, datasets, and other digital objects. DOIs provide a permanent link to the resource location and are maintained by the International DOI Foundation.

2. **ISSN (International Standard Serial Number)**: An eight-digit identifier used to uniquely identify serial publications such as journals, magazines, and periodicals. ISSN helps distinguish between different serial publications and their various formats (print, electronic, etc.).

3. **ISBN (International Standard Book Number)**: A numeric commercial book identifier assigned to books and book-like products. ISBNs are used by publishers, booksellers, libraries, and internet retailers for ordering and inventory management.

4. **Handle**: A persistent identifier system that provides a comprehensive infrastructure for managing digital objects. Handles are often used in institutional repositories and can resolve to the current location of a resource.

By explicitly modeling these identifier schemes in the ontology, GoTriple can:
- Better categorize and validate document identifiers
- Facilitate interoperability with external scholarly systems
- Enable more precise querying based on identifier types
- Support proper citation and reference management

### Technical specification

The identifier types will be modeled as instances of `datacite:IdentifierScheme`, following the DataCite ontology pattern established in earlier iterations. Each identifier scheme will be connected to document identifiers through the `datacite:usesIdentifierScheme` property.

The four identifier schemes being added:

1. **DOI Scheme**
   - **Identifier**: `triple:doi`
   - **Type**: `datacite:IdentifierScheme`
   - **Label**: "DOI"@en
   - **Usage**: Connected to DOI identifiers via `datacite:usesIdentifierScheme`

2. **ISSN Scheme**
   - **Identifier**: `triple:issn`
   - **Type**: `datacite:IdentifierScheme`
   - **Label**: "ISSN"@en
   - **Usage**: Connected to ISSN identifiers via `datacite:usesIdentifierScheme`

3. **ISBN Scheme**
   - **Identifier**: `triple:isbn`
   - **Type**: `datacite:IdentifierScheme`
   - **Label**: "ISBN"@en
   - **Usage**: Connected to ISBN identifiers via `datacite:usesIdentifierScheme`

4. **Handle Scheme**
   - **Identifier**: `triple:handle`
   - **Type**: `datacite:IdentifierScheme`
   - **Label**: "Handle"@en
   - **Usage**: Connected to Handle identifiers via `datacite:usesIdentifierScheme`

Each document can have multiple identifiers of different types, and each identifier is linked to its scheme through the `datacite:usesIdentifierScheme` property. Documents are connected to their identifiers using the `datacite:hasIdentifier` property (note: corrected spelling from earlier iterations' "hasIdentifer").

## Example 1

`document_1` has identifier `identifier_1` which is a DOI. `identifier_1` uses the `triple:doi` identifier scheme and has the literal value "10.1234/example.2024.001".

## Example 2

`document_45` has two identifiers:
- `identifier_23` which is an ISSN with value "1234-5678" (uses `triple:issn`)
- `identifier_24` which is a DOI with value "10.5678/journal.2024.045" (uses `triple:doi`)

## Example 3

`document_78` has identifier `identifier_90` which is a Handle with value "11234/5678-abcd-efgh" (uses `triple:handle`).

## Example 4

`document_99` has identifier `identifier_110` which is an ISBN with value "978-3-16-148410-0" (uses `triple:isbn`).
