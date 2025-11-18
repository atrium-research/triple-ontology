# Motivating Scenario (Iteration 8)

## Name
Book Part Document Type Extension

## Description

### General description

The GoTriple platform continues to expand its document type vocabulary to provide more precise categorization of scholarly resources. A common type of publication in Social Sciences and Humanities (SSH) research is the "book part" - which includes book chapters, book sections, and other portions of larger book publications.

Book parts are distinct from complete books in that they represent a specific contribution within a larger edited volume or collected work. They often have their own authors (who may differ from the book's editors), titles, and page ranges, while being part of a broader publication context.

To improve the precision of document classification and facilitate more accurate discovery and filtering, the "Book part" document type needs to be added to the existing Document Types controlled vocabulary.

### Technical specification

The Book part document type will be added to the existing Document Types controlled vocabulary with the following characteristics:

1. **Term Identifier**: `typ_book-part`
2. **Term Label**: "Book part"
3. **Vocabulary Association**: Connected to the Document Types vocabulary (`skos:inScheme`)
4. **External Alignment**: Exact match to COAR resource type for Book part: `https://vocabularies.coar-repositories.org/resource_types/c_3248/`
5. **Usage**: Can be assigned to documents via the `schema:additionalType` property for enhanced vocabulary alignment and interoperability

This addition aligns the GoTriple ontology with the COAR (Confederation of Open Access Repositories) controlled vocabulary, ensuring interoperability with other scholarly information systems.

## Example 1

`document_1` has type `typ_book-part`. This term belongs to the Document Types vocabulary and has an exact match to the COAR resource type `https://vocabularies.coar-repositories.org/resource_types/c_3248/`.

## Example 2

`document_45` has type `typ_book-part`. It represents a chapter in an edited volume about digital humanities methodologies.

## Example 3

`typ_book-part` is a concept in the Document Types vocabulary that is exactly matched to the external COAR vocabulary term for book parts.
