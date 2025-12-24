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

## [2.1.0] - 2025-12-24

### 2025-12-24 - Refactoring: Global Terms Namespace Standardization

**Type**: Refactoring

**Description**:
Standardized the ontology namespace URI from `https://gotriple.eu/ontology/triple#` to `https://gotriple.eu/ontology/triple/` (slash separator instead of hash) to align with best practices and resolve URI generation consistency issues.

**Details**:
- **Namespace Change**: Updated `TRIPLE` namespace URI to use a trailing slash `/` across the entire project.
- **Development Iterations**: Updated all 16 iterations in `development/` (TBox and ABox) to use `triple:` prefix and slash-based URIs. Removed redundant `@base` and `owl:Ontology` declarations from development files.
- **Source Vocabularies**: Standardized all vocabularies in `vocabularies/serializations/ttl/` to use the new namespace and removed manual ontology headers (delegated to build script).
- **Ontology Modules**: Updated all module serializations in `ontology/modules/serializations/` to consistent `triple:` prefix usage.
- **Build Script**: Updated `scripts/build.py` to generate headers with the correct slash-based namespace.
- **Merge Script**: Updated `scripts/merge_iterations.py` to use the correct `TRIPLE` namespace definition.
- **Main Ontology**: Consolidate `ontology/triple-ontology.ttl` now uses consistent `triple:` prefix for all TRIPLE-defined entities.

**Author**: Alessandro Bertozzi

### 2025-12-23 - Refactoring: Vocabulary Standardization and Modularization

**Type**: Refactoring / Enhancement

**Description**:
Standardized vocabulary file names, implemented the "Bridge Classes" pattern for better modularity, fixed prefix usage, and established strict imports in the main ontology file.

**Details**:
- **Renaming**: Renamed all vocabulary files to PascalCase to match their class definitions:
  - `disciplines.ttl` -> `Discipline.ttl`
  - `license.ttl` -> `License.ttl`
  - `conditions_of_access.ttl` -> `AccessCondition.ttl`
  - `content_types.ttl` -> `ContentType.ttl`
- **New Vocabulary**: Created `ProjectType.ttl` for project types.
- **Bridge Classes**: Defined bridge classes (e.g., `triple:Discipline`) directly within each vocabulary file to make them self-contained.
- **Prefix Fixes**: Corrected `Discipline.ttl` to use the `disc:` prefix for individuals and identifiers, replacing incorrect `owl:` usage.
- **Descriptions**: Replaced `skos:definition` with `rdfs:comment` for consistency and added descriptions to all vocabulary concepts.
- **Ontology Imports**: Updated `ontology/triple.ttl` to explicitly import all modular vocabularies and declare the `disc:` prefix.
- **Restrictions**: Fixed `sioc:topic` restrictions in `ontology/triple.ttl` to correctly reference `triple:Discipline`.

**Author**: Alessandro Bertozzi

### 2025-12-22 - Bugfix: Ontology Consistency

**Type**: Bugfix / Refactoring

**Description**:
Resolved inconsistencies in property definitions and relaxed redundant restrictions on `triple:Document`.

**Details**:
- **Bugfix**: Corrected `datacite:usesIdentifierScheme` in Iteration 10 (`development/10/TBOX.ttl`) which acted as `dcat:distribution` due to a copy-paste error.
- **Refactoring**: Removed redundant and conflicting `owl:allValuesFrom triple:Profile` restriction on `schema:author` in `triple:Document` (Iteration 06 and consolidated ontology). Now relies on the broader `foaf:Person` or `foaf:Organization` union.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Vocabularies Simplification

**Type**: Refactoring

**Description**:
Removed `skos:ConceptScheme` definitions and `skos:inScheme` assertions from all controlled vocabularies to simplify the model. Reset `project_types.ttl` to an empty state.

**Details**:
- **Refactoring**: Removed concept scheme elements from:
  - `conditions_of_access.ttl`
  - `content_types.ttl`
  - `disciplines.ttl`
  - `license.ttl`
- **Enhancement**: Added reference classes definition (`triple:AccessCondition`, `triple:ContentType`, `triple:Discipline`, `triple:License`) to all vocabulary individuals.
- **Refactoring**: Removed redundant `skos:Concept` type assertion from vocabulary individuals, as they are now typed with specific subclasses of `skos:Concept`.
- **Revert**: Cleared `project_types.ttl` content.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Addition: Project Type Controlled Vocabulary

**Type**: Addition

**Description**:
Implemented a controlled vocabulary for Project Types to classify projects (e.g., Research, Training, Network) and integrated it into Iteration 07.

