# Glossary of Terms (Iteration 3)

| Term                    | Definition                                                                                                                                                            |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `triple:Document`       | A document in the GoTriple platform, representing scholarly publications, research datasets and other SSH research artefacts. Subclass of `schema:CreativeWork` and `foaf:Document`. |
| `triple:aggregator`     | Links a document to the organization that collated it from several sources into GoTriple. Minted in the TRIPLE namespace because no standard vocabulary has this role. |
| `schema:author`         | The agent primarily responsible for the content of the document, from Schema.org.                                                                                      |
| `schema:contributor`    | A secondary contributor to the document, from Schema.org: someone who took part without being its primary author.                                                     |
| `schema:publisher`      | The agent responsible for publishing and disseminating the document, from Schema.org.                                                                                  |
| `schema:provider`       | The agent that makes the document available to GoTriple, from Schema.org. It may differ from the publisher when the document is harvested from a third-party repository. |
| `schema:contactPoint`   | Links the document to the contact point designated for it, from Schema.org.                                                                                            |
| `schema:ContactPoint`   | A contact point for a person or an organization, from Schema.org.                                                                                                      |
| `schema:name`           | The name of an agent, from Schema.org.                                                                                                                                 |
| `schema:email`          | The e-mail address of a contact point, from Schema.org.                                                                                                                |
| `schema:datePublished`  | The date of first publication of the document, from Schema.org.                                                                                                        |
| `schema:CreativeWork`   | A creative work, from Schema.org. Superclass of `triple:Document`.                                                                                                     |
| `foaf:Document`         | A document, from FOAF. Superclass of `triple:Document`.                                                                                                                |
| `foaf:Person`           | A person, from FOAF. One of the two kinds of agent that can hold a role on a document.                                                                                 |
| `foaf:Organization`     | An organization, from FOAF. The other kind of agent that can hold a role on a document.                                                                                |
