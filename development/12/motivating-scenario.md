# Motivating Scenario - Iteration 12

## Name
Extension of Resource Types: Semantic Artefact

## General Description
The GoTriple discovery platform needs to support semantic artifacts as a distinct resource type within the Social Sciences and Humanities domain. Semantic artifacts include ontologies, vocabularies, taxonomies, concept schemes, and other structured knowledge representations that are increasingly important in SSH research workflows. These resources require specialized metadata fields that distinguish them from traditional documents and datasets.

The platform must integrate with various semantic artifact repositories including OntoPortal instances, SKOSMOS platforms, and MOD-API compliant catalogs. This integration enables researchers to discover, evaluate, and reuse semantic artifacts for their research projects, facilitating better knowledge organization and interoperability in SSH domains.

This iteration extends the TRIPLE ontology to support semantic artifacts following standards like ADMS (Asset Description Metadata Schema), MOD 3.0 (Metadata Vocabulary for Ontology Description and Publication), and DCAT (Data Catalog Vocabulary). The focus is on administrative and publishing metadata that provides context about version control, status, publication lifecycle, and technical characteristics of semantic artifacts.

## Technical Specification
- Extend TRIPLE ontology with properties specific to semantic artifacts following ADMS and MOD 3.0 standards
- Support for multilingual titles and abstracts using rdf:langString
- Integration with Schema.org properties for publishing metadata (version, status, contact)
- Administrative metadata for lifecycle management including creation, publication, and modification dates
- Publisher and aggregator relationships with proper Organization/Person entity modeling
- Language specification with ISO 639 language code support
- Format and representation technique metadata using MIME types and encoding standards
- Status tracking for semantic artifact lifecycle stages
- Status tracking for semantic artifact lifecycle stages
- Contact point information for administrative queries
- Support for license and access conditions using Bridge Classes (`triple:License`, `triple:AccessCondition`)

## Examples
- Ontology repositories from OntoPortal with version control, publisher information, and status tracking
- SKOS vocabularies with multilingual abstracts, contributor details, and format specifications
- Taxonomy artifacts with administrative contact information, aggregator metadata, and representation technique details
- Concept schemes with publication lifecycle metadata, language variants, and technical format information