**Details**:
- **Vocabulary**: Created `project_types.ttl` with SKOS concepts.
- **TBOX (Iteration 07)**:
  - Imported `project_types.ttl`.
  - Defined `triple:ProjectType` (Bridge Class) and `triple:hasProjectType` property.
  - Added restriction to `triple:Project`.
- **ABOX (Iteration 07)**: Added `triple:hasProjectType` assertions to example projects.
- **Documentation**: Updated Motivating Scenario, Glossary, and Competency Questions.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Geographic Properties and Publisher Cardinality

**Type**: Refactoring

**Description**:
Removed deprecated geographic properties and relaxed publisher cardinality constraints to improve flexibility and consistency.

**Details**:
- **Geographic Properties**: Removed `schema:geo` and `schema:GeoShape` from Iterations 04 (Places), 10 (Datasets), 11 (Multimedia), and 12 (Semantic Artefact).
- **Publisher Cardinality**: Removed `owl:maxCardinality 1` restriction on `schema:publisher` for `triple:Document` (Iteration 03), allowing multiple publishers.
- **ABOX Cleanup**: Updated `triple:place-northern-italy` in Iteration 11 to be `schema:Place` instead of `schema:GeoShape`.
- **Glossary**: Removed `schema:GeoShape` definitions.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Iterations 10 & 12 - Licensing Bridge Classes

**Type**: Refactoring / Addition

**Description**:
Extended the "Bridge Classes" pattern to Iteration 10 (Datasets) and Iteration 12 (Semantic Artefact), ensuring consistent rights and licensing metadata modeling across all resource types.

**Details**:
- **Dataset (Iteration 10)** & **Semantic Artefact (Iteration 12)**:
  - **TBOX**: Added `triple:License`, `triple:AccessCondition` classes and `triple:hasLicense`, `triple:hasAccessCondition` properties. Added restrictions to main classes.
  - **ABOX**: Added license/access instances and assertions to example resources.
  - **Documentation**: Updated Motivating Scenarios, Glossaries, and added Competency Questions checking for rights metadata.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Iteration 11 - Multimedia Licensing Alignment

**Type**: Refactoring

**Description**:
Refactored Iteration 11 (Multimedia) to align with the "Bridge Classes" pattern introduced in Iteration 02, replacing legacy string-based properties with semantic references.

**Details**:
- **TBOX**:
  - Added `triple:License` and `triple:AccessCondition` bridge classes.
  - Defined `triple:hasLicense` and `triple:hasAccessCondition` properties.
  - Added restrictions to `triple:MediaObject`.
- **ABOX**:
  - Replaced `schema:license` and `schema:conditionsOfAccess` string literals with URI references to new Bridge Class instances.
  - Instantiated specific licenses (e.g., `triple:cc_by_nc_nd_4_0`) and access conditions (e.g., `triple:open_access`).
- **Documentation**:
  - Updated `formal-competency-questions.md` SPARQL queries and expected results.
  - Updated `informal-competency-questions.md` expected results.

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Iteration 02 - Bridge Classes and Concept Scheme Removal

**Type**: Refactoring

**Description**:
Refactored Iteration 02 to implement a "Bridge Classes" pattern for controlled vocabularies and simplified the ontology by removing `skos:ConceptScheme`.

**Details**:
- **Bridge Classes**: Defined local classes (`triple:License`, `triple:AccessCondition`, `triple:Discipline`, `triple:ContentType`) that subclass both `skos:Concept` and relevant Dublin Core classes.
- **Properties**:
  - `triple:hasLicense` (subPropertyOf `dcterms:license`)
  - `triple:hasAccessCondition` (subPropertyOf `dcterms:accessRights`)
  - `triple:hasContentType` (subPropertyOf `dcterms:type`)
  - `sioc:topic` (subPropertyOf `dcterms:subject`, removed global range)
- **Restrictions**: Added local `owl:Restriction`s to `triple:Document` for all four properties to enforce typing.
- **Simplification**: Removed `skos:ConceptScheme` definitions and `skos:inScheme` assertions entirely; grouping is now handled via Bridge Classes.
- **Documentation**: Updated `motivating-scenario.md`, `glossary-of-terms.md`, and renumbered Competency Questions (2.1-2.10).

**Author**: Alessandro Bertozzi

---

### 2025-12-22 - Refactoring: Removal of schema:additionalType

**Type**: Refactoring

**Description**:
Completely removed `schema:additionalType` property from all iterations of the TRIPLE ontology to resolve inconsistencies and simplify the model.

**Details**:
- Removed TBOX definitions and restrictions from Iterations 01, 02, 10, 11, 12, and consolidated ontology.
- Removed ABOX assertions from all example individuals.
- Removed related competency questions and documentation patterns.
- Verified 0 remaining occurrences in the codebase.

