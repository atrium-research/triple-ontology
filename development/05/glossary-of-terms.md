# Glossary of Terms (Iteration 5)

| Term                        | Definition                                                                                                                                                   |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `triple:Document`           | A document in the GoTriple platform: scholarly publications, research datasets and other SSH research artefacts. Subclass of `schema:CreativeWork` and `foaf:Document`. |
| `triple:Cluster`            | A group of documents coming from different sources that represent the same scholarly work, used for deduplication. A cluster is computed by GoTriple, so it carries only its internal identifier. |
| `triple:inCluster`          | Associates a document with the cluster it belongs to. A document belongs to exactly one cluster.                                                              |
| `triple:isDiscarded`        | Boolean flag stating whether an author or a keyword has been marked as discarded and must not be used for search and filtering.                               |
| `triple:internal_id_schema` | Identifier scheme of the internal identifier assigned by the GoTriple platform, the only identifier a cluster carries.                                        |
| `triple:original_id_schema` | Identifier scheme of the identifier a document carried in the system it was harvested from.                                                                  |
| `datacite:ark`              | Identifier scheme of the persistent identifier minted by GoTriple: an ARK.                                                                                   |
| `datacite:Identifier`       | An identifier of an entity, from the DataCite ontology. It carries exactly one scheme and one literal value.                                                  |
| `datacite:IdentifierScheme` | The scheme an identifier belongs to, from the DataCite ontology. The scheme is what tells one kind of identifier from another.                                |
| `datacite:hasIdentifier`    | Links an entity to one of its identifiers, from the DataCite ontology.                                                                                       |
| `datacite:usesIdentifierScheme` | Links an identifier to the scheme it uses, from the DataCite ontology.                                                                                   |
| `litre:hasLiteralValue`     | The literal value of an identifier, from the SPAR literal reification ontology.                                                                               |
| `schema:CreativeWork`       | A creative work, from Schema.org. Superclass of `triple:Document`.                                                                                            |
| `schema:DefinedTerm`        | A word, name, acronym or phrase defined in a controlled vocabulary, from Schema.org. Used here for the keywords of a document.                                |
| `schema:author`             | The author of a content, from Schema.org.                                                                                                                     |
| `schema:keywords`           | The keywords describing a content, from Schema.org.                                                                                                           |
| `foaf:Document`             | A document, from FOAF. Superclass of `triple:Document`.                                                                                                       |
| `foaf:Person`               | A person, from FOAF. Used here for the authors of a document.                                                                                                 |
