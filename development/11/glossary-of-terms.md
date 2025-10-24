# Glossary of Terms (Iteration 11)

| Term                  | Definition                                                                                                                                          |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `mentions`            | A property indicating that a document contains a reference to or mentions another entity (`schema:mentions`).                                       |
| `schema:mentions`     | Schema.org property connecting a CreativeWork to an entity it mentions or references.                                                               |
| `schema:CreativeWork` | Schema.org class representing creative works such as documents, articles, books, etc.                                                               |
| `schema:Thing`        | The most generic Schema.org class, representing anything that can be mentioned.                                                                     |
| `triple:Document`     | A document in the GoTriple platform, representing scholarly publications, research datasets, and other SSH research artifacts. Subclass of `schema:CreativeWork` and `foaf:Document`. |
| `foaf:Document`       | FOAF vocabulary class for documents (parent class of `triple:Document`).                                                                           |
| `Person`              | An individual person, such as a researcher or scholar (`foaf:Person`).                                                                              |
| `Project`             | A research project or initiative (`schema:Project`).                                                                                                |
| `Organization`        | An institution, research center, university, or other organizational entity (`foaf:Organization`).                                                  |
| `Citation`            | A mention of one document by another, typically in bibliographic references (modeled as `schema:mentions` between documents).                       |
| `Reference`           | A general mention or reference to any entity within a document's content.                                                                           |
| `Mention network`     | The graph of relationships created by documents mentioning various entities, forming a network of scholarly connections.                            |
