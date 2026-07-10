# Glossary of Terms (Iteration 18)

| Term                               | Definition                                                                                                                                                       |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `triple:confidence`                | A datatype property carrying the trust score (0-1, `xsd:decimal`) of an automatic enrichment, asserted on the `oa:Annotation` that records the enrichment.        |
| `triple:knowsAbout`                | An object property linking a GoTriple resource to a keyword extracted by the enrichment pipeline, represented as a `schema:DefinedTerm`. Sub-property of `schema:about`. |
| `triple:detectedLanguage`          | A datatype property carrying the language tag identified by the GoTriple language-detection service for the resource's text.                                      |
| `triple:machineTranslatedLanguage` | A datatype property listing the language tags whose title/abstract versions were produced by the GoTriple machine-translation service.                            |
| `oa:Annotation`                    | A W3C Web Annotation; used to record enrichment provenance (classification and tagging) together with its confidence and creator.                                 |
| `oa:Motivation`                    | The reason an annotation was created (W3C Web Annotation vocabulary).                                                                                             |
| `oa:hasTarget`                     | The property connecting an annotation to the resource being enriched.                                                                                             |
| `oa:hasBody`                       | The property connecting an annotation to the concept or term assigned to the target.                                                                              |
| `oa:motivatedBy`                   | The property connecting an annotation to its motivation.                                                                                                          |
| `oa:classifying`                   | The standard W3C motivation for classifying the target as something; used for discipline assignments.                                                             |
| `oa:tagging`                       | The standard W3C motivation for associating a tag with the target; used for keyword assignments.                                                                  |
| `dcterms:creator`                  | The agent responsible for the annotation; for GoTriple enrichments, the GoTriple pipeline (covers SKG-IF `associated_with`).                                      |
| `schema:about`                     | The schema.org property for the subject matter of the content; in-domain super-property of `triple:knowsAbout`.                                                   |
| `schema:DefinedTerm`               | A word, name, acronym or phrase defined in a controlled context; the class of GoTriple keywords.                                                                  |
| `schema:name`                      | The schema.org naming property; carries the language-tagged labels of a keyword.                                                                                  |
| `schema:sameAs`                    | The schema.org property for a reference page that unambiguously identifies the item (e.g. a Wikidata entity); carries the keyword's external URI.                 |
| `Document`                         | An entity representing any type of resource available on the GoTriple platform. Represented as `triple:Document`.                                                 |
