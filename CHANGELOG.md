# Changelog - TRIPLE Ontology Development

This file tracks all changes and additions to the TRIPLE ontology following the SAMOD methodology.

## Format

Each entry follows this structure:
- **Date**: When the change was made
- **Iteration**: Which iteration was affected
- **Type**: [Addition | Modification | Refactoring | Documentation]
- **Description**: What was changed and why
- **Author**: Who made the change

---

## [Unreleased]

### 2025-10-06 - Documentation: JSON-LD Examples

**Type**: Documentation

**Description**:
Created examples directory with JSON-LD serialization examples demonstrating practical application of the TRIPLE ontology.

**Details**:
- Created `examples/` directory structure for data export examples
- Added comprehensive JSON-LD example demonstrating all ontology features:
  - Multilingual metadata (title, abstract in EN/FR)
  - Document types and access conditions with COAR mappings
  - Multiple identifier schemes (DOI, Handle)
  - Subject coverage (keywords, spatial, temporal, disciplines)
  - Role modeling (authors, publisher) with time intervals
  - Document mentions (citations, people, projects)
  - Cluster membership and discard flag
- Created JSON-LD reading guide explaining:
  - Key JSON-LD concepts (`@context`, `@id`, `@type`, `@value`, `@graph`)
  - How to read nested objects and arrays
  - Translation to RDF Turtle format
  - Validation and conversion tools
- Updated main `.gitignore` to exclude `CLAUDE.md`

**Files Created**:
- `examples/README.md` - Directory structure and purpose documentation
- `examples/jsonld/README.md` - JSON-LD reading guide
- `examples/jsonld/document-complete-example.jsonld` - Comprehensive document example

**Files Modified**:
- `.gitignore` - Added CLAUDE.md exclusion

**Purpose**:
- Reference implementations for data producers
- Test cases for ontology validation
- Templates for creating new data exports
- Practical documentation of ontology patterns

**Author**: Development team

---

### 2025-10-06 - Tooling: Ontology Merge Script

**Type**: Tooling / Automation

**Description**:
Created Python script to merge all TBOX files from development iterations into a single consolidated ontology file containing only the ontology structure (no instance data).

**Details**:
- Created `scripts/` directory with merge automation tooling
- Script merges all `TBOX.ttl` files from `development/` iterations (01-11)
- Skips `ABOX.ttl` files to exclude instance data
- Outputs consolidated ontology to `ontology/triple-ontology.ttl`
- Adds ontology metadata (version IRI, labels, comments, dates)
- Provides statistics about merged ontology:
  - Classes count
  - Object properties count
  - Data properties count
  - Total triples count
- Uses RDFlib for RDF graph manipulation
- Virtual environment support with `.gitignore` for Python artifacts
- Comprehensive documentation in `scripts/README.md`

**Current Output**:
- **File**: `ontology/triple-ontology.ttl`
- **Size**: 14KB, 372 lines
- **Content**: 331 triples (TBOX only)
  - 23 classes
  - 25 object properties
  - 7 data properties

**Files Created**:
- `scripts/merge_iterations.py` - Main merge script
- `scripts/requirements.txt` - Python dependencies (rdflib==7.0.0)
- `scripts/README.md` - Script documentation and usage guide
- `scripts/.gitignore` - Python/venv artifacts exclusion
- `ontology/triple-ontology.ttl` - Consolidated ontology output (TBOX only)

**Usage**:
```bash
# Default output to ../ontology/triple-ontology.ttl
python merge_iterations.py

# Custom output path
python merge_iterations.py --output /path/to/output.ttl
```

**Author**: Development team

---

### 2025-10-05 - Iteration 11: Document Mentions and References

**Type**: Addition

**Description**:
Added support for documents to mention other entities (documents, people, projects, organizations) using the Schema.org `schema:mentions` property.

**Details**:
- Implemented generic mentions functionality using `schema:mentions` property
- Documents can mention various types of entities:
  - **Other Documents** (`foaf:Document`) - citations and bibliographic references
  - **People** (`foaf:Person`) - researchers or scholars discussed in the text
  - **Projects** (`schema:Project`) - research projects referenced or evaluated
  - **Organizations** (`foaf:Organization`) - institutions or research centers mentioned
- Established explicit compatibility: `foaf:Document rdfs:subClassOf schema:CreativeWork`
- Also declared: `foaf:Person rdfs:subClassOf schema:Thing` and `foaf:Organization rdfs:subClassOf schema:Thing`
- Flexible range allows mentioning any type of entity while maintaining simplicity
- SPARQL queries can filter mentions by type when needed
- Enables:
  - Citation network analysis
  - Discovery of related resources
  - Context enrichment for documents
  - Cross-referencing across entity types

