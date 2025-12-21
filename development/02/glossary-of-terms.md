# Glossary of Terms (Iteration 2)

| Term                           | Definition                                                                                                                                                           |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `skos:Concept`                 | A SKOS class representing a term within a controlled vocabulary.                                                                                                     |
| `skos:closeMatch`              | SKOS property indicating that two concepts are sufficiently similar to be used interchangeably in some contexts (e.g., TRIPLE term matched to COAR term).         |
| `skos:exactMatch`              | SKOS property indicating that two concepts can be used interchangeably across all contexts (e.g., TRIPLE term exactly matching Creative Commons URI).              |
| `skos:definition`              | SKOS property providing a human-readable definition or explanation of a concept.                                                                                     |
| `owl:imports`                  | OWL property used to include external vocabulary modules into the main ontology, enabling modular vocabulary management.                                            |
| `triple:License`               | Bridge class. Subclass of `skos:Concept` and `dcterms:LicenseDocument`. Used for license terms.                                                                      |
| `triple:AccessCondition`       | Bridge class. Subclass of `skos:Concept` and `dcterms:RightsStatement`. Used for access condition terms.                                                             |
| `triple:ContentType`           | Bridge class. Subclass of `skos:Concept`. Used for content type terms.                                                                                               |
| `triple:Discipline`            | Bridge class. Subclass of `skos:Concept`. Used for discipline terms.                                                                                                 |
| `triple:hasLicense`            | Property linking a document to a `triple:License`. Subproperty of `dcterms:license`.                                                                                 |
| `triple:hasAccessCondition`    | Property linking a document to a `triple:AccessCondition`. Subproperty of `dcterms:accessRights`.                                                                    |
| `triple:hasContentType`        | Property linking a document to a `triple:ContentType`. Subproperty of `dcterms:type`.                                                                                |
| `sioc:topic`                   | Property linking a document to a `triple:Discipline`. Subproperty of `dcterms:subject`.                                                                              |
| `triple:Document`              | A TRIPLE class representing documents in the GoTriple platform, subclass of `schema:CreativeWork` and `foaf:Document`.                                            |
| **External Entity**            | A concept from an external vocabulary or classification system (e.g., COAR, Creative Commons, Library of Congress Subject Headings, UNESCO Thesaurus).            |
| **COAR**                       | Confederation of Open Access Repositories - provides standard vocabularies for resource types and access rights.                                                   |
| **LCSH**                       | Library of Congress Subject Headings - authoritative list of subjects and disciplines.                                                                              |
