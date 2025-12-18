# Formal Competency Questions (Iteration 15)

## CQ_15.1 - Unified Retrieval
Return all people mentioned in "Document1", regardless of whether they are external (Wikidata), internal, or new local entities.

```sparql
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX schema: <http://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?doc ?entityName WHERE {
    ?ann oa:hasTarget triple:Document1 ;
         oa:hasBody ?entity .
    
    # Matches both Wikidata URIs and Local URIs thanks to type assertions
    ?entity a schema:Person ; 
            schema:name|skos:prefLabel ?entityName . 
}
```

## CQ_15.2 - External Entities
Return only external entities (e.g., Wikidata) mentioned in "Document1".

```sparql
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX schema: <http://schema.org/>

SELECT ?entity WHERE {
    ?ann oa:hasTarget triple:Document1 ;
         oa:hasBody ?entity .
    filter(regex(str(?entity), "wikidata.org"))
}
```

## CQ_15.3 - New Local Entities
Return only newly created local entities (Dual Typed).

```sparql
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX schema: <http://schema.org/>

SELECT ?entity WHERE {
    ?ann oa:hasTarget <https://gotriple.eu/ontology/triple/Document1> ;
         oa:hasBody ?entity .
    
    ?entity a skos:Concept .
}
```
