# Formal Competency Questions (Iteration 16)

### CQ_16.1: Find the TRIPLE class that closely matches fabio:ScholarlyWork

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX fabio: <http://purl.org/spar/fabio/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?tripleClass
WHERE {
  ?tripleClass skos:closeMatch fabio:ScholarlyWork .
}
```

**Expected Result**: `triple:Document`

---

### CQ_16.2: Find the TRIPLE class that closely matches fabio:Dataset

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX fabio: <http://purl.org/spar/fabio/>

SELECT ?tripleClass
WHERE {
  ?tripleClass skos:closeMatch fabio:Dataset .
}
```

**Expected Result**: `triple:Dataset`

---

### CQ_16.3: Find the FOAF alignment of Profile

Every Profile denotes an agent, so the alignment is structural (issue #30, option A):
a subclass axiom, not a SKOS match.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?foafClass
WHERE {
  triple:Profile rdfs:subClassOf ?foafClass .
  FILTER(STRSTARTS(STR(?foafClass), STR(foaf:)))
}
```

**Expected Result**: `foaf:Agent`

---

### CQ_16.4: Check alignment for Project

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX frapo: <http://purl.org/cerif/frapo/>

SELECT ?tripleClass
WHERE {
  ?tripleClass skos:closeMatch frapo:Grant .
}
```

**Expected Result**: `triple:Project`

---

### CQ_16.5: Find matches for fabio:Work

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX fabio: <http://purl.org/spar/fabio/>

SELECT ?tripleClass
WHERE {
  ?tripleClass ?p fabio:Work .
  FILTER(?p IN (skos:exactMatch, skos:closeMatch))
}
ORDER BY ?tripleClass
```

**Expected Result**: `triple:MediaObject`, `triple:SemanticArtefact`
