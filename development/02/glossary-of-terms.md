# Glossary of Terms (Iteration 2)

| Term                           | Definition                                                                                                                                                           |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `skos:ConceptScheme`           | A SKOS class representing a controlled vocabulary or concept scheme (e.g., License Vocabulary, Content Type Vocabulary).                                          |
| `skos:Concept`                 | A SKOS class representing a term within a controlled vocabulary.                                                                                                     |
| `skos:inScheme`                | SKOS property linking a concept to the concept scheme (vocabulary) it belongs to.                                                                                   |
| `skos:closeMatch`              | SKOS property indicating that two concepts are sufficiently similar to be used interchangeably in some contexts (e.g., TRIPLE term matched to COAR term).         |
| `skos:exactMatch`              | SKOS property indicating that two concepts can be used interchangeably across all contexts (e.g., TRIPLE term exactly matching Creative Commons URI).              |
| `skos:definition`              | SKOS property providing a human-readable definition or explanation of a concept.                                                                                     |
| `owl:imports`                  | OWL property used to include external vocabulary modules into the main ontology, enabling modular vocabulary management.                                            |
| **License Vocabulary**         | A controlled vocabulary (`skos:ConceptScheme`) containing standardized terms for document licenses (e.g., CC-BY-4.0, CC0, All Rights Reserved).                    |
| **Access Conditions Vocabulary** | A controlled vocabulary (`skos:ConceptScheme`) containing standardized terms for access conditions (e.g., Open Access, Restricted Access, Embargoed).            |
| **Content Type Vocabulary**   | A controlled vocabulary (`skos:ConceptScheme`) containing standardized terms for content types (e.g., Article, Dataset, Book, Thesis, Conference Proceeding).    |
| **Discipline Vocabulary**      | A controlled vocabulary (`skos:ConceptScheme`) containing standardized terms for academic disciplines (e.g., Digital Humanities, Linguistics, History, Sociology). |
| `schema:license`               | Schema.org property linking a document to its license term from the License Vocabulary.                                                                            |
| `schema:conditionsOfAccess`    | Schema.org property linking a document to its access conditions term from the Access Conditions Vocabulary.                                                        |
| `schema:additionalType`        | Schema.org property linking a document to its content type term from the Content Type Vocabulary, providing enhanced classification and external vocabulary alignment. |
| `sioc:topic`                   | SIOC property linking a document to one or more discipline terms from the Discipline Vocabulary.                                                                   |
| `triple:Document`              | A TRIPLE class representing documents in the GoTriple platform, subclass of `schema:CreativeWork` and `foaf:Document`.                                            |
| **External Entity**            | A concept from an external vocabulary or classification system (e.g., COAR, Creative Commons, Library of Congress Subject Headings, UNESCO Thesaurus).            |
| **COAR**                       | Confederation of Open Access Repositories - provides standard vocabularies for resource types and access rights.                                                   |
| **LCSH**                       | Library of Congress Subject Headings - authoritative list of subjects and disciplines.                                                                              |
