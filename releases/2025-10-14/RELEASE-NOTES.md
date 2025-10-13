# TRIPLE Ontology v1.0.0

**Release Date**: 2025-01-15

## Overview

Initial public release of the TRIPLE ontology developed through 7 SAMOD iterations.

## What's Included

### Core Ontology
- Document modeling (publications, datasets, etc.)
- Project modeling (SSH research projects)
- Agent modeling (persons and organizations)
- Role-based relationships with temporal information
- Identifier management with multiple schemes
- Subject coverage (temporal, spatial, keywords)
- Duplicate handling (document clusters)
- Author disambiguation and profiles
- Discarding mechanism for unusable data

### Controlled Vocabularies
- Licenses vocabulary
- Access conditions vocabulary
- Document types vocabulary (COAR-aligned)
- Disciplines vocabulary
- Identifier schemes vocabulary

### Documentation
- Complete HTML documentation
- Graffoo diagrams
- SPARQL competency questions

## Iterations Summary

1. **Iteration 01**: Document basics (types, languages, identifiers, metadata)
2. **Iteration 02**: Controlled vocabularies (license, access conditions, document types, disciplines)
3. **Iteration 03**: Document roles (author, contributor, publisher, provider, funder, etc.)
4. **Iteration 04**: Subject coverage (temporal, spatial, keywords)
5. **Iteration 05**: Duplicate handling and discarded entities
6. **Iteration 06**: Author profiles and user accounts
7. **Iteration 07**: Projects (SSH research projects with metadata, roles, subjects)

## External Alignments

- **FOAF**: Document and agent modeling
- **Dublin Core**: Metadata properties
- **DataCite**: Identifier modeling
- **Schema.org**: Language, grants, general properties
- **SKOS**: Controlled vocabularies
- **SPAR Ontologies**: PRO (roles), LiTeRe (literals)
- **COAR**: Resource type vocabulary
- **SPDX**: License vocabulary

## Files

- `serializations/` - Ontology in multiple formats (.ttl, .rdf, .owl, .jsonld, .nt)
- `vocabularies/` - Controlled vocabulary modules
- `documentation/` - HTML docs and diagrams

## Notes

This is the first stable release based on the complete SAMOD development process documented in the `development/` directory.
