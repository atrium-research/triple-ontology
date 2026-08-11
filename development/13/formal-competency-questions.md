# Formal Competency Questions (Iteration 13)

## CQ_13.1

What is the CIDOC-CRM equivalent for a TRIPLE Document?

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

## CQ_13.2

What is the SSHOC-RO equivalent for a TRIPLE Project?

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

## CQ_13.3

How are Multimedia Objects represented in CIDOC-CRM?

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


## CQ_13.4

Which SSHOC class corresponds to a TRIPLE Dataset?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sshocro: <https://sshoc.eu/ontology/>

SELECT ?sshocClass
WHERE {
  triple:Dataset skos:closeMatch ?sshocClass .
  FILTER(STRSTARTS(STR(?sshocClass), STR(sshocro:)))
}
```

**Expected Results:**
- `sshoc:SHE1_Dataset` (a close match: the SSHOC-RO dataset class is the retrieval-level counterpart, not an identity)

