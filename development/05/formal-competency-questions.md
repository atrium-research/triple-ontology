## Formal Competency Questions (Iteration 5)

## CQ_5.1

Return all records of the same scholarly work as `document_7`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?documents WHERE {
  { ?documents triple:isDuplicateOf triple:document_7 }
  UNION
  { BIND(triple:document_7 AS ?documents) }
}
```

## CQ_5.2

Return all authors from `document_56` and if they are discarded or not.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?agent ?discarded WHERE {
	triple:document_56 schema:author ?agent .
  	?agent triple:isDiscarded ?discarded .
}
```

## CQ_5.3

Return all keywords from `document_67` and if they are discarded or not.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?keywords ?discarded WHERE {
	triple:document_67 schema:keywords ?keywords .
  	?keywords triple:isDiscarded ?discarded .
}
```
