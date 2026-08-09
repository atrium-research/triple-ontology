# Glossary of Terms (Iteration 8)

| Term                      | Definition                                                                                                                                                  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `datacite:Identifier`     | Base class for all identifiers following DataCite specification.                                                                                           |
| `datacite:IdentifierScheme` | A standardized system for creating and managing identifiers in DataCite.                                                                                 |
| `datacite:doi` | Identifier scheme: DOI — Digital Object Identifier for digital objects. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:issn` | Identifier scheme: ISSN — International Standard Serial Number for serial publications. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:isbn` | Identifier scheme: ISBN — International Standard Book Number for books. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:handle` | Identifier scheme: Handle — persistent identifier system for digital objects. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:ark`              | The identifier scheme instance representing the Archival Resource Key (ARK) system.                                                                         |
| `hasIdentifier`           | The property connecting a document to its identifiers (`datacite:hasIdentifier`).                                                                           |
| `usesIdentifierScheme`    | The property connecting an identifier to its scheme (`datacite:usesIdentifierScheme`).                                                                      |
| `hasLiteralValue`         | The property connecting an identifier to its string value (`litre:hasLiteralValue`).                                                                        |
| `Document`                | An entity representing any type of resource available on the GoTriple platform.                                                                             |
