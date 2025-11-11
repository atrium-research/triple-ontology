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

## [2.0.0] - 2025-10-24

### 2025-10-24 - Version 2.0.0 Release: Complete Ontology Serialization and Enhanced Metadata

**Type**: Major Release

**Description**:
Major release introducing complete ontology serialization (version 2.0.0) with comprehensive metadata, proper authorship attribution, and enhanced documentation following semantic web best practices.

**Key Changes**:

1. **Complete Ontology Serialization**:
   - Created final merged ontology from 11 SAMOD iterations (development/01 through development/11)
   - Generated multiple serialization formats: TTL, OWL/XML, JSON-LD, N-Triples
   - Added comprehensive HTML documentation with interactive features

2. **Enhanced Metadata**:
   - Added proper authorship: Alessandro Bertozzi (creator), Luca De Santis & Silvio Peroni (contributors)
   - Included comprehensive Dublin Core metadata (title, description, license, rights, subjects, etc.)
   - Added VANN vocabulary annotations (preferred namespace prefix and URI)
   - Included DCAT keywords for better discoverability
   - Added bibliographic citations in both Dublin Core and Schema.org formats

3. **Version Management**:
   - Updated to version 2.0.0 across all metadata fields
   - Added `owl:priorVersion` reference to version 1.0.0
   - Consistent version numbering in `owl:versionInfo`, `owl:versionIRI`, and `schema:version`

4. **External Ontology Label Standardization**:
   - Implemented consistent `prefix:LocalName` format for all external ontology references
   - Updated CLAUDE.md with comprehensive guidelines for ontology metadata and serialization
   - Documented naming conventions for future development

5. **Technical Improvements**:
   - All annotation properties properly declared
   - Complete prefix declarations including vann: and dcat: vocabularies
   - Enhanced ontology structure with proper OWL2 compliance

**Files Added**:
- `ontology/2025-10-24/serializations/triple.ttl` (834 lines)
- `ontology/2025-10-24/serializations/triple.owl` (1360 lines)
- `ontology/2025-10-24/serializations/triple.jsonld` (1614 lines)
- `ontology/2025-10-24/serializations/triple.nt` (838 lines)
- `ontology/2025-10-24/html/index-en.html` (1384 lines)
- Complete HTML documentation with resources (CSS, JS, icons)

**Files Modified**:
- `CLAUDE.md` - Updated with comprehensive ontology metadata guidelines
- Removed legacy `ontology/triple-ontology.ttl` (639 lines)

**Net Changes**: +7150 insertions, -639 deletions

**Author**: Alessandro Bertozzi

**Commit**: 3ce0f35 - "add new complete serialization and documentation"

---

## [Unreleased]

### 2025-11-07 - Restructuring: Iterations 12-16 Reorganization

**Type**: Refactoring

**Description**:
Restructured iterations 12-16 to separate each resource type into its own dedicated iteration following SAMOD methodology. The previous Iteration 12 (which contained all three new resource types together) has been split into four separate iterations (12-15), and the CIDOC-CRM alignment has been moved to Iteration 16.

**New Structure**:
- **Iteration 12**: Dataset - Research dataset as distinct resource type
- **Iteration 13**: Multimedia - Audio-visual and interactive content
- **Iteration 14**: Semantic Artefact - Ontologies, vocabularies, knowledge graphs
- **Iteration 15**: Software - Research software, tools, code repositories
- **Iteration 16**: CIDOC-CRM and SSHOCRo Alignment - External ontology mappings

**Rationale**:
Each resource type deserves its own complete SAMOD iteration with dedicated motivating scenarios, competency questions, and test instances. This structure provides better modularity, clearer documentation, and follows the one-concern-per-iteration principle.

**Files Created**:
- `development/12/` - Dataset iteration structure (empty templates)
- `development/13/` - Multimedia iteration structure (empty templates)
- `development/14/` - Semantic Artefact iteration structure (empty templates)
- `development/15/` - Software iteration structure (empty templates)
- `development/16/` - CIDOC-CRM/SSHOCRo alignment structure (empty templates)

**Status**: All iterations have complete file structure with proper titles and sections. Content population pending.

**Author**: Development team

---

### 2025-10-23 - Refactoring: Minor TBOX Cleaning

**Type**: Refactoring

