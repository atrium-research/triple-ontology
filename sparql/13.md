# Formal Competency Questions (Iteration 13)

### CQ_13.1: Find CIDOC-CRM equivalent for Document

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT ?cidocClass
WHERE {
  triple:Document skos:exactMatch ?cidocClass .
  FILTER(STRSTARTS(STR(?cidocClass), STR(cidoc:)))
}
```

### CQ_13.2: Find the SSHOC-RO counterpart of Project (close match)

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sshocro: <https://sshoc.eu/ontology/>

SELECT ?sshocClass
WHERE {
  triple:Project skos:closeMatch ?sshocClass .
  FILTER(STRSTARTS(STR(?sshocClass), STR(sshocro:)))
}
```

### CQ_13.3: Find matches for MediaObject in CIDOC

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT ?matchType ?cidocClass
WHERE {
  triple:MediaObject ?matchType ?cidocClass .
  FILTER(STRSTARTS(STR(?cidocClass), STR(cidoc:)))
}
```