**Author**: Alessandro Bertozzi

---

### 2025-12-21 - Addition: Iteration 13 - CIDOC-CRM and SSHOC-RO Alignment

**Type**: Addition

**Description**:
Implemented Iteration 13 to align TRIPLE ontology classes with CIDOC-CRM and SSHOC-RO using intensional mappings (`skos:exactMatch` and `skos:closeMatch`).

**Details**:
- **Mappings**:
  - `triple:Document`: `cidoc:E31_Document`, `sshocro:SHE8_Publication`
  - `triple:Project`: `cidoc:E7_Activity` (close), `sshocro:SHE3_SSH_Project` (exact)
  - `triple:Dataset`: `sshocro:SHE1_Dataset`
  - `triple:MediaObject` & `triple:SemanticArtefact`: `cidoc:E90_Symbolic_Object` (close)
- **Files**: Updated all files in `development/13/` to reflect these alignments.

**Author**: Alessandro Bertozzi

---

### 2025-12-21 - Addition: Iteration 16 - SKG-IF Alignment

**Type**: Addition

**Description**:
Added Iteration 16 to formally align TRIPLE ontology classes with the SKG-IF (Scientific Knowledge Graph Interoperability Framework) using mappings to FaBiO, FRAPO, and FOAF.

**Details**:
- **New Iteration**: `development/16/`
- **Mappings**:
  - `triple:Document` matches `fabio:ScholarlyWork`
  - `triple:Dataset` matches `fabio:Dataset`
  - `triple:SemanticArtefact` close match `fabio:Work`
  - `triple:MediaObject` close match `fabio:Work`
  - `triple:Profile` matches `foaf:Agent`
  - `triple:Project` close match `frapo:Grant`
- **Documentation**: Added motivating scenario, glossary, and competency questions.

**Author**: Alessandro Bertozzi

---

### 2025-12-21 - Enhancement: Project and Dataset Metadata Extensions

**Type**: Enhancement / Addition

**Description**:
Added contact points to all main ontology entities. Extended Dataset model with DCAT distribution, provenance support, and spatial bounding box properties.

**Details**:

**Iteration 10 (Datasets)**:
- **New Properties**:
  - `dcat:distribution` (Range: `dcat:Distribution`)
  - `dcat:bbox` (Range: `rdfs:Literal`)
  - `dcterms:provenance` (Range: `dcterms:ProvenanceStatement`)
- Added `schema:contactPoint` property

**Iteration 07 (Projects)**:
- Added `schema:contactPoint` property

**Cross-Cutting Changes**:
- Added `schema:contactPoint` to all other main resource types:
  - Iteration 03 (Documents)
  - Iteration 11 (MediaObject/Multimedia)
  - Iteration 12 (Semantic Artefacts)

**Author**: Alessandro Bertozzi

**Commits**:
- a9bddf1 - "add provenance, bbox adn distribution to dataset"
- 6c2f0f6 - "add contact point to project and add dcat distribution to dataset"
- 2115257 - "add contact point to all entities of the ontology"

---

### 2025-12-19 - Refactoring: Project and Dataset Metadata Alignment

**Type**: Refactoring / Addition

**Description**:
Aligned Iteration 07 (Projects) with new metadata requirements and refined identifier usage. Identified Iteration 10 (Datasets) and began metadata alignment. Refactored Iteration 01 to standardise schema.org prefix usage.

**Details**:

**Iteration 07 (Projects)**:
- **Refined Identifiers**:
  - Restricted `datacite:hasIdentifier` to `triple:ID`, `triple:PID`, `triple:OriginalIdentifier`
  - Removed `triple:DOI` and `triple:Handle` from Project restrictions
- **Added Metadata**:
  - `schema:organizer` (Range: `schema:Organization`)
  - `schema:knowsAbout` (Range: `skos:Concept`)
  - `schema:mainEntityOfPage` (Range: `schema:URL`)
  - `schema:inLanguage` (Range: `schema:Language`)
  - `schema:dateCreated`, `schema:dateModified` (Range: `xsd:date`, maxCardinality 1)
- **Files Aligned**: TBOX, ABOX, Motivating Scenario, Glossary, Competency Questions updated

**Iteration 10 (Datasets)**:
- Identified Iteration 10 as the "Dataset" definition iteration
- Added `schema:mainEntityOfPage` with `schema:URL` range
- Performed gap analysis for missing metadata fields

**Iteration 01 (Core)**:
- Refactored property definitions to preferentially use `schema:` prefix (e.g., `schema:inLanguage`, `schema:abstract`, `schema:headline`)

