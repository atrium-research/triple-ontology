# Motivating Scenario (Iteration 16)

## Name
SKG-IF Alignment - Interoperability with Scientific Knowledge Graphs

## Description

### Context
The GoTriple platform aims to be part of the wider ecosystem of Scientific Knowledge Graphs (SKGs). To ensure interoperability and facilitate data exchange, the TRIPLE ontology must be aligned with the **SKG-IF (Scientific Knowledge Graph Interoperability Framework)**.

### Objective
Formalize the alignment between the core TRIPLE ontology classes and the classes defined in **SKG-O (Science Knowledge Graph Ontology)** and related external vocabularies (FaBiO, FRAPO, FOAF) used by SKG-IF. This is achieved using `skos:exactMatch` and `skos:closeMatch` properties.

## Alignment Specification

The following table defines the official mapping rules for this iteration:

| subject_id | subject_label | subject_source | predicate_id | object_id | object_label | object_source | Mapping Justification | mapping date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **triple:Document** | Document | [Link](https://gotriple.eu/ontology/triple/Document#) | `skos:exactMatch` | `fabio:ScholarlyWork` | Literature | [Link](http://purl.org/spar/fabio/ScholarlyWork) | GoTriple documents contain research literature (articles, books, etc.) | 12/11/2025 |
| **triple:Dataset** | Dataset | [Link](https://gotriple.eu/ontology/triple/Dataset#) | `skos:exactMatch` | `fabio:Dataset` | Research Data | [Link](http://purl.org/spar/fabio/Dataset) | GoTriple datasets match with this class | 12/11/2025 |
| **triple:SemanticArtefact** | Semantic Artefact | [Link](https://gotriple.eu/ontology/triple/SemanticArtefact#) | `skos:closeMatch` | `fabio:Work` | Research product | [Link](http://purl.org/spar/fabio/Work) | No exact correspondence in SKG-O; it consists of a Research Product | 12/11/2025 |
| **triple:MediaObject** | Media Object | [Link](https://gotriple.eu/ontology/triple/MediaObject#) | `skos:closeMatch` | `fabio:Work` | Research product | [Link](http://purl.org/spar/fabio/Work) | No exact correspondence in SKG-O; it consists of a Research Product | 12/11/2025 |
| **triple:Profile** | Profile | [Link](https://gotriple.eu/ontology/triple/Profile#) | `skos:exactMatch` | `foaf:Agent` | Agent | [Link](http://xmlns.com/foaf/0.1/Agent) | foaf:Agent covers both Person and Organisation, which GoTriple doesn't distinguish here | 12/11/2025 |
| **triple:Project** | Project | [Link](https://gotriple.eu/ontology/triple/Project#) | `skos:closeMatch` | `frapo:Grant` | Grant | [Link](http://purl.org/cerif/frapo/Grant) | Some GoTriple projects are not grants (e.g., Citizen Science) | 12/11/2025 |

### Example Scenario
A harvester gathering data from GoTriple needs to understand what a `triple:Dataset` is. By following the `skos:exactMatch` property, the harvester understands that it is equivalent to a `fabio:Dataset`, allowing it to process the data correctly within the SKG-IF compatible system.
