# Glossary of Terms - Iteration 12

## Semantic Artefact Resource Type

| Term | Definition |
|------|------------|
| `schema:ContactPoint` | A contact point for a person or organization providing information about the semantic artifact. |
| `mod:SemanticArtefact` | A semantic artifact from the MOD ontology representing formal knowledge representations. |
| `triple:SemanticArtefact` | A structured knowledge representation such as an ontology, vocabulary, taxonomy, or concept scheme used in SSH research, extending mod:SemanticArtefact. |
| `schema:contactPoint` | A relationship linking the semantic artifact to contact information for administrative purposes. |
| `schema:creativeWorkStatus` | The lifecycle status of the semantic artifact (e.g., draft, published, deprecated). |
| `schema:abstract` | An abstract or summary describing the semantic artifact's purpose and content. |
| `schema:headline` | The primary title or name of the semantic artifact. |
| `schema:datePublished` | The date when the semantic artifact was first published or made available. |
| `schema:dateModified` | The date when the semantic artifact was last modified or updated. |
| `schema:version` | A version identifier for the semantic artifact indicating its evolution or revision. |
| `schema:fileFormat` | The physical file format expressed as a MIME type (e.g., application/rdf+xml, text/turtle, application/zip). |
| `schema:encodingFormat` | The media type of the artefact, typically expressed as a MIME type (e.g. `application/rdf+xml`, `text/turtle`). The representation technique — SKOS, OWL — is a separate property, `adms:representationTechnique`. |
| `schema:keywords` | Keywords or tags used to describe the semantic artifact content. |
| `dcterms:isReferencedBy` | A related resource that references, cites, or otherwise points to the semantic artifact. |
| `triple:internal_id_schema` | Identifier scheme of the internal identifier assigned by the GoTriple platform. |
| `datacite:ark` | Identifier scheme of the persistent identifier minted by GoTriple: an ARK. |
| `triple:original_id_schema` | Generic identifier scheme for the identifier a resource carried in the system it was harvested from. |
| `datacite:doi` | Identifier scheme: DOI — Digital Object Identifier for semantic artifacts. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:handle` | Identifier scheme: Handle — persistent identifier system for semantic artifacts. Identifiers using it are plain `datacite:Identifier`. |
| `datacite:uri` | Identifier scheme: URI — Uniform Resource Identifier for semantic artifacts (ontologies, vocabularies). Identifiers using it are plain `datacite:Identifier`. |
| `datacite:Identifier` | Base class for all identifiers following DataCite specification. |
| `datacite:IdentifierScheme` | A standardized system for creating and managing identifiers in DataCite. |
| `datacite:hasIdentifier` | DataCite property connecting semantic artifacts to their identifiers. |
| `datacite:usesIdentifierScheme` | DataCite property connecting identifiers to their schemes, always asserted explicitly in the data. |
| `litre:hasLiteralValue` | Property connecting identifiers to their string values. |
| `triple:License` | Bridge class for licenses, subclass of skos:Concept and dcterms:LicenseDocument. |
| `triple:ConditionOfAccess` | Bridge class for access rights, subclass of skos:Concept and dcterms:RightsStatement. |
| `triple:hasLicense` | Property connecting a semantic artifact to its license. |
| `triple:hasConditionOfAccess` | Property connecting a semantic artifact to its access conditions. |
| `adms:representationTechnique` | ADMS property giving more information about the format in which the semantic artefact is released (e.g. SKOS, OWL), distinct from the file format. Range `skos:Concept`. |
| `schema:mentions` | Schema.org property indicating that the semantic artefact contains a reference to, but is not necessarily about, a concept or entity. |
| `schema:contributor` | A secondary contributor to the creative work, from Schema.org. |
| `schema:publisher` | The publisher of the creative work, from Schema.org. |
