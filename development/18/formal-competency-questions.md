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
- `triple:document_it18_1` → `disc:methods_and_statistics` → "0.87"
- `triple:document_it18_2` → `disc:political_science` → "0.55"

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
- `triple:document_it18_1`

## CQ_18.3

Return the TRIPLE thesaurus concepts (knows_about) of each document, with their labels and the LCSH heading they correspond to.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?document ?concept ?label ?lcsh WHERE {
  ?document schema:about ?concept .
  ?concept a skos:Concept ;
           skos:prefLabel ?label .
  OPTIONAL { ?concept skos:exactMatch ?lcsh }
}
```

**Expected result:**
- `triple:document_it18_1` → <http://semantics.gr/authorities/SSH-LCSH/sh2008122106> → "Digital humanities" → <http://id.loc.gov/authorities/subjects/sh2008122106>
- `triple:document_it18_1` → <http://semantics.gr/authorities/SSH-LCSH/sh2008122106> → "Informatica umanistica" → <http://id.loc.gov/authorities/subjects/sh2008122106>
- `triple:document_it18_1` → <http://semantics.gr/authorities/SSH-LCSH/sh2008122106> → "Humanités numériques" → <http://id.loc.gov/authorities/subjects/sh2008122106>
- `triple:document_it18_2` → <http://semantics.gr/authorities/SSH-LCSH/sh85009407> → "Attitude (Psychology)" → <http://id.loc.gov/authorities/subjects/sh85009407>
- `triple:document_it18_2` → <http://semantics.gr/authorities/SSH-LCSH/sh85009407> → "Atteggiamento" → <http://id.loc.gov/authorities/subjects/sh85009407>
- `triple:document_it18_2` → <http://semantics.gr/authorities/SSH-LCSH/sh85009407> → "Attitude (psychologie)" → <http://id.loc.gov/authorities/subjects/sh85009407>

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
- "Digital methods and SSH research"
- "Métodos digitais e a pesquisa em CSH"

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
- `triple:document_it18_1` → "fr" → "fre"
- `triple:document_it18_2` → "en" → "und"