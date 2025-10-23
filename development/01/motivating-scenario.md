# Motivating Scenario (Iteration 1)

## Name
TRIPLE Document - Core Metadata Model

## Description

### General description

The TRIPLE ontology defines a comprehensive model for representing documents in the GoTriple discovery platform. At the core of this model is the `triple:Document` class, which extends both `schema:CreativeWork` from Schema.org and `foaf:Document` from the FOAF vocabulary.

**Ontological Design Decision**:

The `triple:Document` class is defined in the TRIPLE namespace (`https://gotriple.eu/ontology/triple#`) as a subclass of:
- **`schema:CreativeWork`**: Aligns with Schema.org's widely-adopted model for creative works, enabling interoperability with web-based systems and search engines
- **`foaf:Document`**: Ensures compatibility with the Friend-of-a-Friend vocabulary, a foundational semantic web standard for describing resources and documents

This dual inheritance strategy provides:
1. **Semantic Interoperability**: Documents can be recognized by systems expecting either Schema.org or FOAF vocabularies
2. **Extensibility**: TRIPLE-specific properties and constraints can be added to the `triple:Document` class without modifying external vocabularies
3. **Standards Compliance**: Leverages established ontological patterns from both web and semantic web communities
4. **Rich Semantics**: Inherits properties from both parent classes while maintaining TRIPLE's domain-specific requirements

**Platform Context**:

GoTriple is an advanced multilingual discovery platform specifically designed for the Social Sciences and Humanities (SSH) sector. The platform aggregates, processes, and semantically enriches diverse SSH resources including scholarly publications, research datasets, project descriptions, and researcher profiles from various European language repositories.

GoTriple's primary objective is to facilitate cross-disciplinary and cross-linguistic discovery and reuse of SSH resources. The platform provides advanced research support features including data visualization, web annotation, personalized recommendations, social networking capabilities, and innovative research funding approaches.

### Document Characteristics

In the TRIPLE ontology, a document (`triple:Document`) represents any scholarly or research-oriented resource available through the GoTriple platform. Each document is characterized by:

1. **Typology Variety**: Documents are classified into various types including Article, Bibliography, Blog Post, Book, Conference, Dataset, Image, Learning Object, Manuscript, Report, Periodical, Preprint, Review, Software, Text, Thesis, Map, and others. Types are represented using SKOS concepts from a controlled vocabulary.

2. **Multilingual Support**: The platform emphasizes accurate language identification and representation. Documents and their metadata components (titles, abstracts, keywords) are available in both the original language and English translation.

3. **Language Standardization**: Languages are represented using `schema:Language` following ISO-639-1 two-character codes (e.g., "en", "fr", "de"). The platform uses a controlled vocabulary including TRIPLE's primary languages (Croatian, English, French, German, Greek, Italian, Polish, Portuguese, Slovenian, Spanish, Ukrainian) and common additional languages (Arabic, Dutch, Swedish, etc.). Special labels "other" and "undefined" handle edge cases.

4. **Multiple Identifiers**: Each document is associated with multiple identifiers following the DataCite specification (`datacite:Identifier`). These include:
   - Local TRIPLE identifier (unique within the platform)
   - DOI (Digital Object Identifier) for persistent web referencing
   - Full document URL (direct access to content)
   - Source URL (original publication location)
   - Landing page URL (metadata and descriptive information)

Each identifier uses the `datacite:Identifier` class and specifies its scheme via `datacite:IdentifierScheme`.

### Technical Specification

**Class Definition**:
```
triple:Document rdf:type owl:Class ;
    rdfs:subClassOf schema:CreativeWork, foaf:Document .
```

**Core Properties and Restrictions**:

1. **Document Type** (`dc:type`):
   - Domain: `triple:Document`
   - Range: `skos:Concept` (from controlled vocabulary)
   - Cardinality: At least one (`owl:someValuesFrom`)
   - Represents the nature and format of the document

2. **Identifiers** (`datacite:hasIdentifier`):
   - Domain: `triple:Document`
   - Range: `datacite:Identifier`
   - Cardinality: At least one (`owl:someValuesFrom`)
   - Each identifier has an associated `datacite:IdentifierScheme`

3. **Language** (`schema:inLanguage`):
   - Domain: `triple:Document`
   - Range: `schema:Language`
   - Cardinality: At least one (`owl:someValuesFrom`)
   - Uses ISO-639-1 codes

**External Vocabularies Used**:
- **Dublin Core** (`dc:type`): Document type classification
- **DataCite** (`datacite:Identifier`, `datacite:hasIdentifier`, `datacite:usesIdentifierScheme`): Identifier management
- **Schema.org** (`schema:inLanguage`, `schema:Language`, `schema:CreativeWork`): Language metadata and creative work modeling
- **FOAF** (`foaf:Document`): Document representation
- **SKOS** (`skos:Concept`): Controlled vocabulary terms

## Example 1

A scholarly article in English with multiple identifiers:

- **Instance**: `document_1`
- **Type**: Instance of `triple:Document`
- **Document Type**: `type_5` (a `skos:Concept` representing "Article")
- **Identifiers**: `identifier_2` (DOI), `identifier_4` (Local ID)
- **Language**: `language_10` (English, "en")

Each identifier is a `datacite:Identifier` with an associated `datacite:IdentifierScheme`.

## Example 2

A research dataset in French with institutional identifiers:

- **Instance**: `document_45`
- **Type**: Instance of `triple:Document`
- **Document Type**: `type_7` (a `skos:Concept` representing "Dataset")
- **Identifiers**: `identifier_67` (institutional ID), `identifier_678` (handle system ID)
- **Language**: `language_2` (French, "fr")

## Example 3

A conference paper in English from a different source:

- **Instance**: `document_31`
- **Type**: Instance of `triple:Document`
- **Document Type**: `type_5` (a `skos:Concept` representing "Article")
- **Identifiers**: `identifier_78` (DOI), `identifier_645` (Source URL)
- **Language**: `language_10` (English, "en")

This example demonstrates how different documents can share the same type and language but maintain unique identifiers for proper differentiation within the platform.
