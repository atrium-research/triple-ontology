# Motivating Scenario (Iteration 17)

## Name
Original Provider Values - Provenance of Harvested Metadata

## Description

### Context
The GoTriple platform aggregates research artifacts from many heterogeneous SSH sources through its data processing pipeline (SCRE). During ingestion, several metadata fields are **normalized**: the resource type is mapped to the Content Type controlled vocabulary, the language is resolved to a `schema:Language` entity, dates are converted to ISO 8601, and licenses and access conditions are mapped to the License and Access Condition controlled vocabularies.

The values **as originally received from the provider** are however preserved by the platform, because they carry provenance information that the normalized values lose: they document what the source actually said, they allow the normalization to be audited and re-run, and they let data consumers detect mapping errors (e.g. a raw `info:eu-repo/semantics/openAccess` mapped to the wrong access condition).

The current ontology (up to iteration 16) models only the normalized values. This iteration completes the model with the raw, pre-normalization values (issue [#38](https://github.com/atrium-research/triple-ontology/issues/38), second checklist item).

### Objective
Introduce six datatype properties that preserve the original provider values on `triple:Document` (and, per the LUMEN ADR 005 data-model tables, on the other content classes):

- `triple:originalType` - the resource type string as received (e.g. `journalArticle`, `COAR text`)
- `triple:originalLanguage` - the language value as received (e.g. `eng`, `English`, `fr-FR`)
- `triple:originalDatePublished` - the publication date string as received, in whatever format the provider used (e.g. `03/05/2021`, `May 2021`)
- `triple:originalLicense` - the license statement as received (e.g. `CC BY 4.0`, a URL, free text)
- `triple:originalConditionsOfAccess` - the access rights statement as received (e.g. `info:eu-repo/semantics/openAccess`)
- `triple:originalSource` - the source statement as received (e.g. a journal issue string), before processing into the normalized source or the URL-based identifiers

## Technical Specification
- All six properties are `owl:DatatypeProperty` with range `xsd:string`: raw values are kept verbatim, so no datatype or vocabulary constraint applies.
- **Hybrid sub-property pattern**: each property is declared `rdfs:subPropertyOf` the corresponding Dublin Core *Elements 1.1* term (`dc:type`, `dc:language`, `dc:date`, `dc:rights`), following the same reuse-by-subsumption approach already used for `triple:hasLicense ⊑ dcterms:license` and `triple:hasContentType ⊑ dcterms:type`. DC Elements is chosen over DCMI Terms because its properties have no range constraints and are the de-facto standard for raw harvested metadata (OAI-PMH `oai_dc`); a generic Dublin Core consumer therefore sees the raw values through the standard `dc:` terms by inference.
- `triple:originalLicense` and `triple:originalConditionsOfAccess` are both sub-properties of `dc:rights` (DC Elements does not distinguish the two notions); the TRIPLE properties preserve the distinction.
- The normalized counterparts remain on the existing properties: `triple:hasContentType`, `schema:inLanguage`, `schema:datePublished`, `triple:hasLicense`, `triple:hasAccessCondition`.
- `triple:originalSource` is declared `rdfs:subPropertyOf dc:source`, consistently with the other five.
- The properties are optional (0 or more), expressed as `owl:allValuesFrom xsd:string` restrictions, consistent with the style of the other iterations. Following the LUMEN ADR 005 data-model tables, the restrictions are declared on `triple:Document`, `triple:Dataset`, `triple:MediaObject` and `triple:SemanticArtefact`; `original_source` is not defined for Dataset in the ADR, so `triple:Dataset` carries only the other five.

## Examples
- A document harvested from an Italian repository arrives with type `journalArticle`, language `eng`, publication date `03/05/2021`, license `CC BY 4.0`, access rights `info:eu-repo/semantics/openAccess` and source `Journal of Digital Humanities, 12(3), 2021`. The pipeline normalizes these to `ContentType/article`, an English `schema:Language`, `"2021-05-03"^^xsd:date`, `License/creative_commons` and `AccessCondition/open_access`, while the six raw strings are preserved on the document.
- A document from another source arrives with only a raw type (`COAR text`) and raw access rights (`restricted`); the other original fields are absent. Only the corresponding original properties are asserted.
- A dataset harvested from a data repository arrives with raw type `Dataset/csv`, raw language `French` and a raw license URL; the raw values are preserved on the dataset with the same properties (no original source, which the ADR does not define for datasets).
