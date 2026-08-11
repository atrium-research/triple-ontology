# Formal Competency Questions - Iteration 20

## CQ_20.1

Return all records of the same scholarly work, given its representative record.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?record WHERE {
  { ?record triple:isDuplicateOf triple:document_it20_rep }
  UNION
  { BIND(triple:document_it20_rep AS ?record) }
}
```

**Expected result:**
- `triple:document_it20_rep`
- `triple:document_it20_dup`

## CQ_20.2

Given a duplicate record, return the representative whose consolidated values are surfaced.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?representative WHERE {
  triple:document_it20_dup triple:isDuplicateOf ?representative .
}
```

**Expected result:**
- `triple:document_it20_rep`

## CQ_20.3

Return the deduplicated view: every document that is not a duplicate of another record.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?document WHERE {
  ?document a triple:Document .
  FILTER NOT EXISTS { ?document triple:isDuplicateOf ?rep }
}
ORDER BY ?document
```

**Expected result:**
- `triple:document_it20_rep`
- `triple:document_it20_single`

## CQ_20.4

How many records does each work have, counting the representative?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?representative (COUNT(?duplicate) + 1 AS ?records) WHERE {
  ?duplicate triple:isDuplicateOf ?representative .
}
GROUP BY ?representative
```

**Expected result:**
- `triple:document_it20_rep` → 2

## CQ_20.5

Return each duplicate with its provider and the headline of its representative.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?duplicate ?provider ?headline WHERE {
  ?duplicate triple:isDuplicateOf ?representative ;
             schema:provider/foaf:name ?provider .
  ?representative schema:headline ?headline .
}
```

**Expected result:**
- `triple:document_it20_dup` → "BASE" → "De l'esthétique au présent"
