# Motivating Scenario - Iteration 10

## Name
Extension of Resource Types: Dataset

## General Description
The GoTriple platform needs to index and represent research datasets from various sources including institutional repositories, data catalogs, and geospatial data platforms. These datasets represent a distinct type of scholarly resource with specific metadata requirements including spatial coverage, temporal coverage, distribution information, and format specifications. The platform must accommodate datasets from different standards (DCAT, GeoDCAT, OGC CSW, ISO 19115) while providing a unified semantic representation.

## Technical Specification
- Extend the ontology to support `triple:Dataset` as a primary resource type (subclass of schema:Dataset)
- Map dataset-specific properties from multiple standards (DCAT, GeoDCAT, ISO 19115, OGC CSW)
- Support both georeferenced and non-georeferenced datasets
- Include comprehensive metadata for discovery, access, and reuse
- Maintain compatibility with existing Document and Project models
- Support distribution and access information for data files (`dcat:distribution`, `dcat:Distribution`)
- Support contact point information for administrative queries (schema:ContactPoint)

## Examples
- Research datasets from institutional repositories
- Geospatial datasets from Geonetwork platforms
- Open data from government catalogs
- Scientific datasets with DOI identifiers
- Multi-format dataset distributions with different access methods
