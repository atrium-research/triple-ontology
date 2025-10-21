## Formal Competency Questions (Iteration 10)

## CQ_10.1

Return all identifiers that use the DOI scheme.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?identifier WHERE {
  ?identifier a datacite:Identifier ;
              datacite:usesIdentifierScheme triple:doi .
}
```

**Expected result:**
- `triple:identifier_1`
- `triple:identifier_24`


## CQ_10.2

Return the identifier scheme used by `identifier_23`.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?scheme WHERE {
  triple:identifier_23 datacite:usesIdentifierScheme ?scheme .
}
```

**Expected result:**
- `triple:issn`


## CQ_10.3

Return all documents that have a DOI identifier.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document a foaf:Document ;
            datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme triple:doi .
}
```

**Expected result:**
- `triple:document_1`
- `triple:document_45`


## CQ_10.4

Return all identifier schemes defined in the ontology.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>

SELECT ?scheme WHERE {
  ?scheme a datacite:IdentifierScheme .
}
```

**Expected result:**
- `triple:doi`
- `triple:issn`
- `triple:isbn`
- `triple:handle`


## CQ_10.5

Return all identifiers of `document_45` along with their schemes.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?identifier ?scheme WHERE {
  triple:document_45 datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme ?scheme .
}
```

**Expected result:**
- `triple:identifier_23` → `triple:issn`
- `triple:identifier_24` → `triple:doi`


## CQ_10.6

Return the literal value of the DOI identifier for `document_1`.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?value WHERE {
  triple:document_1 datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme triple:doi ;
              litre:hasLiteralValue ?value .
}
```

**Expected result:**
- "10.1234/example.2024.001"


## CQ_10.7

Return all documents that have an ISBN identifier.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?document WHERE {
  ?document a foaf:Document ;
            datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme triple:isbn .
}
```

**Expected result:**
- `triple:document_99`


## CQ_10.8

Return all identifiers and their schemes for `document_78`.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?identifier ?scheme WHERE {
  triple:document_78 datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme ?scheme .
}
```

**Expected result:**
- `triple:identifier_90` → `triple:handle`


## CQ_10.9

Return all identifiers with their schemes and literal values.

```sparql
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?identifier ?scheme ?value WHERE {
  ?identifier a datacite:Identifier ;
              datacite:usesIdentifierScheme ?scheme ;
              litre:hasLiteralValue ?value .
}
```

**Expected result:**
- `triple:identifier_1` → `triple:doi` → "10.1234/example.2024.001"
- `triple:identifier_23` → `triple:issn` → "1234-5678"
- `triple:identifier_24` → `triple:doi` → "10.5678/journal.2024.045"
- `triple:identifier_90` → `triple:handle` → "11234/5678-abcd-efgh"
- `triple:identifier_110` → `triple:isbn` → "978-3-16-148410-0"
