## Formal Competency Questions (Iteration 6)

## CQ_6.1

Return all information about `profile_1`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?predicate ?object WHERE {
  triple:profile_1 ?predicate ?object .
}
```

**Expected Result:**
- All triples with profile_1 as subject (type, identifier, account, name, alsoKnownAs)

## CQ_6.2

Return all authors of `document_56` that are claimed by an account.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?author ?account WHERE {
  triple:document_56 schema:author ?author .
  ?author foaf:account ?account .
}
```

**Expected Result:**
- author: profile_56, account: account_109
- author: profile_09, account: account_109
- author: profile_123, account: account_109

**Note:** profile_23 is an author of document_56 but is not returned because it's unclaimed (has no account).

## CQ_6.3

Return all unclaimed authors of `document_56`.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?author ?name WHERE {
  triple:document_56 schema:author ?author .
  ?author schema:name ?name .
  FILTER NOT EXISTS { ?author foaf:account ?account }
}
```

**Expected Result:**
- author: profile_23, name: "author_fullname_9"

## CQ_6.4

Return all profiles claimed by `account_109`.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?profile ?name WHERE {
  ?profile foaf:account triple:account_109 ;
           schema:name ?name .
}
```

**Expected Result:**
- profile: profile_56, name: "author_fullname_6"
- profile: profile_09, name: "author_fullname_7"
- profile: profile_123, name: "author_fullname_8"

## CQ_6.5

Return the original profile for `profile_123`.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?originalProfile WHERE {
  triple:profile_123 triple:alsoKnownAs ?originalProfile .
}
```

**Expected Result:**
- originalProfile: profile_56

## CQ_6.6

Return all documents authored by profiles claimed by `account_109`.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

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

## CQ_6.7

Return all profiles that link to `profile_56` as their original (disambiguated) profile.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?profile WHERE {
  ?profile triple:alsoKnownAs triple:profile_56 .
}
```

**Expected Result:**
- profile: profile_09
- profile: profile_123

## CQ_6.8

Return all fullnames for profiles claimed by `account_109`.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?profile ?fullname WHERE {
  ?profile foaf:account triple:account_109 ;
           schema:name ?fullname .
}
```

**Expected Result:**
- profile: profile_56, fullname: "Maria Rossi"
- profile: profile_09, fullname: "M. Rossi"
- profile: profile_123, fullname: "Maria R. Rossi"

## CQ_6.9

Return all profiles with family name "Rossi" and their given names.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?profile ?givenName ?familyName ?fullName WHERE {
  ?profile a triple:Profile ;
           schema:familyName ?familyName ;
           schema:givenName ?givenName ;
           schema:name ?fullName .

  FILTER(?familyName = "Rossi")
}
ORDER BY ?givenName
```

**Expected Result:**
- profile: profile_09, givenName: "M.", familyName: "Rossi", fullName: "M. Rossi"
- profile: profile_56, givenName: "Maria", familyName: "Rossi", fullName: "Maria Rossi"
- profile: profile_123, givenName: "Maria R.", familyName: "Rossi", fullName: "Maria R. Rossi"

