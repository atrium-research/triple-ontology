# Glossary of Terms (Iteration 18)

| Term                               | Definition                                                                                                                                                       |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `triple:confidence`                | A datatype property carrying the trust score (0-1, `xsd:decimal`) of an automatic enrichment, asserted on the `oa:Annotation` that records the enrichment.        |
| `schema:about` | The subject matter of the content, from Schema.org. Carries the concepts of the TRIPLE thesaurus detected by the enrichment pipeline, identified by their semantics.gr URI. Range `skos:Concept`. |
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
| `skos:Concept` | A concept of a knowledge organization system, from SKOS. The values of `schema:about` are the concepts of the TRIPLE Vocabulary (SSH-LCSH). |
| `skos:prefLabel` | The preferred label of a concept, from SKOS; the TRIPLE Vocabulary carries it in up to twelve languages. |
| `skos:exactMatch` | Links a concept of the TRIPLE Vocabulary to the LCSH heading it derives from, asserted by the authority itself. |
| `schema:sameAs`                    | The schema.org property for a reference page that unambiguously identifies the item (e.g. a Wikidata entity). Used for the external URI of a producer keyword, where `skos:exactMatch` would wrongly type the target as a SKOS concept. |
| `Document`                         | An entity representing any type of resource available on the GoTriple platform. Represented as `triple:Document`.                                                 |
