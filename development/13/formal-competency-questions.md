## Formal Competency Questions (Iteration 13)

## CQ_13.1

Return all multimedia content available in the platform.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?multimedia ?title WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title .
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus"


## CQ_13.2

Return all video content with their duration and encoding format.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?video ?title ?duration ?format WHERE {
  ?video a triple:MediaObject ;
         schema:headline ?title ;
         schema:duration ?duration ;
         schema:encodingFormat ?format .
  # Filter for video content based on encoding format
  FILTER(CONTAINS(?format, "video/"))
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "PT1H25M30S" → "video/mp4"


## CQ_13.3

Return all multimedia content with their file size and access conditions.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?multimedia ?title ?size ?access WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              schema:size ?size ;
              schema:conditionsOfAccess ?access .
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "1.2 GB" → "Open Access"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → "198 MB" → "Open Access with attribution"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → "850 MB" → "Educational and Research Use"


## CQ_13.4

Return all multimedia content that covers medieval history topics.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX sioc: <http://rdfs.org/sioc/ns#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?multimedia ?title ?topic WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              sioc:topic ?topic_uri .
  ?topic_uri skos:prefLabel ?topic .
  FILTER(CONTAINS(LCASE(?topic), "medieval"))
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "Medieval History"


## CQ_13.5

Return all audio recordings with their language and temporal coverage.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?audio ?title ?language ?temporal WHERE {
  ?audio a triple:MediaObject ;
         schema:headline ?title ;
         schema:inLanguage ?language ;
         schema:temporalCoverage ?temporal ;
         schema:encodingFormat ?format .
  # Filter for audio content based on encoding format
  FILTER(CONTAINS(?format, "audio/"))
}
```

**Expected result:**
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → "it" → "1943-1945"


## CQ_13.6

Return all multimedia content with their producers and providers.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?multimedia ?title ?producer ?provider WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title .
  OPTIONAL { ?multimedia schema:producer ?producer }
  OPTIONAL { ?multimedia schema:provider ?provider }
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "CERIMES" → "Canal-U"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → null → "ISIDORE"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → "Uffizi Digital Archive" → "Europeana"


## CQ_13.7

Return all multimedia content with Creative Commons licenses.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?multimedia ?title ?license WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              schema:license ?license .
  FILTER(CONTAINS(?license, "CC"))
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "CC BY-NC-ND 4.0"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → "CC BY-SA 4.0"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → "CC BY-NC 4.0"


## CQ_13.8

Return all multimedia content with their spatial coverage and subject topics.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX sioc: <http://rdfs.org/sioc/ns#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?multimedia ?title ?spatial ?topic WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              schema:spatialCoverage ?spatial ;
              sioc:topic ?topic_uri .
  ?topic_uri skos:prefLabel ?topic .
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "Europe occidentale" → "Medieval History"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → "Italy" → "European History"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → "Florence, Italy" → "Art History"


## CQ_13.9

Return all multimedia content that references other documents.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?multimedia ?title ?referencedDoc ?docTitle WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              dcterms:isReferencedBy ?referencedDoc .
  ?referencedDoc schema:headline ?docTitle .
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "triple:document-medieval-anthology-2023" → "Medieval Studies Anthology 2023"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → "triple:document-botticelli-analysis-2023" → "Digital Analysis of Botticelli's Techniques"


## CQ_13.10

Return all multimedia content with their descriptive keywords.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?multimedia ?title ?keyword ?keywordName WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              schema:keywords ?keyword .
  ?keyword schema:name ?keywordName .
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → `triple:keyword-histoire-medievale` → "histoire médiévale"
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → `triple:keyword-renaissance-carolingienne` → "renaissance carolingienne"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → `triple:keyword-oral-history` → "oral history"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → `triple:keyword-renaissance-art` → "Renaissance art"


## CQ_13.11

Return all multimedia content that have DOI identifiers using class-based approach.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?multimedia ?title ?identifierValue WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              datacite:hasIdentifier ?identifier .
  ?identifier a triple:DOI ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "10.5281/zenodo.video.medieval.carolingian"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → "10.5281/zenodo.audio.resistance.interview"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → "10.5281/zenodo.image.birth.venus.hd"


## CQ_13.12

Return all multimedia content that have Handle identifiers using class-based approach.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?multimedia ?title ?identifierValue WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              datacite:hasIdentifier ?identifier .
  ?identifier a triple:Handle ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → "21.11130/00-VIDEO-MEDIEVAL-CAROLINGIAN"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → "21.11130/00-AUDIO-RESISTANCE-INTERVIEW"
- `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → "21.11130/00-IMAGE-BIRTH-VENUS-HD"


## CQ_13.13

Return all multimedia content with platform identifiers by type.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?multimedia ?title ?identifierType ?value WHERE {
  ?multimedia a triple:MediaObject ;
              schema:headline ?title ;
              datacite:hasIdentifier ?identifier .
  ?identifier a ?identifierType ;
              litre:hasLiteralValue ?value .
  FILTER (?identifierType IN (triple:ID, triple:PID, triple:OriginalIdentifier))
}
```

**Expected result:**
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → `triple:ID` → "TRIPLE_MEDIA_VIDEO_001"
- `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → `triple:PID` → "gotriple:media:video-medieval-carolingian"
- `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → `triple:ID` → "TRIPLE_MEDIA_AUDIO_002"