**Design Decision**:
Chose Schema.org generic `schema:mentions` (Opzione A) over specialized sub-properties for simplicity and maximum flexibility. Entity types are distinguished through SPARQL type filtering.

**Files Created**:
- `development/11/motivating-scenario.md`
- `development/11/informal-competency-questions.md`
- `development/11/glossary-of-terms.md`
- `development/11/TBOX.ttl`
- `development/11/ABOX.ttl`
- `development/11/formal-competency-questions.md`

**Artifacts Pending**:
- `development/11/modelet.graphml` (Graffoo diagram source)
- `development/11/modelet.png` (Visual diagram)

**Competency Questions**: 9 questions defined and tested
- CQ_11.1: Retrieve all entities mentioned by a document
- CQ_11.2: Get documents mentioned by a specific document
- CQ_11.3: Find documents mentioning a specific person
- CQ_11.4: List all projects mentioned in any document
- CQ_11.5: Get organizations mentioned by a document
- CQ_11.6: Retrieve people mentioned by a document
- CQ_11.7: Find documents that cite other documents
- CQ_11.8: Get mentioned entities with their types
- CQ_11.9: Count mentions per document (with aggregation)

**Author**: Development team

---

### 2025-10-04 - Iteration 10: Document Identifier Types Extension

**Type**: Addition / Extension

**Description**:
Extended the ontology to explicitly support the four primary identifier schemes used in academic publishing: DOI, ISSN, ISBN, and Handle.

**Details**:
- Formalized four standard identifier schemes as instances of `datacite:IdentifierScheme` following DataCite naming conventions:
  - **DOI** (`triple:doi`) - Digital Object Identifier for persistent identification of digital objects
  - **ISSN** (`triple:issn`) - International Standard Serial Number for serial publications
  - **ISBN** (`triple:isbn`) - International Standard Book Number for books and book-like products
  - **Handle** (`triple:handle`) - Handle System for persistent identifier infrastructure
- Each identifier scheme includes:
  - `rdfs:label` for human-readable name (e.g., "DOI"@en)
  - `rdfs:comment` for detailed description
- Each identifier (`datacite:Identifier`) must use exactly one scheme via `datacite:usesIdentifierScheme`
- Each identifier must have exactly one literal value via `litre:hasLiteralValue`
- Documents can have multiple identifiers of different types
- Added cardinality restrictions to ensure data integrity:
  - `datacite:Identifier` has exactly 1 `datacite:IdentifierScheme`
  - `datacite:Identifier` has exactly 1 literal value (xsd:string)
- Naming convention follows DataCite standards (simple names without "_scheme" suffix)
- Builds upon the identifier pattern established in Iteration 01

**Files Created**:
- `development/10/motivating-scenario.md`
- `development/10/informal-competency-questions.md`
- `development/10/glossary-of-terms.md`
- `development/10/TBOX.ttl`
- `development/10/ABOX.ttl`
- `development/10/formal-competency-questions.md`

**Artifacts Pending**:
- `development/10/modelet.graphml` (Graffoo diagram source)
- `development/10/modelet.png` (Visual diagram)

**Competency Questions**: 9 questions defined and tested
- CQ_10.1: Retrieve all DOI identifiers
- CQ_10.2: Get identifier scheme for specific identifier
- CQ_10.3: Find documents with DOI identifiers
- CQ_10.4: List all identifier schemes
- CQ_10.5: Get all identifiers and schemes for a document
- CQ_10.6: Retrieve literal value of specific identifier
- CQ_10.7: Find documents with ISBN identifiers
- CQ_10.8: Get identifiers and schemes for specific document
- CQ_10.9: Retrieve all identifiers with schemes and values

**Author**: Development team

---

### 2025-10-03 - Iteration 09: Access Conditions Vocabulary Extension and COAR Alignment

**Type**: Addition / Mapping

**Description**:
Extended the `conditions_of_access` controlled vocabulary by mapping and adding four COAR (Confederation of Open Access Repositories) access rights terms.

