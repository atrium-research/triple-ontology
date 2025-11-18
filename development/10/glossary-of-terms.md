# Glossary of Terms (Iteration 10)

| Term                      | Definition                                                                                                                                                  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `datacite:Identifier`     | Base class for all identifiers following DataCite specification.                                                                                           |
| `datacite:IdentifierScheme` | A standardized system for creating and managing identifiers in DataCite.                                                                                 |
| `triple:DOI`              | DOI identifier class - Digital Object Identifier for digital objects, subclass of `datacite:Identifier`.                                                  |
| `datacite:doi`              | The identifier scheme instance representing the DOI system.                                                                                                 |
| `triple:ISSN`             | ISSN identifier class - International Standard Serial Number for serial publications, subclass of `datacite:Identifier`.                                  |
| `datacite:issn`             | The identifier scheme instance representing the ISSN system.                                                                                                |
| `triple:ISBN`             | ISBN identifier class - International Standard Book Number for books, subclass of `datacite:Identifier`.                                                   |
| `datacite:isbn`             | The identifier scheme instance representing the ISBN system.                                                                                                |
| `triple:Handle`           | Handle identifier class - persistent identifier system for digital objects, subclass of `datacite:Identifier`.                                            |
| `datacite:handle`           | The identifier scheme instance representing the Handle system.                                                                                              |
| `hasIdentifier`           | The property connecting a document to its identifiers (`datacite:hasIdentifier`).                                                                           |
| `usesIdentifierScheme`    | The property connecting an identifier to its scheme (`datacite:usesIdentifierScheme`).                                                                      |
| `hasLiteralValue`         | The property connecting an identifier to its string value (`litre:hasLiteralValue`).                                                                        |
| `Document`                | An entity representing any type of resource available on the GoTriple platform.                                                                             |
