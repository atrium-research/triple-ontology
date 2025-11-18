# Glossary of Terms (Iteration 12)

| Term                           | Definition                                                                                                                                          |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `triple:Dataset`               | GoTriple ontology class representing a dataset, subclass of schema:Dataset, with specific metadata requirements for research data.                 |
| `Dataset`                      | A research dataset indexed in the GoTriple platform, representing data from various sources including institutional repositories and data catalogs. |
| `schema:spatialCoverage`       | Schema.org property indicating the geographical area covered by the dataset.                                                                        |
| `schema:temporalCoverage`      | Schema.org property indicating the temporal period that the dataset covers.                                                                         |
| `schema:encodingFormat`        | Schema.org property specifying the file format of the dataset (e.g., text/csv, application/json, application/x-spss).                             |
| `schema:size`                  | Schema.org property indicating the size of the dataset (e.g., file size in MB).                                                                    |
| `schema:creativeWorkStatus`    | Schema.org property describing the status of the dataset in terms of its stage in a lifecycle.                                                     |
| `schema:GeoShape`              | Schema.org class representing the geographic shape or bounding box of the dataset's spatial coverage.                                               |
| `schema:contactPoint`          | Schema.org property providing contact information for the dataset.                                                                                  |
| `DOI`                          | Digital Object Identifier - a persistent identifier for datasets when available.                                                                   |
| `Handle.Net`                   | A persistent identifier system used for datasets, alternative to DOI.                                                                              |
| `Spatial Coverage`             | The geographical scope of the data contained in the dataset.                                                                                        |
| `Temporal Coverage`            | The time period that the dataset's data represents or covers.                                                                                       |
| `Distribution`                 | Information about how the dataset can be accessed, downloaded, or obtained.                                                                         |
| `Bounding Box`                 | Geographic coordinates defining the spatial extent of the dataset.                                                                                  |
| `Lineage`                      | Provenance information describing the dataset's chain of custody and processing history.                                                            |
| `schema:contributor`           | Schema.org property indicating a secondary contributor to the dataset.                                                                              |
| `schema:dateModified`          | Schema.org property indicating the date on which the dataset was most recently modified.                                                            |
| `schema:provider`              | Schema.org property indicating the aggregator or service provider of the dataset.                                                                   |
| `schema:additionalType`        | Schema.org property specifying additional type information for the dataset (e.g., "Geospatial Dataset", "Survey Dataset").                       |
| `schema:knowsAbout`            | Schema.org property indicating topics that the dataset is about, often automatically detected from controlled vocabularies.                        |
| `schema:funding`               | Schema.org property linking the dataset to research projects that funded its creation.                                                              |
| `schema:mentions`              | Schema.org property indicating references or mentions of other datasets or entities within the dataset's metadata.                                 |
| `schema:comment`               | Schema.org property used for lineage information - free-text descriptions of the dataset's processing history.                                     |
| `sioc:topic`                   | SIOC vocabulary property linking the dataset to topic concepts or themes.                                                                           |
| `dcterms:isReferencedBy`       | Dublin Core Terms property indicating documents or publications that reference this dataset.                                                        |
| `schema:keywords`              | Schema.org object property linking to defined terms that describe the dataset content.                                                              |
| `schema:DefinedTerm`           | Schema.org class representing a word, name, acronym, phrase, etc. with a formal definition used to describe dataset topics.                        |