**Author**: Alessandro Bertozzi

---

### 2025-12-12 - Refactoring: Controlled Vocabularies Simplification

**Type**: Refactoring

**Description**:
Simplified controlled vocabularies by removing `datacite:IdentifierScheme` and `datacite:usesIdentifierScheme` from all vocabulary files. Identifiers are now declared as simple `datacite:Identifier` instances without scheme references.

**Details**:
- Removed `datacite:usesIdentifierScheme` property from all identifier declarations
- Removed `datacite:IdentifierScheme` class declarations
- Removed individual identifier scheme instances (`:documentType_identifier`, `:conditionsOfAccess_identifier`, `:licenses_identifier`, `:disciplines_identifier`)
- Fixed `:other` and `:undefined` concept identifiers to follow naming pattern (`:typ_other`, `:acr_other`, `:lic_other`, etc.)
- Maintained all SKOS concept definitions and external vocabulary mappings

**Files Modified**:
- `vocabularies/serializations/ttl/content_types.ttl` - Added `:video` and `:image` concepts (COAR c_12ce, c_c513), removed identifier schemes
- `vocabularies/serializations/ttl/conditions_of_access.ttl` - Removed identifier schemes
- `vocabularies/serializations/ttl/license.ttl` - Removed identifier schemes
- `vocabularies/serializations/ttl/disciplines.ttl` - Removed identifier schemes

**Rationale**:
The identifier scheme pattern added unnecessary complexity to controlled vocabularies. Since vocabularies use a consistent internal identifier pattern and rely on SKOS for semantic alignment with external vocabularies, the explicit scheme declaration was redundant.

**Author**: Alessandro Bertozzi

---

### 2025-12-12 - Refactoring: Iteration 06 Profile Model Simplification

**Type**: Refactoring

**Description**:
Major refactoring of Iteration 06 (Author Profile and User Account) to simplify the profile model by restructuring class hierarchy, removing name decomposition, eliminating "claim" terminology, and removing disambiguation references.

**Details**:

**Phase 1 - Class Hierarchy Restructuring**:
- Changed `triple:Profile` from subclass of `foaf:Person` to superclass
- Made `foaf:Person` and `foaf:Organization` subclasses of `triple:Profile`
- Profiles can now represent either persons or organizations
- Maintained `owl:equivalentClass` between `foaf:Person` and `schema:Person`
- No equivalence between `foaf:Organization` and `schema:Organization` (not overlapping)

**Phase 2 - Name Property Simplification**:
- Removed `schema:givenName` and `schema:familyName` properties
- Profiles now use only `schema:name` (full name string)
- Added cardinality restriction: exactly 1 `schema:name` required per profile
- Updated all ABOX examples to remove name decomposition
- Removed CQ_6.6 (family name query) and renumbered remaining queries

**Phase 3 - Terminology Normalization**:
- Replaced "claim/claimed/unclaimed" terminology with "associate/associated/unassociated"
- Updated all documentation, competency questions, and comments
- More neutral terminology that describes relationship without ownership implications

**Phase 4 - Identifier Requirement**:
- Added cardinality restriction: exactly 1 `datacite:Identifier` required per profile
- Ensures all profiles have unique identifiers

**Phase 5 - Disambiguation Reference Removal**:
- Removed all references to "also known as" relationships between profiles
- Removed concept of "original profile" vs derived profiles
- Simplified disambiguation section in motivating scenario
- No formal property for linking profile variations (previously removed `triple:alsoKnownAs`)
- Updated all examples to remove disambiguation references

**Files Modified**:
- `development/06/TBOX.ttl` - Restructured class hierarchy, added restrictions, removed properties
- `development/06/ABOX.ttl` - Removed givenName/familyName, updated all comments
- `development/06/motivating-scenario.md` - Simplified examples and technical specification
- `development/06/glossary-of-terms.md` - Updated class definitions and property descriptions
- `development/06/informal-competency-questions.md` - Removed CQ_6.4, updated all questions, renumbered
- `development/06/formal-competency-questions.md` - Removed queries, updated descriptions, renumbered

**Final Profile Model**:
- `triple:Profile` (superclass) with restrictions:
  - Exactly 1 `datacite:Identifier`
  - Exactly 1 `schema:name` (xsd:string)
  - Maximum 1 `foaf:account` (foaf:OnlineAccount)
- `foaf:Person` (subclass of triple:Profile)
- `foaf:Organization` (subclass of triple:Profile)

**Competency Questions**: Reduced from 7 to 5 questions (removed CQ_6.4 "original profile" and CQ_6.6 "family name query")

