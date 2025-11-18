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
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
	
SELECT ?type WHERE {
  triple:document_1 schema:additionalType ?type .
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
PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?documents WHERE {
 ?documents schema:inLanguage triple:language_10 .
 ?documents schema:additionalType triple:type_5 .
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
  ?identifier datacite:usesIdentiferScheme triple:landing_page_url_schema ;
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
  FILTER (?scheme IN (triple:landing_page_url_schema, triple:full_text_url_schema, triple:source_url_schema))
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
  ?identifier datacite:usesIdentiferScheme triple:internal_id_schema ;
              litre:hasLiteralValue ?internal_id .
}
```

## CQ_1.15_NEW

Return the internal ID for `triple:document_1` using class-based approach.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?internal_id WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier a triple:ID ;
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
  ?identifier datacite:usesIdentiferScheme triple:pid_schema ;
              litre:hasLiteralValue ?pid .
}
```

## CQ_1.16_NEW

Return the PID (persistent identifier) for `triple:document_1` using class-based approach.

```
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?pid WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier a triple:PID ;
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
  FILTER (?scheme IN (triple:internal_id_schema, triple:pid_schema, triple:original_id_schema))
}
```

## CQ_1.17_NEW

Return all platform identifiers (internal, PID, original) for `triple:document_1` using class-based approach.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?identifier ?type ?value WHERE {
  triple:document_1 datacite:hasIdentifer ?identifier .
  ?identifier a ?type ;
              litre:hasLiteralValue ?value .
  FILTER (?type IN (triple:ID, triple:PID, triple:OriginalIdentifier))
}
```

## CQ_1.18

Return all documents that have a specific type of identifier.

```
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?document WHERE {
  ?document rdf:type triple:Document ;
            datacite:hasIdentifer ?identifier .
  ?identifier a triple:ID .
}
```
