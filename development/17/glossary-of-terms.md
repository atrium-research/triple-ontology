# Glossary of Terms (Iteration 17)

| Term                                | Definition                                                                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `triple:originalType`               | A datatype property preserving the resource type exactly as received from the source provider, before normalization to the Content Type vocabulary. Sub-property of `dc:type`. |
| `triple:originalLanguage`           | A datatype property preserving the language value exactly as received from the source provider, before normalization to a `schema:Language` entity. Sub-property of `dc:language`. |
| `triple:originalDatePublished`      | A datatype property preserving the publication date string exactly as received from the source provider, before conversion to ISO 8601. Sub-property of `dc:date`. |
| `triple:originalLicense`            | A datatype property preserving the license statement exactly as received from the source provider, before normalization to the License vocabulary. Sub-property of `dc:rights`. |
| `triple:originalConditionsOfAccess` | A datatype property preserving the access rights statement exactly as received from the source provider, before normalization to the Access Condition vocabulary. Sub-property of `dc:rights`. |
| `dc:type`                           | The Dublin Core Elements 1.1 property for the nature or genre of the resource; used as the interoperable super-property of `triple:originalType`.                  |
| `dc:language`                       | The Dublin Core Elements 1.1 property for the language of the resource; used as the interoperable super-property of `triple:originalLanguage`.                     |
| `dc:date`                           | The Dublin Core Elements 1.1 property for a date associated with the resource; used as the interoperable super-property of `triple:originalDatePublished`.         |
| `dc:rights`                         | The Dublin Core Elements 1.1 property for rights information about the resource; used as the interoperable super-property of `triple:originalLicense` and `triple:originalConditionsOfAccess`. |
| `Document`                          | An entity representing any type of resource available on the GoTriple platform. Represented as `triple:Document`.                                                  |