**Details**:
- Mapped existing GoTriple access conditions vocabulary to COAR Access Rights standard
- Added four access level terms with `skos:exactMatch` to COAR URIs:
  - **Embargoed Access** (`acc_embargoed-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_f1cf/`
  - **Metadata Only Access** (`acc_metadata-only-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_14cb/`
  - **Open Access** (`acc_open-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_abf2/`
  - **Restricted Access** (`acc_restricted-access`) → `https://vocabularies.coar-repositories.org/access_rights/c_16ec/`
- Each term is a `skos:Concept` within the `triple:conditions_of_access` ConceptScheme
- Documents are linked to access conditions via `schema:conditionsOfAccess` property
- Ensures interoperability with global repository networks and scholarly infrastructures

**Files Created**:
- `development/09/motivating-scenario.md`
- `development/09/informal-competency-questions.md`
- `development/09/glossary-of-terms.md`
- `development/09/TBOX.ttl`
- `development/09/ABOX.ttl`
- `development/09/formal-competency-questions.md`

**Artifacts Pending**:
- `development/09/modelet.graphml` (Graffoo diagram source)
- `development/09/modelet.png` (Visual diagram)

**Competency Questions**: 7 questions defined and tested
- CQ_9.1: Retrieve documents with open access
- CQ_9.2: Identify vocabulary scheme for access terms
- CQ_9.3: Get all COAR external term mappings
- CQ_9.4: Get access condition for specific document
- CQ_9.5: List all access condition terms in vocabulary
- CQ_9.6: Retrieve documents with metadata-only access
- CQ_9.7: Get COAR external term for specific access condition

**Author**: Development team

---

### 2025-10-02 - Iteration 08: Book Part Document Type

**Type**: Addition

**Description**:
Added "Book part" document type to the Document Types controlled vocabulary.

**Details**:
- Created Iteration 08 following SAMOD methodology
- Added `typ_book-part` as a new `skos:Concept` in the `document_types` vocabulary
- Established `skos:exactMatch` alignment with COAR resource type: `https://vocabularies.coar-repositories.org/resource_types/c_3248/`
- Book part represents portions of books such as chapters, sections, or contributions to edited volumes
- Documents can be classified as book parts using `dc:type` property

**Files Created**:
- `development/08/motivating-scenario.md`
- `development/08/informal-competency-questions.md`
- `development/08/glossary-of-terms.md`
- `development/08/TBOX.ttl`
- `development/08/ABOX.ttl`
- `development/08/formal-competency-questions.md`

**Artifacts Pending**:
- `development/08/modelet.graphml` (Graffoo diagram source)
- `development/08/modelet.png` (Visual diagram)

**Competency Questions**: 5 questions defined and tested
- CQ_8.1: Retrieve documents with "Book part" type
- CQ_8.2: Identify vocabulary scheme for `typ_book-part`
- CQ_8.3: Get external term alignments
- CQ_8.4: Get document type for specific document
- CQ_8.5: List all document types in vocabulary

**Author**: Development team

---

### 2025-10-05 - Documentation Enhancement

**Type**: Documentation

**Description**:
Enhanced project documentation with comprehensive SAMOD methodology guide and improved CLAUDE.md instructions.

**Details**:
- Created `SAMOD-METHODOLOGY.md` with detailed explanation of the three-phase SAMOD cycle
- Updated `CLAUDE.md` with:
  - Expanded project overview including GoTriple platform description
  - Detailed core design decisions for all 7 original iterations
  - Enhanced iteration coverage descriptions
  - Added SAMOD methodology reference section
  - Documented all document types and project metadata patterns

**Files Modified**:
- `CLAUDE.md`

**Files Created**:
- `SAMOD-METHODOLOGY.md`

**Author**: Development team

---

## Previous Development (Iterations 01-07)

The initial seven iterations of the TRIPLE ontology were developed following SAMOD methodology, covering:

1. **Iteration 01**: GoTriple Document basics (types, languages, identifiers, metadata)
2. **Iteration 02**: Controlled vocabularies (license, access conditions, document types, disciplines)
3. **Iteration 03**: Document roles (author, contributor, publisher, provider, funder, etc.)
4. **Iteration 04**: Subject coverage (temporal, spatial, keywords)
5. **Iteration 05**: Duplicate handling (document clusters) and discarded entities (flagged authors/keywords)
6. **Iteration 06**: Author profiles and user accounts (disambiguation, claimed/unclaimed profiles)
7. **Iteration 07**: Projects (SSH research projects with metadata, roles, subjects)

**Base ontology established**:
- Namespace: `https://gotriple.eu/ontology/triple#`
- Format: RDF/Turtle
- External standards integrated: FOAF, Dublin Core, DataCite, Schema.org, SKOS, SPAR

---

## Notes

- All changes follow the SAMOD (Simplified Agile Methodology for Ontology Development) three-phase cycle
- Each iteration includes: motivating scenario, competency questions (informal and formal), glossary, TBOX, ABOX, and diagrams
- Competency questions are tested with SPARQL queries against instance data
- Visual documentation uses Graffoo notation for OWL ontologies
