## Formal Competency Questions (Iteration 5)

## CQ_5.1

Return the documents inside `cluster_45`.

```
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?documents WHERE {
	?documents triple:inCluster triple:cluster_45 .
}
```

## CQ_5.2

Return all authors from `document_56` and if they are discarded or not.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?agent ?discarded WHERE {
	triple:document_56 schema:author ?agent .
  	?agent triple:isDiscarded ?discarded .
}
```

## CQ_5.3

Return all keywords from `document_67` and if they are discarded or not.

```
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?keywords ?discarded WHERE {
	triple:document_67 schema:keywords ?keywords .
  	?keywords triple:isDiscarded ?discarded .
}
```