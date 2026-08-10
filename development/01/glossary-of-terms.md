# Glossary of Terms (Iteration 1)

| Term                    | Definition                                                                                                                                                                                                        |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `triple:Document`       | A document in the GoTriple platform, representing scholarly publications, research datasets, and other SSH research artifacts. Subclass of `schema:CreativeWork` and `foaf:Document`.                           |
| `schema:CreativeWork`   | A creative work from Schema.org vocabulary, representing the most generic kind of creative work, including books, movies, photographs, software programs, etc.                                                  |
| `foaf:Document`         | A document from FOAF (Friend of a Friend) vocabulary, representing a document or resource.                                                                                                                       |
| `datacite:Identifier`   | An identifier associated with the document following DataCite specification.                                                                                                                                     |
| `triple:internal_id_schema` | Identifier scheme of the internal identifier assigned by the GoTriple platform. |
| `datacite:ark` | Identifier scheme of the persistent identifier minted by GoTriple: an ARK. |
| `triple:original_id_schema` | Generic identifier scheme for the identifier a resource carried in the system it was harvested from. |
| `schema:Language`       | The language in which the document was produced, using Schema.org vocabulary.                                                                                                                                     |
| `skos:Concept`          | A concept from SKOS vocabulary representing the type of the document.                                                                                                                                             |
| `schema:headline`       | Data property representing the title of the document, available in multiple languages as `rdf:langString`.                                                                                                        |
| `schema:abstract`       | Data property representing the abstract or summary of the document, available in multiple languages as `rdf:langString`.                                                                                          |
| `schema:encodingFormat` | Data property representing the file format (MIME type) of the document, such as "application/pdf" or "text/html".                                                                                                 |
| `schema:datePublished`  | Data property representing the date of first publication of the document, normalized to ISO 8601 (`xsd:date`).                                                                                                    |
| `schema:dateModified`   | Data property representing the date on which the document record was most recently modified in the GoTriple index (`xsd:date`).                                                                                   |
| `dcterms:source`        | Property indicating the source of the document. Here used broadly to indicate a reference or mention of another entity.                                                                                           |
| `triple:landing_page_url_schema` | IdentifierScheme for landing page URLs containing metadata and descriptive information about the document.                                                                                            |
| `triple:full_text_url_schema`    | IdentifierScheme for URLs providing direct access to the full content of the document.                                                                                                                    |
| `triple:source_url_schema`       | IdentifierScheme for URLs of the original publication location or source repository.                                                                                                                      |
| `triple:internal_id_schema`      | IdentifierScheme for internal identifiers used within the GoTriple platform for document management.                                                                                                     |
| `datacite:ark`                   | IdentifierScheme of the Archival Resource Key, used for the persistent identifiers minted and exposed externally by the GoTriple platform.                                                               |
| `triple:original_id_schema`      | IdentifierScheme for original identifiers from the source system where the document was harvested.                                                                                                       |
| `datacite:doi` | Identifier scheme for the Digital Object Identifier (ISO 26324). |
| `datacite:handle` | Identifier scheme for the Handle System, on top of which the DOI system is built. |
| `datacite:issn` | Identifier scheme for the International Standard Serial Number (ISO 3297). |
| `schema:inLanguage` | The language of the content, from Schema.org. Values are `schema:Language` individuals identified by their ISO-639-1 code. |
| `datacite:hasIdentifier` | Links an entity to one of its identifiers. Every identifier in the TRIPLE ontology is reached through this property and is a `datacite:Identifier`: there is no other way of attaching an identifier to an entity. |
| `datacite:usesIdentifierScheme` | Links an identifier to the scheme it belongs to. The scheme is what tells one kind of identifier from another. |
| `datacite:IdentifierScheme` | The scheme an identifier belongs to, from the DataCite ontology. |
| `litre:hasLiteralValue` | The literal value of an identifier, from the SPAR literal reification ontology. |
