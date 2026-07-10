# Motivating Scenario (Iteration 17)

## Name
Original Provider Values - Provenance of Harvested Metadata

## Description

### Context
The GoTriple platform aggregates research artifacts from many heterogeneous SSH sources through its data processing pipeline (SCRE). During ingestion, several metadata fields are **normalized**: the resource type is mapped to the Content Type controlled vocabulary, the language is resolved to a `schema:Language` entity, dates are converted to ISO 8601, and licenses and access conditions are mapped to the License and Access Condition controlled vocabularies.

The values **as originally received from the provider** are however preserved by the platform, because they carry provenance information that the normalized values lose: they document what the source actually said, they allow the normalization to be audited and re-run, and they let data consumers detect mapping errors (e.g. a raw `info:eu-repo/semantics/openAccess` mapped to the wrong access condition).

The current ontology (up to iteration 16) models only the normalized values. This iteration completes the model with the raw, pre-normalization values (issue [#38](https://github.com/atrium-research/triple-ontology/issues/38), second checklist item).

### Objective
Introduce five datatype properties that preserve the original provider values on `triple:Document`:

- `triple:originalType` - the resource type string as received (e.g. `journalArticle`, `COAR text`)
- `triple:originalLanguage` - the language value as received (e.g. `eng`, `English`, `fr-FR`)
- `triple:originalDatePublished` - the publication date string as received, in whatever format the provider used (e.g. `03/05/2021`, `May 2021`)
- `triple:originalLicense` - the license statement as received (e.g. `CC BY 4.0`, a URL, free text)
- `triple:originalConditionsOfAccess` - the access rights statement as received (e.g. `info:eu-repo/semantics/openAccess`)

## Technical Specification
- All five properties are `owl:DatatypeProperty` with range `xsd:string`: raw values are kept verbatim, so no datatype or vocabulary constraint applies.
- **Hybrid sub-property pattern**: each property is declared `rdfs:subPropertyOf` the corresponding Dublin Core *Elements 1.1* term (`dc:type`, `dc:language`, `dc:date`, `dc:rights`), following the same reuse-by-subsumption approach already used for `triple:hasLicense ⊑ dcterms:license` and `triple:hasContentType ⊑ dcterms:type`. DC Elements is chosen over DCMI Terms because its properties have no range constraints and are the de-facto standard for raw harvested metadata (OAI-PMH `oai_dc`); a generic Dublin Core consumer therefore sees the raw values through the standard `dc:` terms by inference.
- `triple:originalLicense` and `triple:originalConditionsOfAccess` are both sub-properties of `dc:rights` (DC Elements does not distinguish the two notions); the TRIPLE properties preserve the distinction.
- The normalized counterparts remain on the existing properties: `triple:hasContentType`, `schema:inLanguage`, `schema:datePublished`, `triple:hasLicense`, `triple:hasAccessCondition`.
- The properties are optional (0 or more) on `triple:Document`, expressed as `owl:allValuesFrom xsd:string` restrictions, consistent with the style of the other iterations.

## Examples
- A document harvested from an Italian repository arrives with type `journalArticle`, language `eng`, publication date `03/05/2021`, license `CC BY 4.0` and access rights `info:eu-repo/semantics/openAccess`. The pipeline normalizes these to `ContentType/article`, an English `schema:Language`, `"2021-05-03"^^xsd:date`, `License/creative_commons` and `AccessCondition/open_access`, while the five raw strings are preserved on the document.
- A document from another source arrives with only a raw type (`COAR text`) and raw access rights (`restricted`); the other original fields are absent. Only the corresponding original properties are asserted.
