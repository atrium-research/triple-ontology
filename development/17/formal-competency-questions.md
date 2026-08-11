# Formal Competency Questions (Iteration 17)

## CQ_17.1

Return all the original (as-received) metadata values of `triple:document_it17_1`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?property ?value WHERE {
  triple:document_it17_1 ?property ?value .
  FILTER(?property IN (
    triple:originalAdditionalType,
    triple:originalInLanguage,
    triple:originalDatePublished,
    triple:originalLicense,
    triple:originalConditionOfAccess
  ))
}
```

**Expected result:**
- `triple:originalAdditionalType` → "journalArticle"
- `triple:originalInLanguage` → "eng"
- `triple:originalDatePublished` → "03/05/2021"
- `triple:originalLicense` → "CC BY 4.0"
- `triple:originalConditionOfAccess` → "info:eu-repo/semantics/openAccess"

## CQ_17.2

For each document, return the original type received from the provider and the Content Type concept it was normalized to.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?document ?originalAdditionalType ?contentType WHERE {
  ?document rdf:type triple:Document ;
            triple:originalAdditionalType ?originalAdditionalType ;
            triple:hasContentType ?contentType .
}
```

**Expected result:**
- `document_it17_1` → "journalArticle" / `ContentType/article`
- `document_it17_2` → "COAR text" / `ContentType/text`

## CQ_17.3

Return the documents that were received with the raw access rights statement `info:eu-repo/semantics/openAccess`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?document WHERE {
  ?document rdf:type triple:Document ;
            triple:originalConditionOfAccess "info:eu-repo/semantics/openAccess" .
}
```

**Expected result:**
- `document_it17_1`

## CQ_17.4

Return all rights-related information (in the Dublin Core sense) received from the provider for `triple:document_it17_1`, i.e. the values of every property that refines `dc:rights`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?property ?value WHERE {
  ?property rdfs:subPropertyOf dc:rights .
  triple:document_it17_1 ?property ?value .
}
```

**Expected result:**
- `triple:originalLicense` → "CC BY 4.0"
- `triple:originalConditionOfAccess` → "info:eu-repo/semantics/openAccess"

## CQ_17.5

Return the raw source statement of `triple:document_it17_1` and all original provider values of `triple:dataset_it17_1`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?documentSource ?datasetProperty ?datasetValue WHERE {
  triple:document_it17_1 triple:originalSource ?documentSource .
  triple:dataset_it17_1 ?datasetProperty ?datasetValue .
  FILTER(STRSTARTS(STR(?datasetProperty), STR(triple:original)))
}
```

**Expected result:**
- `documentSource` → "Journal of Digital Humanities, 12(3), 2021"
- `triple:originalAdditionalType` → "Dataset/csv"
- `triple:originalInLanguage` → "French"
- `triple:originalLicense` → "https://spdx.org/licenses/CC-BY-4.0.html"