**Rationale**:
Simplified the profile model to focus on core functionality: profiles (person or organization) can be associated with user accounts. Removed complex disambiguation modeling and name decomposition that added unnecessary complexity without formal semantic representation.

**Author**: Alessandro Bertozzi

---

### 2025-12-12 - Documentation: Update README.md

**Type**: Documentation

**Description**:
Updated main README.md to provide clearer project overview and structure.

**Author**: Alessandro Bertozzi

**Commit**: 8bba21d - "update README"

---

### 2025-12-11 - Refactoring: Iterations Renumbering

**Type**: Refactoring

**Description**:
Changed iteration numbering to establish consistent sequence for new resource type iterations.

**Details**:
- Renumbered iterations to maintain logical progression
- Ensures proper iteration ordering in SAMOD development cycle

**Author**: Alessandro Bertozzi

**Commit**: becc9b5 - "change iterations numeration"

---

### 2025-12-10 - Enhancement: Clean TBOX Definitions and Add Controlled Vocabularies

**Type**: Enhancement

**Description**:
Removed redeclarations of imported external ontology classes and properties; added conditions of access and content types vocabularies directly to development iterations.

**Details**:
- Cleaned TBOX files across iterations by removing redundant declarations of Schema.org, FOAF, Dublin Core properties
- Added complete controlled vocabulary definitions for:
  - Conditions of Access (from iteration 09)
  - Content Types (formerly Document Types, from iteration 02)
- Improved ontology modularity and reduced duplication

**Files Modified**:
- Multiple TBOX files across development iterations
- Controlled vocabulary definitions consolidated in iterations 02 and 09

**Author**: Alessandro Bertozzi

**Commit**: c188ead - "remove redeclarations of imported class and properties; add conditions of access and content types"

---

### 2025-12-09 - Documentation: Add Ontology Visualization

**Type**: Documentation

**Description**:
Added GraphML format ontology visualization for enhanced documentation and structural overview.

**Details**:
- Created ontology visualization in GraphML format (yEd compatible)
- Provides visual representation of complete ontology structure
- Enables graph-based analysis and documentation

**Files Created**:
- Ontology visualization in GraphML format

**Author**: Alessandro Bertozzi

**Commit**: 7db2c25 - "add ontology visualization in graphml"

---

### 2025-12-08 - Tooling: Vocabulary Serialization Script

**Type**: Tooling / Automation

**Description**:
Created script to convert vocabulary serializations from RDF/XML to Turtle format.

**Details**:
- New Python script for converting RDF format vocabularies
- Supports automated conversion from RDF/XML to TTL
- Enhanced vocabulary management tooling

**Files Created**:
- Vocabulary conversion script
- New vocabulary serializations in TTL format

**Author**: Alessandro Bertozzi

**Commit**: b0867ab - "add new vocab serializations and script for converting in ttl format from rdf"

---

### 2025-12-07 - Enhancement: Add Vocabularies to Repository

**Type**: Addition

**Description**:
Added controlled vocabularies directly to repository for better accessibility and version control.

**Details**:
- Added complete controlled vocabulary files
- Includes all SKOS ConceptSchemes used in the ontology
- Improves vocabulary governance and traceability

**Files Created**:
- Vocabulary files added to repository structure

**Author**: Alessandro Bertozzi

**Commit**: 00ddd51 - "added vocabularies to repo"

---

### 2025-12-06 - Refactoring: Reorganize Serialization Directory

**Type**: Refactoring

**Description**:
Moved TRIPLE ontology serializations to current directory structure for better organization.

**Details**:
- Reorganized serialization files location
- Moved from nested structure to current directory
- Added MOD namespace binding in merge_graphs function

**Files Modified**:
- Serialization file locations updated
- `scripts/merge_iterations.py` - Added MOD namespace binding

**Author**: Alessandro Bertozzi

**Commits**: 
- db017f8 - "move triple serializations in current dir"
- 6a6d535 - "Add MOD namespace binding in merge_graphs function"

---

### 2025-12-05 - Refactoring: Remove triple:alsoKnownAs Property

**Type**: Refactoring

**Description**:
Removed the `triple:alsoKnownAs` property from the Profile model to simplify author profile management and disambiguation.

**Details**:
- **Iteration 06**: Removed `triple:alsoKnownAs` object property definition and restriction from Profile class
- Updated Profile model to rely solely on `foaf:account` for profile claiming mechanism
- Removed associated competency questions (CQ_6.5, CQ_6.7) and renumbered remaining questions
- Updated ABOX examples to remove alsoKnownAs usage

