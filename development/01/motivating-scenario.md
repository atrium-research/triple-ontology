# Motivating Scenario (Iteration 1)

## Name
TRIPLE Document - Core Metadata Model

## Description

### General description

The TRIPLE ontology defines a comprehensive model for representing documents in the GoTriple discovery platform. At the core of this model is the `triple:Document` class, which extends both `schema:CreativeWork` from Schema.org and `foaf:Document` from the FOAF vocabulary.

**Ontological Design Decision**:

The `triple:Document` class is defined in the TRIPLE namespace (`https://gotriple.eu/ontology/triple/`) as a subclass of:
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

4. **Multiple Identifiers**: Each document carries several identifiers, all following the DataCite pattern. Every identifier is a `datacite:Identifier` node with exactly one `datacite:usesIdentifierScheme` and exactly one `litre:hasLiteralValue`: **the scheme is what tells one kind of identifier from another**, and the ontology has no identifier subclasses. Three kinds are mandatory:

   - **Internal ID** — scheme `triple:internal_id_schema`. Unique identifier within the GoTriple platform, for internal resource management.
   - **Persistent ID** — scheme `datacite:ark`. The ARK that GoTriple mints and exposes externally.
   - **Original Identifier** — scheme `triple:original_id_schema`, or a scheme naming the source system when it has one. The identifier the document carried where it was harvested.

The scheme is always asserted explicitly in the data; nothing is inferred. That these three are mandatory is expressed in `shapes/entity.shapes.ttl` and checked with SHACL, not stated as OWL axioms — OWL restrictions describe inferences rather than constraints, so a missing identifier would be inferred to exist instead of being reported.

The landing page, full text and source URLs are identifiers too, distinguished by their own schemes (`triple:landing_page_url_schema`, `triple:full_text_url_schema`, `triple:source_url_schema`), and DOI, Handle, ISSN and ISBN are optional additions with their DataCite schemes.

### Technical Specification

**Class Definition**:
```
triple:Document rdf:type owl:Class ;
    rdfs:subClassOf schema:CreativeWork, foaf:Document .
```

**Core Properties and Restrictions**:

2. **Identifiers** (`datacite:hasIdentifier`):
   - Domain: `triple:Document`
   - Range: `datacite:Identifier` — there are no identifier subclasses; every identifier carries exactly one `datacite:usesIdentifierScheme` and one `litre:hasLiteralValue`, and the scheme is what says which kind it is
   - Cardinality: no OWL restriction. Which identifiers a document must carry (one internal id, one ARK PID, at least one source identifier) is stated in `shapes/entity.shapes.ttl` and checked with SHACL

3. **Language** (`schema:inLanguage`):
   - Domain: `triple:Document`
   - Range: `schema:Language`
   - Cardinality: At least one (`owl:someValuesFrom`)
   - Uses ISO-639-1 codes

4. **Title** (`schema:headline`):
   - Domain: `triple:Document`
   - Range: `rdf:langString` (multilingual text)
   - Cardinality: At least one (`owl:someValuesFrom`)
   - Represents the document title in multiple languages

5. **Abstract** (`schema:abstract`):
   - Domain: `triple:Document`
   - Range: `rdf:langString` (multilingual text)
   - Cardinality: At least one (`owl:someValuesFrom`)
   - Provides a summary or description of the document content

6. **File Format** (`schema:encodingFormat`):
   - Domain: `triple:Document`
   - Range: `xsd:string` (MIME type)
   - Cardinality: At least one (`owl:someValuesFrom`)
   - Indicates the file format (e.g., "application/pdf", "text/html")

7. **Source** (`dcterms:source`):
   - Domain: `triple:Document`
   - Range: `owl:Thing` (unrestricted)
   - Cardinality: Optional (`owl:minCardinality 0`)
   - Indicates a related resource from which the described resource is derived or mentions.

**External Vocabularies Used**:
- **Schema.org** (`schema:inLanguage`, `schema:Language`, `schema:CreativeWork`, `schema:headline`, `schema:abstract`, `schema:encodingFormat`): Document type classification, language metadata, creative work modeling, and descriptive metadata
- **DataCite** (`datacite:Identifier`, `datacite:hasIdentifier`, `datacite:usesIdentifierScheme`): the whole identifier model, used as-is with no subclasses of our own
- **FOAF** (`foaf:Document`): Document representation
- **SKOS** (`skos:Concept`): Controlled vocabulary concepts for document types
- **SPAR Literal** (`litre:hasLiteralValue`): Literal value management for identifiers
- **Dublin Core Terms** (`dcterms:source`): Source reference


## Example 1

A scholarly article in English and French with multiple identifiers including URLs:

- **Instance**: `document_1`
- **Type**: Instance of `triple:Document`
- **Document Type**: `type_5` (a `skos:Concept` representing "Article")
- **Platform Identifiers** (each a `datacite:Identifier`, told apart by its scheme):
  - `identifier_internal_1` (scheme `triple:internal_id_schema`): "TRIPLE_DOC_001" - internal platform identifier
  - `identifier_pid_1` (scheme `datacite:ark`): "ark:/12345/doc-12345-abcd-6789" - the ARK GoTriple mints
  - `identifier_original_1` (scheme `triple:original_id_schema`): "hal-12345" - source system identifier
- **Additional Identifiers** (schema-based):
  - `identifier_landing_1` (Landing Page URL: "https://hal.archives-ouvertes.fr/hal-12345")
  - `identifier_fulltext_1` (Full Text URL: "https://hal.archives-ouvertes.fr/hal-12345/document")
  - `identifier_source_1` (Source URL: "https://journals.openedition.org/dh/12345")
- **Language**: `language_10` (English, "en")
- **Title**: "The Impact of Digital Humanities on SSH Research"@en, "L'impact des humanités numériques sur la recherche SHS"@fr
- **Abstract**: "This paper examines the transformative role of digital humanities in Social Sciences and Humanities research."@en, "Cet article examine le rôle transformateur des humanités numériques dans la recherche en sciences humaines et sociales."@fr
- **Format**: "application/pdf"
- **Source**: `document_journal` (The "Journal of Digital Humanities" containing this article)


The example shows the single pattern applied uniformly: every identifier, whether a platform id, an ARK, a source-system id or a URL, is a `datacite:Identifier` whose scheme states its kind.

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
- **Title**: "Migration Patterns in 20th Century Europe"@en
- **Abstract**: "An analysis of migration flows across European countries during the twentieth century."@en
- **Format**: "text/html"

This example demonstrates how different documents can share the same type and language but maintain unique identifiers and distinct titles, abstracts, and formats for proper differentiation within the platform.
