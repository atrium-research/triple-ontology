# Formal Competency Questions (Iteration 15)

## CQ_15.1 - Unified Retrieval
Return all entities mentioned in "Document1", regardless of type or source.

```sparql
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?doc ?entityName WHERE {
    ?ann oa:hasTarget triple:Document1 ;
         oa:hasBody ?entity .
    
    # Optional name matching for different types
    OPTIONAL { ?entity schema:name ?entityName }
    OPTIONAL { ?entity skos:prefLabel ?entityName }
}
```

## CQ_15.2 - External Entities
Return only external entities (e.g., Wikidata) mentioned in "Document1".

```sparql
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?entity WHERE {
    ?ann oa:hasTarget triple:Document1 ;
         oa:hasBody ?entity .
    filter(regex(str(?entity), "wikidata.org"))
}
```

## CQ_15.3 - New Local Entities
Return only newly created local entities (Dual Typed or internal).

```sparql
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?entity WHERE {
    ?ann oa:hasTarget triple:Document1 ;
         oa:hasBody ?entity .
    
    FILTER (STRSTARTS(STR(?entity), "https://gotriple.eu/ontology/triple#"))
}
```

## CQ_15.4 - Retrieve Annotations from Document
Retrieve all annotations connected to the document via `schema:mentions`.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX oa: <http://www.w3.org/ns/oa#>

SELECT ?annotation ?body WHERE {
    triple:Document1 schema:mentions ?annotation .
    ?annotation oa:hasBody ?body .
}
```

## CQ_15.5 - Filter by Type (Place)
Return only Places mentioned.

```sparql
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?entity WHERE {
    ?ann oa:hasTarget triple:Document1 ;
         oa:hasBody ?entity .
    ?entity a schema:Place .
}
```
