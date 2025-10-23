# Formal Competency Questions (Iteration 2)

## CQ_2.1

What license is associated with `document_1`?

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?license WHERE {
  triple:document_1 schema:license ?license .
}
```

**Expected Result:**
- `triple:cc_by_4_0`


## CQ_2.2

What are the access conditions for `document_2`?

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?accessConditions WHERE {
  triple:document_2 schema:conditionsOfAccess ?accessConditions .
}
```

**Expected Result:**
- `triple:open_access`


## CQ_2.3

What type of document is `document_3`?

```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?type WHERE {
  triple:document_3 dc:type ?type .
}
```

**Expected Result:**
- `triple:article`


## CQ_2.4

What disciplines is `document_4` associated with?

```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?discipline WHERE {
  triple:document_4 dc:subject ?discipline .
}
```

**Expected Result:**
- `triple:digital_humanities`
- `triple:linguistics`


## CQ_2.5

What external entity does the license term `cc_by_4_0` match exactly?

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

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
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?externalEntity WHERE {
  triple:open_access skos:closeMatch ?externalEntity .
}
```

**Expected Result:**
- `http://purl.org/coar/access_right/c_abf2`


## CQ_2.7

Which vocabulary (ConceptScheme) does the term `article` belong to?

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?vocabulary WHERE {
  triple:article skos:inScheme ?vocabulary .
}
```

**Expected Result:**
- `triple:document_type_vocabulary`


## CQ_2.8

Return all terms that belong to the `discipline_vocabulary`.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?term WHERE {
  ?term skos:inScheme triple:discipline_vocabulary .
}
```

**Expected Result:**
- `triple:digital_humanities`
- `triple:linguistics`


## CQ_2.9

Return all documents that are licensed under Creative Commons licenses (checking for exactMatch to Creative Commons URIs).

```sparql
PREFIX schema: <http://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document schema:license ?license .
  ?license skos:exactMatch ?externalLicense .
  FILTER(STRSTARTS(STR(?externalLicense), "https://creativecommons.org/"))
}
```

**Expected Result:**
- `triple:document_1`


## CQ_2.10

Return all documents that are of type "Article" and are Open Access.

```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document dc:type triple:article .
  ?document schema:conditionsOfAccess triple:open_access .
}
```

**Expected Result:**
- (No documents currently match both criteria in the ABOX)


## CQ_2.11

Return all ConceptSchemes (controlled vocabularies) defined in the ontology.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?vocabulary WHERE {
  ?vocabulary rdf:type skos:ConceptScheme .
}
```

**Expected Result:**
- `triple:license_vocabulary`
- `triple:access_conditions_vocabulary`
- `triple:document_type_vocabulary`
- `triple:discipline_vocabulary`


## CQ_2.12

For a given document, return all its classification metadata (license, access conditions, type, and disciplines).

```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?license ?access ?type ?discipline WHERE {
  OPTIONAL { triple:document_1 schema:license ?license . }
  OPTIONAL { triple:document_1 schema:conditionsOfAccess ?access . }
  OPTIONAL { triple:document_1 dc:type ?type . }
  OPTIONAL { triple:document_1 dc:subject ?discipline . }
}
```

**Expected Result:**
- `?license` = `triple:cc_by_4_0`
- `?access` = (none in current data)
- `?type` = (none in current data)
- `?discipline` = (none in current data)
