## Formal Competency Questions (Iteration 8)

## CQ_8.1

Return all documents with type "Book part".

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX schema: <http://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document a foaf:Document ;
            schema:additionalType triple:typ_book-part .
}
```

**Expected result:**
- `triple:document_1`
- `triple:document_45`


## CQ_8.2

Return the vocabulary scheme to which `typ_book-part` belongs.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?scheme WHERE {
  triple:typ_book-part skos:inScheme ?scheme .
}
```

**Expected result:**
- `triple:content_types`


## CQ_8.3

Return all external terms that exactly match `typ_book-part`.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?externalTerm WHERE {
  triple:typ_book-part skos:exactMatch ?externalTerm .
}
```

**Expected result:**
- `https://vocabularies.coar-repositories.org/resource_types/c_3248/`


## CQ_8.4

Return the type of `document_1`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?type WHERE {
  triple:document_1 schema:additionalType ?type .
}
```

**Expected result:**
- `triple:typ_book-part`


## CQ_8.5

Return all content types in the controlled vocabulary.

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?docType WHERE {
  ?docType skos:inScheme triple:content_types .
}
```

**Expected result:**
- `triple:typ_book-part`
- (... other content type terms from the vocabulary)
