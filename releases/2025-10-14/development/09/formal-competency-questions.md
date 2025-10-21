## Formal Competency Questions (Iteration 9)

## CQ_9.1

Return all documents with "Open access" conditions.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document a foaf:Document ;
            schema:conditionsOfAccess triple:acc_open-access .
}
```

**Expected result:**
- `triple:document_1`


## CQ_9.2

Return the vocabulary scheme to which `acc_embargoed-access` belongs.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?scheme WHERE {
  triple:acc_embargoed-access skos:inScheme ?scheme .
}
```

**Expected result:**
- `triple:conditions_of_access`


## CQ_9.3

Return all external COAR terms that exactly match the access conditions in the GoTriple vocabulary.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?accessTerm ?coarTerm WHERE {
  ?accessTerm skos:inScheme triple:conditions_of_access ;
              skos:exactMatch ?coarTerm .
  FILTER(STRSTARTS(STR(?coarTerm), "https://vocabularies.coar-repositories.org/access_rights/"))
}
```

**Expected result:**
- `triple:acc_embargoed-access` → `https://vocabularies.coar-repositories.org/access_rights/c_f1cf/`
- `triple:acc_metadata-only-access` → `https://vocabularies.coar-repositories.org/access_rights/c_14cb/`
- `triple:acc_open-access` → `https://vocabularies.coar-repositories.org/access_rights/c_abf2/`
- `triple:acc_restricted-access` → `https://vocabularies.coar-repositories.org/access_rights/c_16ec/`


## CQ_9.4

Return the access condition of `document_23`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?accessCondition WHERE {
  triple:document_23 schema:conditionsOfAccess ?accessCondition .
}
```

**Expected result:**
- `triple:acc_embargoed-access`


## CQ_9.5

Return all access condition terms in the controlled vocabulary.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?accessTerm WHERE {
  ?accessTerm skos:inScheme triple:conditions_of_access .
}
```

**Expected result:**
- `triple:acc_embargoed-access`
- `triple:acc_metadata-only-access`
- `triple:acc_open-access`
- `triple:acc_restricted-access`
- (... other access condition terms)


## CQ_9.6

Return all documents that have metadata-only access.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document a foaf:Document ;
            schema:conditionsOfAccess triple:acc_metadata-only-access .
}
```

**Expected result:**
- `triple:document_56`


## CQ_9.7

Return the COAR external term that exactly matches `acc_open-access`.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?coarTerm WHERE {
  triple:acc_open-access skos:exactMatch ?coarTerm .
}
```

**Expected result:**
- `https://vocabularies.coar-repositories.org/access_rights/c_abf2/`
