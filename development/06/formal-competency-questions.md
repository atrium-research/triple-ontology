## Formal Competency Questions (Iteration 6)

## CQ_6.1

Return all information about `profile_1`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?predicate ?object WHERE {
  triple:profile_1 ?predicate ?object .
}
```

**Expected Result:**
- All triples with profile_1 as subject (type, identifier, account, name)

## CQ_6.2

Return all authors of `document_56` that are associated with a user account.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?author ?account WHERE {
  triple:document_56 schema:author ?author .
  ?author foaf:account ?account .
}
```

**Expected Result:**
- author: profile_56, account: account_109
- author: profile_09, account: account_109
- author: profile_123, account: account_109

**Note:** profile_23 is an author of document_56 but is not returned because it's not associated with any account.

## CQ_6.3

Return all unassociated authors of `document_56` (authors without an account).

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?author ?name WHERE {
  triple:document_56 schema:author ?author .
  ?author schema:name ?name .
  FILTER NOT EXISTS { ?author foaf:account ?account }
}
```

**Expected Result:**
- author: profile_23, name: "Pierre Dupont"

## CQ_6.4

Return all profiles associated with `account_109`.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?profile ?name WHERE {
  ?profile foaf:account triple:account_109 ;
           schema:name ?name .
}
```

**Expected Result:**
- profile: profile_56, name: "Maria Rossi"
- profile: profile_09, name: "M. Rossi"
- profile: profile_123, name: "Maria R. Rossi"


## CQ_6.4

Return all documents authored by profiles associated with `account_109`.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT DISTINCT ?document ?authorProfile WHERE {
  ?authorProfile foaf:account triple:account_109 .
  ?document schema:author ?authorProfile .
}
```

**Expected Result:**
- document: document_56, authorProfile: profile_56
- document: document_56, authorProfile: profile_09
- document: document_56, authorProfile: profile_123
- document: document_67, authorProfile: profile_56
- document: document_98, authorProfile: profile_09
- document: document_42, authorProfile: profile_123


## CQ_6.5

Return all unassociated profiles (profiles without an account).

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?profile ?name WHERE {
  ?profile a triple:Profile ;
           schema:name ?name .
  FILTER NOT EXISTS { ?profile foaf:account ?account }
}
```

**Expected Result:**
- profile: profile_23, name: "Pierre Dupont"
