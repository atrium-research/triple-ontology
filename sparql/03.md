## Formal Competency Questions (Iteration 1)

## CQ_2.1

Return all roles connected to `document_1`.

```
SELECT DISTINCT ?roles ?startDate ?endDate WHERE {
 triple:document_1 pro:isDocumentContextFor ?roles_in_time .
 ?roles_in_time pro:withRole ?roles .
}
```

## CQ_2.1

Return all roles connected to `document_1` and with the respective year.

```
PREFIX pro: <http://purl.org/spar/pro/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?roles ?startDate ?endDate WHERE {
 triple:document_1 pro:isDocumentContextFor ?roles_in_time .
 ?roles_in_time pro:withRole ?roles .
 OPTIONAL {
   ?roles_in_time tvc:atTime ?timeInterval .
   OPTIONAL { ?timeInterval ti:hasIntervalStartDate ?startDate . }
   OPTIONAL { ?timeInterval ti:hasIntervalEndDate ?endDate . }
 }
}
```

## CQ_2.1

Return all roles connected to `document_1` with the respective years and all agent associated with.

```
PREFIX pr: <http://purl.org/ontology/prv/core#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ti: <http://www.ontologydesignpatterns.org/cp/owl/timeinterval.owl#>
PREFIX tr: <http://www.thomsonreuters.com/>
PREFIX tvc: <http://www.essepuntato.it/2012/04/tvc/>
PREFIX pro: <http://purl.org/spar/pro/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?roles ?name ?startDate ?endDate WHERE {
 triple:document_1 pro:isDocumentContextFor ?roles_in_time .
 ?roles_in_time pro:withRole ?roles .
 ?roles_in_time pro:isHeldBy ?agent.
  ?agent foaf:name ?name .
 OPTIONAL {
   ?roles_in_time tvc:atTime ?timeInterval .
   OPTIONAL { ?timeInterval ti:hasIntervalStartDate ?startDate . }
   OPTIONAL { ?timeInterval ti:hasIntervalEndDate ?endDate . }
 }
}
```