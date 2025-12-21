# Motivating Scenario (Iteration 13)

## Name
CIDOC-CRM and SSHOC-RO Alignment

## Description

### Context
To enhance the interoperability of the TRIPLE ontology within the cultural heritage and social sciences domains, it is necessary to align core classes with **CIDOC-CRM** (a standard for cultural heritage information) and **SSHOC-RO** (Social Sciences and Humanities Open Cloud Reference Ontology).

### Objective
Implement intensional mappings using `skos:exactMatch` and `skos:closeMatch` to link TRIPLE classes with their equivalents in CIDOC-CRM and SSHOC-RO.

## Alignment Specification

The following mappings are implemented:

| TRIPLE Class | Predicate | External Class | Ontology |
| --- | --- | --- | --- |
| **triple:Document** | `skos:exactMatch` | `E31 Document` | CIDOC-CRM |
| **triple:Document** | `skos:exactMatch` | `SHE8 Publication` | SSHOC-RO |
| **triple:Project** | `skos:closeMatch` | `E7 Activity` | CIDOC-CRM |
| **triple:Project** | `skos:exactMatch` | `SHE3 SSH Project` | SSHOC-RO |
| **triple:Dataset** | `skos:exactMatch` | `SHE1 Dataset` | SSHOC-RO |
| **triple:MediaObject** | `skos:closeMatch` | `E90 Symbolic Object` | CIDOC-CRM |
| **triple:SemanticArtefact** | `skos:closeMatch` | `E90 Symbolic Object` | CIDOC-CRM |

### Note on Mapping
These mappings follow the pattern defined in the ICON ontology for comprehensive artistic interpretations, serving both documentation purposes and query-time data integration.
