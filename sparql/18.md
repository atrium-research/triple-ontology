# Formal Competency Questions (Iteration 18)

## CQ_18.1

Return the disciplines assigned to each document together with the classifier's confidence.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX oa: <http://www.w3.org/ns/oa#>

SELECT ?document ?discipline ?confidence WHERE {
  ?annotation oa:motivatedBy oa:classifying ;
              oa:hasTarget ?document ;
              oa:hasBody ?discipline ;
              triple:confidence ?confidence .
}
```

**Expected result:**
- `document_it18_1` → `Discipline/methods_and_statistics` → 0.87
- `document_it18_2` → `Discipline/political_science` → 0.55

## CQ_18.2

Return the documents classified under a discipline with confidence of at least 0.8.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX oa: <http://www.w3.org/ns/oa#>

SELECT ?document WHERE {
  ?annotation oa:motivatedBy oa:classifying ;
              oa:hasTarget ?document ;
              triple:confidence ?confidence .
  FILTER(?confidence >= 0.8)
}
```

**Expected result:**
- `document_it18_1`

## CQ_18.3

Return the keywords (knows_about) of each document, with their labels and, when available, their external URI.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?document ?keyword ?label ?uri WHERE {
  ?document triple:knowsAbout ?keyword .
  ?keyword schema:name ?label .
  OPTIONAL { ?keyword schema:sameAs ?uri }
}
```

**Expected result:**
- `document_it18_1` → `kw_text-mining_it18` → "Text mining"@en → `wikidata:Q676880`
- `document_it18_1` → `kw_text-mining_it18` → "Fouille de textes"@fr → `wikidata:Q676880`
- `document_it18_2` → `kw_public-opinion_it18` → "Public opinion"@en → (unbound)

## CQ_18.4

Return the title versions of `triple:document_it18_1` that are machine translations.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?headline WHERE {
  triple:document_it18_1 schema:headline ?headline ;
                         triple:machineTranslatedLanguage ?mt .
  FILTER(lang(?headline) = ?mt)
}
```

**Expected result:**
- "Digital methods and SSH research"@en
- "Métodos digitais e a pesquisa em CSH"@pt

## CQ_18.5

Return the documents whose detected language differs from the raw language declared by the provider (`triple:originalLanguage`, iteration 17).

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?document ?detected ?original WHERE {
  ?document triple:detectedLanguage ?detected ;
            triple:originalLanguage ?original .
  FILTER(?detected != ?original)
}
```

**Expected result:**
- `document_it18_2` → "en" / "und"
- `document_it18_1` → "fr" / "fre" (the provider used an ISO 639-2 code; the detector emits ISO 639-1)