**Description**:
Minor cleanup of TBOX files across multiple iterations to remove redundant class definitions and improve ontology structure consistency.

**Details**:
- **Iteration 01**: Simplified property definitions and removed redundant comments
- **Iteration 03**: Removed duplicate class definitions that were inherited from external vocabularies
- **Iteration 04**: Removed 40 lines of redundant class and property definitions already defined in previous iterations
- **Iteration 06**: Simplified class definitions by removing redundant property restrictions

**Design Decision**:
Following SAMOD best practices, each iteration should focus only on its specific modelet without re-declaring classes and properties already established in previous iterations. This reduces duplication and improves maintainability.

**Files Modified**:
- `development/01/TBOX.ttl` - 12 lines modified (formatting improvements)
- `development/03/TBOX.ttl` - 9 lines removed (redundant definitions)
- `development/04/TBOX.ttl` - 40 lines removed (redundant definitions)
- `development/06/TBOX.ttl` - 19 lines removed (redundant restrictions)

**Net Changes**: -70 deletions, +10 insertions

**Author**: Development team

---

### 2025-10-23 - Refactoring: Remove foaf:Agent Class

**Type**: Refactoring

**Description**:
Removed the unused `foaf:Agent` intermediate class, directly using `foaf:Person` and `foaf:Organization` instead to simplify the class hierarchy.

**Details**:
- **Removed class**: `foaf:Agent` was serving as an unnecessary intermediate class
- **Updated class hierarchy**:
  - `foaf:Person` now directly subclasses `schema:Person` with `schema:name` restriction
  - `foaf:Organization` now directly subclasses with `schema:name` restriction
  - Both classes maintain the same cardinality constraint: exactly 1 `schema:name` (xsd:string)
- **ABOX updates**: Simplified instance declarations in iterations 03 and 06
- **Documentation updates**: Updated glossary files to reflect the simplified class structure
- **Rationale**: FOAF already provides `foaf:Person` and `foaf:Organization` which are standard and well-adopted. The intermediate `foaf:Agent` class added complexity without semantic benefit.

**Files Modified**:
- `.gitignore` - Added Python cache exclusions
- `development/03/TBOX.ttl` - Removed `foaf:Agent` class, moved restrictions to `foaf:Person` and `foaf:Organization`
- `development/03/ABOX.ttl` - Simplified agent instances
- `development/06/TBOX.ttl` - Removed `foaf:Agent` class, moved restrictions to `foaf:Person` and `foaf:Organization`
- `development/06/ABOX.ttl` - Simplified agent instances
- `development/06/glossary-of-terms.md` - Removed `foaf:Agent` term definition
- `development/07/glossary-of-terms.md` - Updated class hierarchy documentation

**Net Changes**: +32 insertions, -60 deletions

**Author**: Development team

---

### 2025-10-23 - Iteration 01: Addition of Core Descriptive Metadata and URL Identifiers

**Type**: Addition

**Description**:
Enhanced Iteration 01 with essential descriptive metadata properties (title, abstract, format) and comprehensive URL identifier support using DataCite pattern for consistency.

**Details**:

**Part 1 - Core Descriptive Metadata**:
- **New properties added**:
  - `schema:headline` - Document title (multilingual, rdf:langString)
  - `schema:abstract` - Document abstract/summary (multilingual, rdf:langString)
  - `schema:encodingFormat` - File format as MIME type (xsd:string)
- **TBOX updates**: Added three new data properties with cardinality restrictions on `triple:Document`
- **ABOX examples**:
  - `document_1` with bilingual title/abstract (English & French) + PDF format
  - `document_31` with English title/abstract + HTML format
- **Competency questions**: Added 5 new questions (CQ_1.8 to CQ_1.12) with corresponding SPARQL queries
- **Coverage impact**: 70.8% (17/24) → 83.3% (20/24)

**Part 2 - URL Identifier Support**:
- **New IdentifierSchemes**:
  - `triple:landing_page_url` - Landing page with metadata and descriptive information
  - `triple:full_text_url` - Direct access to full document content
  - `triple:source_url` - Original publication location or source repository
