## Informal Competency Questions (Iteration 10)

## Question 1

### Identifier
CQ_10.1

### Question
Return all datasets available in the platform.

### Expected Outcome
A list of all datasets with their titles.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database"
* `triple:dataset-002` → "European Social Attitudes Survey 2023"

### Based on
Example 1 and Example 2


## Question 2

### Identifier
CQ_10.2

### Question
Return all datasets with their spatial coverage.

### Expected Outcome
A list of datasets with their geographical coverage information.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:place-europe`
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:place-european-union`

### Based on
Example 1 and Example 2


## Question 3

### Identifier
CQ_10.3

### Question
Return all datasets with their format and size information.

### Expected Outcome
A list of datasets with encoding format and file size.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "text/csv" → "15.2 MB"
* `triple:dataset-001` → "European Archaeological Sites Database" → "application/json" → "15.2 MB"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "application/x-spss" → "245 MB"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "text/csv" → "245 MB"

### Based on
Example 1 and Example 2


## Question 4

### Identifier
CQ_10.4

### Question
Return all datasets that have DOI identifiers.

### Expected Outcome
A list of datasets with valid DOI identifiers.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "10.5281/zenodo.heritage.arch.2023"
* `triple:dataset-001` → "European Archaeological Sites Database" → "10.1234/example.dataset.001"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "10.5281/zenodo.social.attitudes.2023"

### Based on
Example 1 and Example 2


## Question 5

### Identifier
CQ_10.5

### Question
Return all datasets with their descriptive keywords.

### Expected Outcome
A list of datasets with their associated keyword terms.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:keyword-archaeology` → "archaeology"
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:keyword-europe` → "Europe"
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:keyword-heritage` → "heritage"
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:keyword-spatial-data` → "spatial data"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:keyword-social-attitudes` → "social attitudes"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:keyword-survey` → "survey"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:keyword-politics` → "politics"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:keyword-demographics` → "demographics"

### Based on
Example 1 and Example 2


## Question 6

### Identifier
CQ_10.6

### Question
Return all datasets with temporal coverage.

### Expected Outcome
A list of datasets with their temporal scope.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "2000 BCE - 1500 CE"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "2023"

### Based on
Example 1 and Example 2


## Question 7

### Identifier
CQ_10.7

### Question
Return all datasets with their contributors.

### Expected Outcome
A list of datasets with their contributor information.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "Dr. Anna Fischer"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "Prof. Elena Rodriguez"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "Dr. Klaus Mueller"

### Based on
Example 1 and Example 2


## Question 8

### Identifier
CQ_10.8

### Question
Return all datasets with their funding projects.

### Expected Outcome
A list of datasets with their associated research projects.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:project-heritage-mapping`
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:project-social-cohesion`

### Based on
Example 1 and Example 2


## Question 9

### Identifier
CQ_10.9

### Question
Return all datasets with their contact points.

### Expected Outcome
A list of datasets with contact information for data access.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:contact-heritage-institute` → "data@heritage.eu"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:contact-social-observatory` → "support@social-eu.org"

### Based on
Example 1 and Example 2


## Question 10

### Identifier
CQ_10.10

### Question
Return all datasets that have Handle identifiers by identifier scheme.

### Expected Outcome
A list of datasets with valid Handle identifiers.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "21.11130/00-HERITAGE-ARCH-2023"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "21.11130/00-SOCIAL-ATTITUDES-2023"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "hdl:1234.5/survey2023"

### Based on
Example 1 and Example 2


## Question 11

### Identifier
CQ_10.11

### Question
Return all datasets that have platform identifiers (internal id, PID, original identifier).

### Expected Outcome
A list of datasets with their internal platform identifiers by type.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:identifier-heritage-internal` → `triple:internal_id_schema` → "TRIPLE_DATASET_HERITAGE_001"
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:identifier-heritage-pid` → `datacite:ark` → "ark:/12345/dataset-heritage-archaeological-sites"
* `triple:dataset-001` → "European Archaeological Sites Database" → `triple:identifier-heritage-original` → `triple:original_id_schema` → "heritage_inst_arch_sites_2023"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:identifier-social-internal` → `triple:internal_id_schema` → "TRIPLE_DATASET_SOCIAL_002"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:identifier-social-pid` → `datacite:ark` → "ark:/12345/dataset-social-attitudes-survey-2023"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:identifier-social-original` → `triple:original_id_schema` → "social_obs_attitudes_2023"

### Based on
Example 1 and Example 2


## Question 12

### Identifier
CQ_10.12

### Question
Return all datasets with their distribution access URLs.

### Expected Outcome
A list of datasets with the URL to access/download the data.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "https://data.heritage.eu/download/sites.csv"

### Based on
Example 1


## Question 13

### Identifier
CQ_10.13

### Question
Return all datasets with their bounding box.

### Expected Outcome
A list of datasets with their spatial extent defined as a WKT literal.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "POLYGON((-10 35, 30 35, 30 70, -10 70, -10 35))"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "POLYGON((-10 34, 34 34, 34 72, -10 72, -10 34))"

### Based on
Example 1 and Example 2


## Question 14

### Identifier
CQ_10.14

### Question
Return the provenance statement for all datasets.

### Expected Outcome
A list of datasets with the statement describing how the data was produced.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "Data aggregated from 15 national museums and normalized to CIDOC-CRM before conversion to CSV."
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "Survey results merged from 27 EU member state polls, anonymized, and weighted for demographic representativeness."

### Based on
Example 1 and Example 2


## Question 15

### Identifier
CQ_10.15

### Question
Return all datasets with their license.

### Expected Outcome
A list of datasets with their license information.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "CC BY-NC-ND 4.0"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "CC BY 4.0"

### Based on
Example 1 and Example 2


## Question 16

### Identifier
CQ_10.16

### Question
Return all datasets with their access conditions.

### Expected Outcome
A list of datasets with their access status.

### Result
* `triple:dataset-001` → "European Archaeological Sites Database" → "Open Access"
* `triple:dataset-002` → "European Social Attitudes Survey 2023" → "Restricted Access"

### Based on
Example 1 and Example 2
