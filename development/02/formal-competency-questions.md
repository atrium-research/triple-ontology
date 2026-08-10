# Formal Competency Questions (Iteration 2)

## CQ_2.1

What license is associated with `document_1`?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?license WHERE {
  triple:document_1 triple:hasLicense ?license .
}
```

**Expected Result:**
- `triple:cc_by_4_0`


## CQ_2.2

What are the access conditions for `document_2`?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?accessConditions WHERE {
  triple:document_2 triple:hasAccessCondition ?accessConditions .
}
```

**Expected Result:**
- `triple:open_access`


## CQ_2.3

What type of document is `document_3`?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?type WHERE {
  triple:document_3 triple:hasContentType ?type .
}
```

**Expected Result:**
- `triple:article`


## CQ_2.4

What disciplines is `document_4` associated with?

```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?discipline WHERE {
  triple:document_4 sioc:topic ?discipline .
}
```

**Expected Result:**
- `triple:digital_humanities`
- `triple:linguistics`


## CQ_2.5

What external entity does the license term `cc_by_4_0` match exactly?

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?externalEntity WHERE {
  triple:cc_by_4_0 skos:exactMatch ?externalEntity .
}
```

**Expected Result:**
- `https://creativecommons.org/licenses/by/4.0/`


## CQ_2.6

What external entities does the access term `open_access` closely match?

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?externalEntity WHERE {
  triple:open_access skos:closeMatch ?externalEntity .
}
```

**Expected Result:**
- `http://purl.org/coar/access_right/c_abf2`


## CQ_2.7

Return all documents that are licensed under Creative Commons licenses (checking for exactMatch to Creative Commons URIs).

```sparql
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?document WHERE {
  ?document triple:hasLicense ?license .
  ?license skos:exactMatch ?externalLicense .
  FILTER(STRSTARTS(STR(?externalLicense), "https://creativecommons.org/"))
}
```

**Expected Result:**
- `triple:document_1`


## CQ_2.8

Return all documents that are of type "Article" and are Open Access.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?document WHERE {
  ?document triple:hasContentType triple:article ;
            triple:hasAccessCondition triple:open_access .
}
```

**Expected Result:**
- (Empty in current example data, valid query structure)


## CQ_2.9

For a given document, return all its classification metadata (license, access conditions, type, and disciplines).

```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?license ?access ?type ?discipline WHERE {
  OPTIONAL { triple:document_1 triple:hasLicense ?license . }
  OPTIONAL { triple:document_1 triple:hasAccessCondition ?access . }
  OPTIONAL { triple:document_1 triple:hasContentType ?type . }
  OPTIONAL { triple:document_1 sioc:topic ?discipline . }
}
```

**Expected Result:**
- `?license` = `triple:cc_by_4_0`
- `?access` = (none)
- `?type` = (none)
- `?discipline` = (none)


## CQ_2.10

Which controlled-vocabulary classes does the document metadata draw its values from?

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?vocabularyClass ?label WHERE {
  ?vocabularyClass a owl:Class ;
                   rdfs:subClassOf skos:Concept ;
                   rdfs:label ?label .
}
```

**Expected Result:**
- `triple:License` → "License"
- `triple:AccessCondition` → "Access Condition"
- `triple:Discipline` → "Discipline"
- `triple:ContentType` → "Content Type"

The four vocabularies are published as separate modules (`vocabularies/serializations/ttl/`) and compiled into stand-alone ontologies by `scripts/build.py`; the iteration TBOX declares the classes their concepts instantiate, not an `owl:imports` of the modules.
