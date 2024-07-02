## Formal Competency Questions (Iteration 7)

## CQ_7.1

Return all triples that have as subject the `project_1`.

```
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?predicate ?object WHERE {
	triple:project_1 ?predicate ?object .
}
```

## CQ_7.2

Return all grants for the `project_1` and the corresponding person or organization involved.

```
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?grant ?funder WHERE {
	triple:project_1 schema:funding ?grant .
  	?grant schema:funder ?funder .
}
```

## CQ_7.3

Return all agents and the respective roles connected to `project_1`.

```
PREFIX pro: <http://purl.org/spar/pro/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?role_in_time ?role WHERE {
	triple:project_1 pro:isDocumentContextFor ?role_in_time .
  	?role_in_time pro:withRole ?role .
}
```


