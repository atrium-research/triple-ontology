## Formal Competency Questions (Iteration 9)

## CQ_9.1

Return all entities mentioned by `document_1`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?entity WHERE {
  triple:document_1 schema:mentions ?entity .
}
```

**Expected result:**
- `triple:document_45`
- `triple:person_23`


## CQ_9.2

Return all documents mentioned by `document_89`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  triple:document_89 schema:mentions ?document .
  ?document a triple:Document .
}
```

**Expected result:**
- `triple:document_100`
- `triple:document_101`
- `triple:document_102`


## CQ_9.3

Return all documents that mention `person_78`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document a triple:Document ;
            schema:mentions triple:person_78 .
}
```

**Expected result:**
- `triple:document_34`


## CQ_9.4

Return all projects mentioned in any document.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT DISTINCT ?project WHERE {
  ?document a triple:Document ;
            schema:mentions ?project .
  ?project a triple:Project .
}
```

**Expected result:**
- `triple:project_12`


## CQ_9.5

Return all organizations mentioned by `document_67`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?organization WHERE {
  triple:document_67 schema:mentions ?organization .
  ?organization a foaf:Organization .
}
```

**Expected result:**
- `triple:organization_5`


## CQ_9.6

Return all people mentioned by `document_34`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?person WHERE {
  triple:document_34 schema:mentions ?person .
  ?person a foaf:Person .
}
```

**Expected result:**
- `triple:person_78`


## CQ_9.7

Return all documents that mention at least one other document.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT DISTINCT ?document WHERE {
  ?document a triple:Document ;
            schema:mentions ?mentioned .
  ?mentioned a triple:Document .
}
```

**Expected result:**
- `triple:document_1`
- `triple:document_89`


## CQ_9.8

Return all entities mentioned by `document_67` with their types.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?entity ?type WHERE {
  triple:document_67 schema:mentions ?entity .
  ?entity a ?type .
}
```

**Expected result:**
- `triple:project_12` → `triple:Project`
- `triple:organization_5` → `foaf:Organization`


## CQ_9.9

Count how many entities each document mentions.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?document (COUNT(?entity) AS ?mentionCount) WHERE {
  ?document a triple:Document ;
            schema:mentions ?entity .
}
GROUP BY ?document
ORDER BY DESC(?mentionCount)
```

**Expected result:**
- `triple:document_89` → 3
- `triple:document_1` → 2
- `triple:document_34` → 2
- `triple:document_67` → 2