**Files Modified**:
- `development/06/TBOX.ttl` - Removed triple:alsoKnownAs property definition and Profile restriction
- `development/06/ABOX.ttl` - Removed triple:alsoKnownAs usage from profile examples
- `development/06/glossary-of-terms.md` - Removed triple:alsoKnownAs term definition
- `development/06/motivating-scenario.md` - Removed alsoKnownAs reference
- `development/06/formal-competency-questions.md` - Removed CQ_6.5 and CQ_6.7, renumbered CQ_6.8→CQ_6.6, CQ_6.9→CQ_6.7

**Rationale**:
Simplified profile model by removing complex disambiguation relationships, relying on the simpler claiming mechanism via user accounts for profile management.

**Author**: Alessandro Bertozzi

---

### 2025-11-30 - Refactoring: Major Ontology Architectural Changes

**Type**: Refactoring

**Description**:
Major refactoring introducing class-based identifier types, removing dc:type for content types, implementing controlled vocabularies pattern, and switching subject property from dc:subject to sioc:topic.

**Details**:

**Phase 1 - Identifier Architecture (Nov 25-28)**:
- Implemented class-based identifier types instead of scheme-based pattern:
  - Created `triple:DOI`, `triple:ISSN`, `triple:ISBN`, `triple:Handle`, `triple:ID`, `triple:PID`, `triple:OriginalIdentifier` classes
  - Each identifier class is subclass of `datacite:Identifier`
  - Uses `datacite:usesIdentifierScheme` for scheme references
  - Consolidated schemes to use `datacite:local-resource-identifier-scheme` for local identifiers
  - Extended identifier support to all main entities (Document, Dataset, MediaObject, SemanticArtefact, Project)
- Fixed typos: `usesIdentiferScheme` → `usesIdentifierScheme`
- Added `litre:hasLiteralValue` property with cardinality restrictions
- Distinguished between PID, ID, and OriginalIdentifier for documents

**Phase 2 - Content Types Refactoring (Nov 20-22)**:
- Renamed "Document Types" to "Content Types" across all iterations
- Removed `dc:type` for content type classification
- Updated all TBOX, ABOX, glossaries, and competency questions
- Ensured consistency across all 14 iterations

**Phase 3 - Controlled Vocabularies Pattern (Nov 18-19)**:
- Implemented SKOS-based controlled vocabularies pattern
- Created modular vocabulary files with owl:imports declarations
- Added comprehensive vocabulary documentation
- Standardized ConceptScheme and Concept definitions

**Phase 4 - Subject Property Migration (Nov 15-17)**:
- Replaced `dc:subject` with `sioc:topic` across entire ontology
- Updated all iterations, documentation, and SPARQL queries
- Ensures consistency in subject/topic modeling

**Phase 5 - Schema.org Property Restrictions (Nov 10-14)**:
- Removed rdfs:domain restrictions from Schema.org properties
- Fixed owl:allValuesFrom for schema:mentions property
- Updated rdfs:range for schema:headline and schema:abstract to rdf:langString
- Added cardinality restrictions to date patterns
- Replaced schema:identifier with DataCite pattern across iterations 4, 12-14
- Added constraints to MediaObject, SemanticArtefact, and Dataset

**Phase 6 - Resource Type Classes (Nov 5-8)**:
- Created triple:Project and triple:Dataset classes in TRIPLE namespace
- Created triple:MediaObject class (removed schema-specific subclass)
- Added mod:SemanticArtefact with proper prefix binding
- Updated all class references and documentation

**Phase 7 - Patterns and Status (Nov 1-4)**:
- Created patterns directory for reusable ontology patterns
- Added schema:mentions property pattern for CreativeWork references
- Implemented schema:creativeWorkStatus pattern for Dataset, MediaObject, SemanticArtefact
- Added date cardinality restrictions

**Files Modified**: 100+ files across all iterations

**Files Created**:
- `patterns/` directory with reusable ontology patterns
- Class definition files for new TRIPLE namespace classes
- Updated vocabulary module files

**Rationale**:
These changes establish a more robust, consistent, and interoperable ontology architecture:
- Class-based identifiers provide stronger typing and clearer semantics
- Schema.org properties offer better web integration than Dublin Core
- TRIPLE namespace classes ensure proper ontology ownership
- Controlled vocabularies pattern enables better vocabulary governance
- Removal of domain restrictions allows flexible property reuse

**Author**: Alessandro Bertozzi

**Commits**: 
- 92a0049 - "Implement class-based identifier types"
- 0792f9c - "Updated ABOX and TBOX ontologies to define new identifier classes"
- 92d7ea3 - "Refactor identifier schemes to use datacite prefixes"
- b525216 - "Extension to other doi entities"
- b67ae57 - "extend support to pid, internal_id and original id to other entites"
- 92988c9 - "align URL description pattern; add distinction between pid, id and original id"

