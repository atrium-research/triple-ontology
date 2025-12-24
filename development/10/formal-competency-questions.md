## Formal Competency Questions (Iteration 10)

## CQ_10.1

Return all datasets available in the platform.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database"
- `triple:dataset_002` → "European Social Attitudes Survey 2023"


## CQ_10.2

Return all datasets with their spatial coverage.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title ?spatial WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           schema:spatialCoverage ?spatial .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "Europe"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "European Union"


## CQ_10.3

Return all datasets with their format and size information.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title ?format ?size WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           schema:encodingFormat ?format ;
           schema:size ?size .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "text/csv" → "15.2 MB"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "application/x-spss" → "245 MB"


## CQ_10.4

Return all datasets that have DOI identifiers.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?dataset ?title ?identifierValue WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           datacite:hasIdentifier ?identifier .
  ?identifier a triple:DOI ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:dataset-001` → "European Archaeological Sites Database" → "10.5281/zenodo.heritage.arch.2023"
- `triple:dataset-002` → "European Social Attitudes Survey 2023" → "10.5281/zenodo.social.attitudes.2023"


## CQ_10.10

Return all datasets that have Handle identifiers using class-based approach.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?dataset ?title ?identifierValue WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           datacite:hasIdentifier ?identifier .
  ?identifier a triple:Handle ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:dataset-001` → "European Archaeological Sites Database" → "21.11130/00-HERITAGE-ARCH-2023"
- `triple:dataset-002` → "European Social Attitudes Survey 2023" → "21.11130/00-SOCIAL-ATTITUDES-2023"


## CQ_10.11

Return all datasets that have platform identifiers (ID, PID, OriginalIdentifier).

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?dataset ?title ?identifier ?identifierType ?value WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           datacite:hasIdentifier ?identifier .
  ?identifier a ?identifierType ;
              litre:hasLiteralValue ?value .
  FILTER (?identifierType IN (triple:ID, triple:PID, triple:OriginalIdentifier))
}
```

**Expected result:**
- `triple:dataset-001` → "European Archaeological Sites Database" → `triple:identifier-heritage-internal` → `triple:ID` → "TRIPLE_DATASET_HERITAGE_001"
- `triple:dataset-001` → "European Archaeological Sites Database" → `triple:identifier-heritage-pid` → `triple:PID` → "gotriple:dataset:heritage-archaeological-sites"
- `triple:dataset-002` → "European Social Attitudes Survey 2023" → `triple:identifier-social-internal` → `triple:ID` → "TRIPLE_DATASET_SOCIAL_002"


## CQ_10.5

Return all datasets with their keywords.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title ?keyword ?keywordName WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           schema:keywords ?keyword .
  ?keyword schema:name ?keywordName .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → `triple:keyword-archaeology` → "archaeology"
- `triple:dataset_001` → "European Archaeological Sites Database" → `triple:keyword-heritage` → "heritage"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → `triple:keyword-survey` → "survey"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → `triple:keyword-politics` → "politics"


## CQ_10.6

Return all datasets with temporal coverage.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title ?temporal WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           schema:temporalCoverage ?temporal .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "2000 BCE - 1500 CE"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "2023"


## CQ_10.7

Return all datasets with their contributors.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title ?contributor WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           schema:contributor ?contributor .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "Dr. Anna Fischer"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "Prof. Elena Rodriguez"


## CQ_10.8

Return all datasets with their funding projects.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title ?project WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           schema:funding ?project .
  ?project schema:name ?projectName .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → `triple:project-heritage-mapping`
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → `triple:project-social-cohesion`


## CQ_10.9

Return all datasets with their contact points.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?dataset ?title ?contact ?email WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           schema:contactPoint ?contact .
  ?contact schema:email ?email .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → `triple:contact-heritage-institute` → "data@heritage.eu"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → `triple:contact-social-observatory` → "support@social-eu.org"


## CQ_10.12

Return all datasets with their distribution access URLs.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

SELECT ?dataset ?title ?accessURL WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           dcat:distribution ?distribution .
  ?distribution dcat:accessURL ?accessURL .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "https://data.heritage.eu/download/sites.csv"


## CQ_10.13

Return all datasets with their bounding box.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

SELECT ?dataset ?title ?bbox WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           dcat:bbox ?bbox .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "POLYGON((-10 35, 30 35, 30 70, -10 70, -10 35))"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "POLYGON((-10 34, 34 34, 34 72, -10 72, -10 34))"


## CQ_10.14

Return the provenance statement for all datasets.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?dataset ?title ?provenanceComment WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           dcterms:provenance ?provenance .
  ?provenance rdfs:comment ?provenanceComment .
}
```

**Expected result:**
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "Survey results merged from 27 EU member state polls..."


## CQ_10.15

Return all datasets with their license.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?dataset ?title ?license WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           triple:hasLicense ?lic .
  ?lic rdfs:label ?license .
}
```

**Expected result:**
- `triple:dataset-001` → "European Archaeological Sites Database" → "CC BY-NC-ND 4.0"
- `triple:dataset-002` → "European Social Attitudes Survey 2023" → "CC BY 4.0"


## CQ_10.16

Return all datasets with their access conditions.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?dataset ?title ?access WHERE {
  ?dataset a triple:Dataset ;
           schema:headline ?title ;
           triple:hasAccessCondition ?acc .
  ?acc rdfs:label ?access .
}
```

**Expected result:**
- `triple:dataset-001` → "European Archaeological Sites Database" → "Open Access"
- `triple:dataset-002` → "European Social Attitudes Survey 2023" → "Restricted Access"