- **Design decision**: Used DataCite Identifier pattern instead of Schema.org direct properties (`schema:url`, `schema:mainEntityOfPage`, `schema:isBasedOnURL`) to maintain consistency with DOI, ISBN, ISSN, Handle identifiers
- **ABOX examples**: Added 3 URL identifiers to `document_1`:
  - Landing page: https://hal.archives-ouvertes.fr/hal-12345
  - Full text: https://hal.archives-ouvertes.fr/hal-12345/document
  - Source: https://journals.openedition.org/dh/12345
- **Competency questions**: Added 2 new questions (CQ_1.13, CQ_1.14) with SPARQL queries for URL retrieval
- **Coverage impact**: 83.3% (20/24) → **95.8% (23/24)**

**Files Modified**:
- `development/01/TBOX.ttl` - Added 3 data properties with restrictions
- `development/01/ABOX.ttl` - Added 3 IdentifierSchemes + 3 URL identifiers + metadata examples
- `development/01/motivating-scenario.md` - Updated technical specification and Example 1
- `development/01/informal-competency-questions.md` - Added 7 new questions (CQ_1.8 to CQ_1.14)
- `development/01/formal-competency-questions.md` - Added 7 SPARQL queries
- `development/01/glossary-of-terms.md` - Added 6 new terms

**Rationale**:
The DataCite approach for URLs ensures architectural consistency, strong typing, and alignment with scholarly publishing standards used by major SSH repositories (HAL, Zenodo, OpenAIRE). This pattern allows distinguishing between different URL types while maintaining the same structure as academic identifiers.

**Author**: Development team

---

### 2025-10-23 - Iteration 06: Refactoring to Remove PRO Ontology References

**Type**: Refactoring

**Description**:
Completely refactored Iteration 06 to remove all references to the PRO (Publishing Roles Ontology) and updated the author profile model to use Schema.org and FOAF properties directly.

**Details**:
- **Removed PRO ontology**: Eliminated all references to `pro:RoleInTime`, `pro:withRole`, `pro:isHeldBy`, `pro:isDocumentContextFor`
- **Updated model**: Documents now link directly to author profiles using `schema:author` property
- **Profile claiming mechanism**: Profiles can be "claimed" or "unclaimed" based on presence of `foaf:account` property
- **Name decomposition**: Added `schema:givenName` and `schema:familyName` to all profiles for better name disambiguation
- **Realistic examples**: Replaced generic placeholder names with realistic examples:
  - Example 1: John Smith / J. Smith (name variation disambiguation)
  - Example 2: Maria Rossi with 3 variants (Maria Rossi, M. Rossi, Maria R. Rossi) + Pierre Dupont (unclaimed)
  - Example 3: Single user account claiming multiple profile variations
- **Documentation updates**:
  - Completely rewritten glossary (15 terms) removing PRO concepts
  - Updated motivating scenario with clear technical specification
  - Enhanced all 5 informal competency questions
  - Added new CQ_6.6 for givenName/familyName queries
  - Added new CQ_6.9 SPARQL query for filtering by family name
- **Updated formal competency questions**: All SPARQL queries now use `schema:author` instead of PRO patterns

**Files Modified**:
- `development/06/glossary-of-terms.md` - Completely rewritten (removed 6 PRO terms, added 15 correct terms)
- `development/06/motivating-scenario.md` - Technical specification and all 3 examples rewritten
- `development/06/informal-competency-questions.md` - All 5 questions updated + 1 new question added
- `development/06/ABOX.ttl` - Added givenName/familyName to all 5 profiles with realistic names
- `development/06/formal-competency-questions.md` - Updated expected results + 1 new SPARQL query
- `development/05/formal-competency-questions.md` - Removed PRO prefix, updated CQ_5.2
- `development/07/motivating-scenario.md` - Removed PRO pattern description

**Design Decision**:
Simplified author attribution by using direct `schema:author` links instead of complex role-in-time patterns. The claiming mechanism (presence/absence of `foaf:account`) provides clearer semantics for claimed vs unclaimed profiles.

**Competency Questions**: 9 total (was 8, added 1 for name decomposition)

**Author**: Development team

---

### 2025-10-23 - Iteration 07: Projects (Research Projects in SSH Domain) - Completion

**Type**: Addition

**Description**:
Completed Iteration 07 by extending and formalizing competency questions for SSH research projects, expanding TBOX/ABOX with comprehensive examples and full SPARQL test coverage.