- 2a13e43 - "Rename Document Types to Content Types"
- 0707a04 - "Add controlled vocabularies pattern"
- abc9a76 - "Add owl:imports declarations"
- 39a0697 - "Replace dc:subject with sioc:topic"
- 5d56f08 - "Refactor project and dataset classes to use triple:Project and triple:Dataset"
- 180010b - "add to multimedia triple:MediaObject"
- 09d6a18 - "Add mod:SemanticArtefact prefix"
- a393d8c - "Remove rdfs:domain restrictions for schema properties"
- 5429ade - "fix owl:allValuesFrom for schema:mentions property"
- 8b71040 - "Update rdfs:range for schema:headline and schema:abstract"
- 0f04d30 - "Add litre:hasLiteralValue property"
- eef6813 - "Add schema:mentions property and status pattern"
- a393af0 - "add cardinality restriction to date patterns"
- 4a83413 - "add patterns dir"
- 7eb9db9 - "Replace schema:identifier with DataCite pattern"
- 775bac1 - "Update iterations 12-13: add keywords support"
- bac6917 - "Remove skos:exactMatch and skos:closeMatch annotation properties"
- 28a3c47 - "Refactor vocabulary terms"
- 53f9840 - "remove dc:type"
- c43c2cd - "improve prefix management in merge script"
- 9e60f00 - "Add deduplication of OWL restrictions in merge_iterations script"

---

### 2025-12-05 - Enhancement: Standardize Identifier Schemes with DataCite (SUPERSEDED)

**Type**: Enhancement (SUPERSEDED BY NOV 30 REFACTORING)

**Description**:
~~Consolidated all local identifier types (ID, PID, OriginalIdentifier) to use the standardized `datacite:local-resource-identifier-scheme` instead of individual schemes.~~

**Note**: This change was part of the larger identifier architecture refactoring completed on November 30, 2025 (see above).

**Details**:
- **Iterations 01, 12, 13, 14**: Updated `triple:ID`, `triple:PID`, `triple:OriginalIdentifier` classes to use `datacite:local-resource-identifier-scheme`
- Removed individual schemes: `triple:internal_id_schema`, `triple:pid_schema`, `triple:original_id_schema`
- Fixed typo: `usesIdentiferScheme` → `usesIdentifierScheme` in iteration 01 ABOX
- Cleaned up TBOX and ABOX definitions across all affected iterations

**Files Modified**:
- `development/01/TBOX.ttl` - Updated classes and added datacite:local-resource-identifier-scheme
- `development/01/ABOX.ttl` - Fixed typo and cleaned up schema references
- `development/12/TBOX.ttl` - Updated classes and removed old schemas
- `development/12/ABOX.ttl` - Removed old schema definitions
- `development/13/TBOX.ttl` - Updated classes and removed old schemas
- `development/13/ABOX.ttl` - Updated schema references
- `development/14/TBOX.ttl` - Updated classes and removed old schemas

**Rationale**:
Aligns with DataCite standards for local resource identifiers, providing consistency and interoperability across the platform's identifier system.

**Author**: Alessandro Bertozzi

---

### 2025-12-05 - Enhancement: Add dcterms:isReferencedBy to MediaObject and Dataset

**Type**: Enhancement  

**Description**:
Added `dcterms:isReferencedBy` property with restrictions to MediaObject and Dataset classes for consistency with SemanticArtefact.

**Details**:
- **Iteration 12 (Dataset)**: Added restriction `allValuesFrom triple:Document` for `dcterms:isReferencedBy` property
- **Iteration 13 (MediaObject)**: Added `dcterms:isReferencedBy` property definition and restriction `allValuesFrom triple:Document`

**Files Modified**:
- `development/12/TBOX.ttl` - Added dcterms:isReferencedBy restriction to Dataset class
- `development/13/TBOX.ttl` - Added dcterms:isReferencedBy property definition and restriction to MediaObject class

**Rationale**:
Ensures consistent citation modeling across all resource types (Document, SemanticArtefact, MediaObject, Dataset) allowing any resource to be referenced by scholarly documents.

**Author**: Alessandro Bertozzi

---

### 2025-12-05 - Refactoring: Remove Producer Role

**Type**: Refactoring

**Description**:
Removed the "producer" role from the ontology across all SAMOD iterations to simplify the role model.

**Details**:
- **Iteration 03**: Removed `schema:producer` object property and `triple:primaryProducer` property; removed associated restrictions on Document class
- **Iteration 13**: Removed `schema:producer` property and restriction on MediaObject class; updated competency questions, glossary, and ABOX examples

