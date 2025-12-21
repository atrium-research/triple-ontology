# Glossary of Terms (Iteration 16)

## External Classes

### fabio:ScholarlyWork
**Definition**: A scholarly work.
**Source**: [FaBiO Ontology](http://purl.org/spar/fabio/ScholarlyWork)
**Alignment**: `skos:exactMatch` with `triple:Document`.

### fabio:Dataset
**Definition**: A dataset.
**Source**: [FaBiO Ontology](http://purl.org/spar/fabio/Dataset)
**Alignment**: `skos:exactMatch` with `triple:Dataset`.

### fabio:Work
**Definition**: A work.
**Source**: [FaBiO Ontology](http://purl.org/spar/fabio/Work)
**Alignment**: `skos:closeMatch` with `triple:SemanticArtefact` and `triple:MediaObject`.

### frapo:Grant
**Definition**: A funding grant.
**Source**: [FRAPO Ontology](http://purl.org/cerif/frapo/Grant)
**Alignment**: `skos:closeMatch` with `triple:Project`.

### foaf:Agent
**Definition**: An agent (person or organization).
**Source**: [FOAF Vocabulary](http://xmlns.com/foaf/0.1/Agent)
**Alignment**: `skos:exactMatch` with `triple:Profile`.

## Properties

### skos:exactMatch
**Definition**: skos:exactMatch is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications.

### skos:closeMatch
**Definition**: skos:closeMatch is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.