**Details**:
- Extended motivating scenarios from basic project description to **4 comprehensive examples**:
  - TRIPLE-SSH project funded by Horizon 2020 (EU Commission)
  - National research project on migration studies (PRIN-funded)
  - Collaborative heritage documentation project (multi-funder: FWF + Getty Foundation)
  - ERC Advanced Grant on ancient philosophy
- Expanded informal competency questions from **3 to 10 questions** covering:
  - Project metadata retrieval (identifiers, dates, names, descriptions)
  - Multi-funder/sponsor analysis
  - Discipline/topic filtering and search
  - Duration calculations and temporal queries
  - Identifier scheme usage patterns
  - Organization funding analysis
  - Keyword frequency analysis
  - Full-text search across project fields
- Expanded formal competency questions from **3 basic to 10 comprehensive SPARQL queries**
  - Enhanced CQ_7.1: Complete metadata properties query with optional fields
  - Enhanced CQ_7.2: Funding grants with funder and sponsor details
  - New CQ_7.3: Multi-funder project identification
  - New CQ_7.4: Discipline-based project filtering (e.g., Digital Humanities)
  - New CQ_7.5: Project duration calculations
  - New CQ_7.6: Temporal filtering (projects active in specific period)
  - New CQ_7.7: Identifier scheme enumeration
  - New CQ_7.8: Organization funding patterns (multi-project funders)
  - New CQ_7.9: Keyword frequency analysis
  - New CQ_7.10: Full-text search in project metadata
- Completed TBOX.ttl with **170 lines** defining:
  - `schema:Project` class with comprehensive restrictions
  - Properties: `schema:about`, `schema:funder`, `schema:funding`, `schema:keywords`, `schema:sponsor`
  - Data properties: `schema:alternateName`, `schema:description`, `schema:startDate`, `schema:endDate`
  - Support classes: `schema:Grant`, `schema:DefinedTerm`
  - Cardinality constraints and value type restrictions
- Completed ABOX.ttl with **259 lines** containing:
  - 4 complete project instances with realistic metadata
  - 5 identifier schemes (H2020, PRIN, FWF, Getty, ERC)
  - 10 organizations (funders, sponsors, coordinating entities)
  - 5 grants with funder/sponsor relationships
  - 8 topics/disciplines (SKOS concepts)
  - 15 keywords (defined terms)
- Updated glossary with **26 terms** defining all classes and properties

**Design Patterns**:
- Used `schema:Grant` with `schema:funder` and `schema:sponsor` for funding relationships
- Projects can have multiple grants (multi-funder support)
- Temporal information via `xsd:date` typed literals
- Multilingual support for names, acronyms, descriptions (`rdf:langString`)
- Subject indexing via SKOS concepts and Schema.org DefinedTerms
- Reused DataCite identifier pattern from Iteration 01

**Files Modified**:
- `development/07/motivating-scenario.md` - Extended from 1 to 4 examples (+106 lines)
- `development/07/informal-competency-questions.md` - Expanded from 3 to 10 questions (+193 lines)
- `development/07/glossary-of-terms.md` - Refined and completed 26 term definitions (+51 lines change)
- `development/07/TBOX.ttl` - Created complete terminological box (+170 lines)
- `development/07/ABOX.ttl` - Created complete assertional box (+259 lines)
- `development/07/formal-competency-questions.md` - Expanded from 3 to 10 SPARQL queries (+298 lines)

**Artifacts Pending**:
- `development/07/modelet.graphml` (Graffoo diagram source)
- `development/07/modelet.png` (Visual diagram)

**Statistics**:
- Total changes: +1077 insertions, -70 deletions
- 6 files modified
- 10 competency questions with full SPARQL coverage
- 4 realistic project examples with complete metadata

**Author**: Development team

---

### 2025-10-23 - Refactoring: Introduction of triple:Document

**Type**: Refactoring

**Description**:
Major refactoring to introduce `triple:Document` class in the TRIPLE namespace with dual inheritance pattern, replacing incorrect usage of `foaf:Document` throughout all iterations.

**Details**:
- **Main Change**: Defined `triple:Document` as subclass of both `schema:CreativeWork` and `foaf:Document`
  - Establishes dual inheritance pattern for semantic interoperability
  - Resolves namespace ownership issues (TRIPLE ontology now owns its Document class)
  - Maintains compatibility with both Schema.org and FOAF vocabularies
