# Motivating Scenario (Iteration 8)

## Name
Document Identifier Types Extension

## Description

### General description

Scholarly documents in the GoTriple platform are identified through various standardized identifier schemes, each serving specific purposes within the academic publishing ecosystem. While the ontology already supports the concept of document identifiers (established in Iteration 01), there is a need to explicitly specify and support the most common identifier types used in academic publishing.

The four primary identifier types being implemented are:

1. **DOI (Digital Object Identifier)**: A persistent identifier widely used for journal articles, conference papers, datasets, and other digital objects. DOIs provide a permanent link to the resource location and are maintained by the International DOI Foundation. Implemented as `triple:DOI` class.

2. **ISSN (International Standard Serial Number)**: An eight-digit identifier used to uniquely identify serial publications such as journals, magazines, and periodicals. ISSN helps distinguish between different serial publications and their various formats (print, electronic, etc.). Implemented as `triple:ISSN` class.

3. **ISBN (International Standard Book Number)**: A numeric commercial book identifier assigned to books and book-like products. ISBNs are used by publishers, booksellers, libraries, and internet retailers for ordering and inventory management. Implemented as `triple:ISBN` class.

4. **Handle**: A persistent identifier system that provides a comprehensive infrastructure for managing digital objects. Handles are often used in institutional repositories and can resolve to the current location of a resource. Implemented as `triple:Handle` class.

By explicitly modeling these identifier schemes in the ontology, GoTriple can:
- Better categorize and validate document identifiers
- Facilitate interoperability with external scholarly systems
- Enable more precise querying based on identifier types
- Support proper citation and reference management

### Technical specification

The identifier types are implemented through a class-based approach, extending the DataCite ontology pattern established in earlier iterations. Each identifier type is modeled as a distinct class that inherits from `datacite:Identifier`, with automatic schema association through OWL restrictions.

The four academic identifier classes being implemented:

1. **DOI Class**
   - **Class**: `triple:DOI`
   - **Inherits from**: `datacite:Identifier`
   - **Automatic Schema**: Uses `triple:doi` via `owl:hasValue` restriction
   - **Usage**: Identifiers are directly instantiated as `triple:DOI` class members

2. **ISSN Class**
   - **Class**: `triple:ISSN`
   - **Inherits from**: `datacite:Identifier`
   - **Automatic Schema**: Uses `triple:issn` via `owl:hasValue` restriction
   - **Usage**: Identifiers are directly instantiated as `triple:ISSN` class members

3. **ISBN Class**
   - **Class**: `triple:ISBN`
   - **Inherits from**: `datacite:Identifier`
   - **Automatic Schema**: Uses `triple:isbn` via `owl:hasValue` restriction
   - **Usage**: Identifiers are directly instantiated as `triple:ISBN` class members

4. **Handle Class**
   - **Class**: `triple:Handle`
   - **Inherits from**: `datacite:Identifier`
   - **Automatic Schema**: Uses `triple:handle` via `owl:hasValue` restriction
   - **Usage**: Identifiers are directly instantiated as `triple:Handle` class members

This approach provides strong typing for academic identifiers while maintaining full compatibility with the DataCite ontology. The identifier scheme association is inferred automatically through OWL restrictions, eliminating the need for manual `datacite:usesIdentifierScheme` assertions. Documents are connected to their typed identifiers using the `datacite:hasIdentifier` property.

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
