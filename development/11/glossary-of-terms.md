# Glossary of Terms (Iteration 11)

| Term                           | Definition                                                                                                                                          |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `schema:MediaObject`           | Schema.org class representing a media object such as an image, video, or audio object embedded in a web page or downloadable dataset.              |
| `triple:MediaObject`           | GoTriple class representing multimedia objects in the platform, extending schema:MediaObject with platform-specific semantics for all media types. |
| `schema:headline`              | Schema.org property specifying the headline or title of the creative work.                                                                          |
| `schema:abstract`              | Schema.org property providing an abstract or short description that summarizes a CreativeWork.                                                      |
| `schema:author`                | Schema.org property indicating the author of the content or creative work.                                                                          |
| `schema:contributor`           | Schema.org property indicating a secondary contributor to the creative work or event.                                                               |
| `schema:dateCreated`           | Schema.org property specifying the date on which the creative work was created.                                                                     |
| `schema:datePublished`         | Schema.org property specifying the date of first publication or broadcast.                                                                          |
| `schema:dateModified`          | Schema.org property specifying the date on which the creative work was most recently modified.                                                      |
| `schema:publisher`             | Schema.org property indicating the publisher of the creative work.                                                                                  |
| `schema:provider`              | Schema.org property indicating the service provider or aggregator of the content.                                                                   |
| `schema:encodingFormat`        | Schema.org property specifying the media type using MIME format (e.g., video/mp4, audio/mp3).                                                       |
| `schema:duration`              | Schema.org property specifying the duration of multimedia content in ISO 8601 format (e.g., PT1H25M30S for 1 hour, 25 minutes, 30 seconds).      |
| `schema:size`                  | Schema.org property specifying the size of a digital product or creative work.                                                                      |
| `Multimedia Content`           | Digital media files including video, audio, and image content indexed in the GoTriple platform for SSH research.                                   |
| `Technical Metadata`           | Multimedia-specific metadata including duration, file size, encoding format, and resolution.                                                        |
| `MIME Type`                    | Media type specification for multimedia files (e.g., video/mp4, audio/mp3, image/tiff) used in `schema:encodingFormat`.                           |
| `ISO 8601 Duration`            | Standard format for expressing time durations (PT[hours]H[minutes]M[seconds]S).                                                                     |
| `OAI-PMH`                      | Open Archives Initiative Protocol for Metadata Harvesting, used for extracting multimedia metadata from repositories.                              |
| `schema:keywords`              | Schema.org object property linking multimedia content to defined terms that describe the content topics.                                            |
| `schema:DefinedTerm`           | Schema.org class representing a word, name, acronym, phrase, etc. with a formal definition used to describe multimedia content.                     |
| `triple:internal_id_schema` | Identifier scheme of the internal identifier assigned by the GoTriple platform. |
| `datacite:ark` | Identifier scheme of the persistent identifier minted by GoTriple: an ARK. |
| `triple:original_id_schema` | Generic identifier scheme for the identifier a resource carried in the system it was harvested from. |
| `datacite:doi` | Identifier scheme: DOI — Digital Object Identifier for multimedia objects. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:handle` | Identifier scheme: Handle — persistent identifier system for multimedia objects. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:Identifier`          | Base class for all identifiers following DataCite specification.                                                                                    |
| `datacite:IdentifierScheme`    | A standardized system for creating and managing identifiers in DataCite.                                                                            |
| `datacite:hasIdentifier`       | DataCite property connecting multimedia objects to their identifiers.                                                                               |
| `datacite:usesIdentifierScheme`| DataCite property connecting identifiers to their schemes, always asserted explicitly in the data.                                          |
| `litre:hasLiteralValue`        | Property connecting identifiers to their string values.                                                                                             |
