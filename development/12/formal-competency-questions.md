## Formal Competency Questions (Iteration 12)

## CQ_12.1

Return all datasets available in the platform.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database"
- `triple:dataset_002` → "European Social Attitudes Survey 2023"


## CQ_12.2

Return all datasets with their spatial coverage.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title ?spatial WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title ;
           schema:spatialCoverage ?spatial .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "Europe"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "European Union"


## CQ_12.3

Return all datasets with their format and size information.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title ?format ?size WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title ;
           schema:encodingFormat ?format ;
           schema:size ?size .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "text/csv" → "15.2 MB"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "application/x-spss" → "245 MB"


## CQ_12.4

Return all datasets that have DOI identifiers.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?dataset ?title ?identifierValue WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title ;
           datacite:hasIdentifier ?identifier .
  ?identifier datacite:hasIdentifierScheme triple:doi ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "10.1234/example.dataset.001"


## CQ_12.5

Return all datasets with their keywords.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title ?keyword ?keywordName WHERE {
  ?dataset a schema:Dataset ;
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


## CQ_12.6

Return all datasets with temporal coverage.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title ?temporal WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title ;
           schema:temporalCoverage ?temporal .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "2000 BCE - 1500 CE"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "2023"


## CQ_12.7

Return all datasets with their contributors.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title ?contributor WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title ;
           schema:contributor ?contributor .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → "Dr. Anna Fischer"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → "Prof. Elena Rodriguez"


## CQ_12.8

Return all datasets with their funding projects.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title ?project WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title ;
           schema:funding ?project .
  ?project schema:name ?projectName .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → `triple:project-heritage-mapping`
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → `triple:project-social-cohesion`


## CQ_12.9

Return all datasets with their contact points.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?dataset ?title ?contact ?email WHERE {
  ?dataset a schema:Dataset ;
           schema:headline ?title ;
           schema:contactPoint ?contact .
  ?contact schema:email ?email .
}
```

**Expected result:**
- `triple:dataset_001` → "European Archaeological Sites Database" → `triple:contact-heritage-institute` → "data@heritage.eu"
- `triple:dataset_002` → "European Social Attitudes Survey 2023" → `triple:contact-social-observatory` → "support@social-eu.org"