- **Iteration 01**: Foundational `triple:Document` definition with labels, comments, and restrictions for document types, identifiers, and languages
- **Iteration 02**: Expanded controlled vocabularies with 4 complete examples (License, Access Conditions, Document Type, Discipline) including real external matches to COAR, Creative Commons, and Library of Congress; added 10 informal and 12 formal competency questions; corrected `skos:definition` from `owl:DatatypeProperty` to `owl:AnnotationProperty` (SKOS compliance)
- **Iteration 03**: Updated property domains and 2 document instances
- **Iteration 04**: Updated property domains and class definitions
- **Iteration 05**: Simplified to focus only on Cluster and isDiscarded functionality (removed redundant definitions from previous iterations following SAMOD best practices)
- **Iteration 06**: Added `triple:Document` with author profile restrictions, updated 5 document instances
- **Iteration 08**: Added `triple:Document` with `dc:type` restrictions, updated 2 document instances
- **Iteration 09**: Added `triple:Document` with `schema:conditionsOfAccess` restrictions, updated 3 document instances
- **Iteration 10**: Added `triple:Document` with `datacite:hasIdentifier` restrictions, updated 4 document instances, fixed 2 SPARQL queries
- **Iteration 11**: Resolved `schema:CreativeWork` conflict, updated 8 document instances, fixed 5 SPARQL queries

**Design Decision**:
Chose dual inheritance (`schema:CreativeWork` + `foaf:Document`) to maximize interoperability with both Schema.org (widely used for web semantics) and FOAF (standard for social networks and scholarly communications).

**Files Modified**: 31 files across 10 iterations
- TBOX files: 10 (iterations 01-06, 08-11)
- ABOX files: 10 (iterations 01-06, 08-11)
- Documentation files: 11 (motivating scenarios, glossaries, competency questions)

**Statistics**:
- Document instances updated: 22
- SPARQL queries corrected: 7
- Net changes: +1118 insertions, -664 deletions (+454 lines)

**Author**: Development team

---

## [1.0.0] - 2025-10-22

### Release v1.0.0 - First Stable Release of TRIPLE Ontology

**Type**: Release

**Description**:
First stable release of the TRIPLE ontology, representing the complete ontology with all 7 original SAMOD iterations plus 4 extension iterations (08-11).

**Details**:
- Complete ontology package with development artifacts for 11 iterations
- Refactored diagrams (Graffoo notation) for all iterations
- Refactored SPARQL competency questions organized by iteration
- HTML documentation and controlled vocabularies
- Release includes:
  - `development/` directory with all 11 iterations (motivating scenarios, glossaries, TBOX/ABOX, competency questions, diagrams)
  - `diagrams/` directory with visual representations (01.png - 07.png)
  - `sparql/` directory with refactored competency questions (01.md - 07.md)
  - `serializations/` directory with consolidated ontology in Turtle format

**Technical Changes**:
- Updated release date to 2025-10-22
- Changed `owl:versionIRI` to `owl:versionInfo` for stable URI management
- Complete package structure for reproducibility and documentation

**Ontology Coverage**:
- **Core Features** (Iterations 01-07):
  1. Document basics (types, languages, identifiers, metadata)
  2. Controlled vocabularies (license, access conditions, document types, disciplines)
  3. Document roles (author, contributor, publisher, provider, funder)
  4. Subject coverage (temporal, spatial, keywords)
  5. Duplicate handling and discarded entities
  6. Author profiles and user accounts
  7. Projects (SSH research projects)

- **Extensions** (Iterations 08-11):
  8. Book part document type with COAR alignment
  9. Access conditions vocabulary with COAR alignment
  10. Document identifier types (DOI, ISSN, ISBN, Handle)
  11. Document mentions and references

**Release Artifacts**:
- `releases/2025-10-14/` directory with complete package
- `releases/2025-10-14/RELEASE-NOTES.md` with detailed release information
- 95 files packaged (TBOX, ABOX, diagrams, SPARQL queries, documentation)

**Author**: Development team

---

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
Enhanced project documentation with SAMOD methodology guide.

**Details**:
- Created `SAMOD-METHODOLOGY.md` with detailed explanation of the three-phase SAMOD cycle

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
