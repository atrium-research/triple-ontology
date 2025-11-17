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
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?documents WHERE {
 ?documents rdf:type triple:Document .
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

## CQ_1.8

Return the title (headline) of `triple:document_1` in English.

```
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?headline WHERE {
  triple:document_1 schema:headline ?headline .
  FILTER (lang(?headline) = "en")
}
```

## CQ_1.9

Return all titles (headlines) associated with `triple:document_1`.

```
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?headline WHERE {
  triple:document_1 schema:headline ?headline .
}
```

## CQ_1.10

Return the abstract of `triple:document_31`.

```
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?abstract WHERE {
  triple:document_31 schema:abstract ?abstract .
}
```

## CQ_1.11

Return the encoding format of all documents.

```
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?document ?format WHERE {
  ?document rdf:type triple:Document .
  ?document schema:encodingFormat ?format .
}
```

## CQ_1.12

Return all documents in PDF format.

```
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?document WHERE {
  ?document rdf:type triple:Document .
  ?document schema:encodingFormat "application/pdf" .
}
```

## CQ_1.13

Return the landing page URL of `triple:document_1`.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?url WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier datacite:usesIdentiferScheme triple:landing_page_url ;
              litre:hasLiteralValue ?url .
}
```

## CQ_1.14

Return all URL-based identifiers (landing page, full text, source) for `triple:document_1`.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?identifier ?scheme ?url WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier datacite:usesIdentiferScheme ?scheme ;
              litre:hasLiteralValue ?url .
  FILTER (?scheme IN (triple:landing_page_url, triple:full_text_url, triple:source_url))
}
```

## CQ_1.15

Return the internal ID for `triple:document_1`.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?internal_id WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier datacite:usesIdentiferScheme triple:internal_id ;
              litre:hasLiteralValue ?internal_id .
}
```

## CQ_1.16

Return the PID (persistent identifier) for `triple:document_1`.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?pid WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier datacite:usesIdentiferScheme triple:pid ;
              litre:hasLiteralValue ?pid .
}
```

## CQ_1.17

Return all platform identifiers (internal, PID, original) for `triple:document_1`.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?identifier ?scheme ?value WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier datacite:usesIdentiferScheme ?scheme ;
              litre:hasLiteralValue ?value .
  FILTER (?scheme IN (triple:internal_id, triple:pid, triple:original_id))
}
```
