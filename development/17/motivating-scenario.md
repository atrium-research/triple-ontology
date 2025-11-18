# Motivating Scenario - Iteration 17

## Name
External Ontology Alignment for Project Relationships and Citation Networks

## General Description
The GoTriple platform needs to align its research artifact relationships with established semantic web standards to improve interoperability and data exchange with other research infrastructure systems. This iteration focuses on aligning project relationships and citation patterns with widely adopted ontologies in the scholarly communication domain.

Specifically, the platform requires:
1. **Project Output Relationships**: Documents, SemanticArtefacts, MediaObjects, and Datasets should be formally linked to their originating research projects using standardized properties
2. **Citation and Reference Networks**: SemanticArtefacts, MediaObjects, and Datasets should use standardized properties to express reverse citation relationships

The alignment with FRAPO (Funding, Research Administration and Projects Ontology) for project relationships and Dublin Core Terms for bibliographic relationships ensures compatibility with CRIS (Current Research Information Systems), institutional repositories, and other scholarly data platforms.

## Technical Specification
- Use `frapo:isOutputOf` property for Document, SemanticArtefact, MediaObject, and Dataset classes to link to their originating projects
- Use `dcterms:isReferencedBy` property for SemanticArtefact, MediaObject, and Dataset classes to express citation relationships
- Maintain existing class definitions and restrictions while adding standardized property constraints
- Ensure compatibility with existing SAMOD iterations and consolidated ontology structure
- Add FRAPO and Dublin Core Terms namespace support

## Examples
- A research paper (Document) produced as output of an EU Horizon project
- A digital humanities dataset (Dataset) created within a national research project
- An ontology (SemanticArtefact) developed as deliverable of an academic project
- Audio recordings (MediaObject) collected during fieldwork funded by a research grant
- Cross-references between semantic artifacts and their citing documents