**Files Modified**:
- `development/03/TBOX.ttl` - Removed producer property definitions and restrictions
- `development/13/TBOX.ttl` - Removed schema:producer property and MediaObject restriction
- `development/13/glossary-of-terms.md` - Removed schema:producer term definition
- `development/13/informal-competency-questions.md` - Updated CQ_13.6 to remove producer references
- `development/13/formal-competency-questions.md` - Updated CQ_13.6 SPARQL query to exclude producer
- `development/13/ABOX.ttl` - Removed producer instances from multimedia examples

**Rationale**:
Simplified role model by removing the distinction between producer and other content creation roles, maintaining only essential roles like author, publisher, and provider.

**Author**: Alessandro Bertozzi

---

### 2025-11-10 - Extension: New Resource Type Iterations (12-14)

**Type**: Addition

**Description**:
Added three new iterations to extend the ontology beyond documents to other SSH research resource types: Dataset, Multimedia, and Semantic Artefact.

**New Iterations**:
- **Iteration 12**: Dataset - Research datasets as distinct resource type with comprehensive metadata
- **Iteration 13**: Multimedia - Audio-visual and interactive content (images, videos, audio)
- **Iteration 14**: Semantic Artefact - Ontologies, vocabularies, knowledge graphs, and semantic resources

**Details**:

**Iteration 12 - Dataset**:
- Created `triple:Dataset` class as subclass of schema:Dataset
- Properties: title, abstract, version, encoding format, spatial/temporal coverage, keywords, subjects
- Identifier support: DOI, Handle, ID, PID, OriginalIdentifier
- URL support: landing page, download, source
- Access conditions and license information
- Publisher, provider, and funder relationships
- Publication dates and language support
- Added dcterms:isReferencedBy for citation relationships

**Iteration 13 - Multimedia (MediaObject)**:
- Created `triple:MediaObject` class for audio-visual content
- Properties: title, abstract, encoding format, duration, content size
- Media type classification: image, video, audio, interactive
- Comprehensive identifier and URL support
- Creator, publisher, provider roles
- Subject coverage (keywords, topics, spatial, temporal)
- Access conditions and licensing
- Added dcterms:isReferencedBy for citations
- Removed schema:producer role for simplification

**Iteration 14 - Semantic Artefact**:
- Created `triple:SemanticArtefact` class for ontologies and semantic resources
- Properties: title, abstract, version, namespace URI, preferred prefix
- Semantic resource types: ontology, vocabulary, taxonomy, knowledge graph
- Identifier support following DataCite pattern
- URL patterns for landing page, downloadable files, source repositories
- Creator and publisher information
- Subject classification and keywords
- Temporal and spatial coverage
- License and access conditions

**Common Patterns Across Iterations**:
- DataCite identifier pattern for DOI, Handle, ID, PID, OriginalIdentifier
- URL as DataCite identifier (not schema:url)
- Multilingual metadata support (rdf:langString)
- Controlled vocabularies for types, access conditions, licenses, disciplines
- Schema.org alignment for interoperability
- Comprehensive competency questions with SPARQL tests

**Files Created**:
- `development/12/` - Complete Dataset iteration (motivating scenario, CQs, TBOX, ABOX, glossary)
- `development/13/` - Complete MediaObject iteration (motivating scenario, CQs, TBOX, ABOX, glossary)
- `development/14/` - Complete SemanticArtefact iteration (motivating scenario, CQs, TBOX, ABOX, glossary)

**Rationale**:
GoTriple platform aggregates diverse SSH research outputs beyond traditional documents. These iterations provide formal models for datasets, multimedia resources, and semantic artifacts, enabling comprehensive discovery and interoperability.

**Author**: Alessandro Bertozzi

**Commits**:
- ec5e2b0 - "add iteration 14: Semantic Artifacts"
- aa46c64 - "add iterations 13"
- 6ae4307 - "add iteration 12 for Dataset"
- 82c68d3 - "add iterations draft for new class"
- 11b1e57 - "Add new ontology iteration and update existing ontology definitions"

---

### 2025-11-07 - Restructuring: Iterations Planning and Organization

**Type**: Planning

**Description**:
Initial planning and restructuring for iterations 12-16, creating templates and organizational structure for new resource types.

**Details**:
- Drafted iteration structures for Dataset, Multimedia, Semantic Artefact
- Planned CIDOC-CRM alignment iteration
- Removed release and refactoring plan documents (moved to .gitignore)

**Author**: Alessandro Bertozzi

**Commits**:
- b61a757 - "delete release plan"
- ea3722f - "remove refactoring plan and add to .gitignore"

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

**Author**: Alessandro Bertozzi

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

**Author**: Alessandro Bertozzi

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
