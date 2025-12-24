## Formal Competency Questions (Iteration 1)

## CQ_4.1

Return all spatial subjects of the `document_2`.

```
PREFIX sc: <http://purl.org/science/owl/sciencecommons/>
PREFIX tr: <http://www.thomsonreuters.com/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?place ?name WHERE {
	triple:document_2 schema:spatialCoverage ?place .
  	?place schema:name ?name .
}
```

## CQ_4.2

Return all temporal subjects of the `document_2`.

```
PREFIX sc: <http://purl.org/science/owl/sciencecommons/>
PREFIX tr: <http://www.thomsonreuters.com/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?time WHERE {
	triple:document_2 schema:temporalCoverage ?time .
}
```

## CQ_4.3

Return all keywords connected to `document_1`.

```
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?keywords ?name WHERE {
	triple:document_1 schema:keywords ?keywords .
  	?keywords schema:name ?name .
}
```
