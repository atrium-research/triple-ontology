## Formal Competency Questions (Iteration 1)

## CQ_1.1

Return the language associated with `triple:document_1`.

```
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?language WHERE {
  triple:document_1 schema:inLanguage ?language .
}
```

## CQ_1.2

Return the identifiers associated with `document_1`.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?ids WHERE {
  triple:document_1 datacite:hasIdentifer ?ids .
}
```
## CQ_1.3

Return the types associated with `document_1`.

```
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
	
SELECT ?type WHERE {
  triple:document_1 dc:type ?type .
}
```

## CQ_1.4
Return all `documents`.

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?documents WHERE {
 ?documents rdf:type foaf:Document .
}
```

## CQ_1.5
Return all `languages`.

```
PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?languages WHERE {
 ?languages rdf:type schema:Language .
}
```

## CQ_1.6
Return all documents, given the `type_5` and the language `language_10`.

```
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?documents WHERE {
 ?documents schema:inLanguage triple:language_10 .
 ?documents dc:type triple:type_5 .
}
```
