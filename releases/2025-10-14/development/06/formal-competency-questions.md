## Formal Competency Questions (Iteration 5)

## CQ_6.1

Return all triples that have as subject the `profile_78`.

```
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?predicate ?object WHERE {
	triple:profile_1 ?predicate ?object .
}
```

## CQ_6.2

Return all author claimed by an account of the `document_56`.

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX pro: <http://purl.org/spar/pro/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?agent ?account WHERE {
	triple:document_56 pro:isDocumentContextFor ?role_in_time .
  	?role_in_time pro:isHeldBy ?agent .
  	?agent foaf:account ?account .
}
```

## CQ_6.3

Return all profiles associated with `account_45`.

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?profile WHERE {
	?profile foaf:account triple:account_109 .
}
```


## CQ_6.4

Return for `profile_34` the original profile.

```
PREFIX tr: <http://www.thomsonreuters.com/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?profile WHERE {
	triple:profile_123 triple:alsoKnowAs ?profile .
}
```

## CQ_6.5

Return all the fullname defined for the profile claimed by `account_109`.

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?profile ?fullname WHERE {
	?profile foaf:account triple:account_109 .
  	?profile foaf:name ?fullname .
}
```


