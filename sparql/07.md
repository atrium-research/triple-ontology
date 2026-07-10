## Formal Competency Questions (Iteration 7)

## CQ_7.1

What are all the metadata properties and values associated with a specific project?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?identifierValue ?startDate ?endDate ?name ?alternateName ?description
       ?topicLabel ?keywordName ?grant
WHERE {
  BIND(triple:project_1 AS ?project)

  # Identifier
  OPTIONAL {
    ?project datacite:hasIdentifier ?identifier .
    ?identifier litre:hasLiteralValue ?identifierValue .
  }

  # Temporal information
  OPTIONAL { ?project schema:startDate ?startDate . }
  OPTIONAL { ?project schema:endDate ?endDate . }

  # Names and descriptions
  OPTIONAL { ?project schema:name ?name . }
  OPTIONAL { ?project schema:alternateName ?alternateName . }
  OPTIONAL { ?project schema:description ?description . }

  # Topics
  OPTIONAL {
    ?project schema:about ?topic .
    ?topic rdfs:label ?topicLabel .
  }

  # Keywords
  OPTIONAL {
    ?project schema:keywords ?keyword .
    ?keyword schema:name ?keywordName .
  }

  # Funding
  OPTIONAL { ?project schema:funding ?grant . }
}
```

**Expected Results:**
- project_1 metadata including H2020-863420, dates 2019-01-01 to 2022-12-31, multilingual names, Digital Humanities topic, 3 keywords, and grant_1


## CQ_7.2

What are all the funding grants associated with a project, and who are the funders and sponsors for each grant?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?grant ?funderName ?sponsorName
WHERE {
  BIND(triple:project_1 AS ?project)

  ?project schema:name ?projectName .
  ?project schema:funding ?grant .

  OPTIONAL {
    ?grant schema:funder ?funder .
    ?funder schema:name ?funderName .
  }

  OPTIONAL {
    ?grant schema:sponsor ?sponsor .
    ?sponsor schema:name ?sponsorName .
  }
}
```

**Expected Results:**
- project_1, "Transforming Research...", grant_1, "European Commission", "European Research Executive Agency"


## CQ_7.3

Which projects have multiple funders or sponsors?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName (COUNT(DISTINCT ?grant) AS ?grantCount)
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:funding ?grant .
}
GROUP BY ?project ?projectName
HAVING (COUNT(DISTINCT ?grant) > 1)
ORDER BY DESC(?grantCount)
```

**Expected Results:**
- project_3, "Digital Documentation of Endangered Cultural Heritage in the Balkans", 2 grants


## CQ_7.4

What projects are associated with a specific discipline or topic (e.g., Digital Humanities)?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?alternateName ?topicLabel
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:about ?topic .

  ?topic rdfs:label ?topicLabel .

  OPTIONAL { ?project schema:alternateName ?alternateName . }

  FILTER(REGEX(?topicLabel, "Digital Humanities", "i"))
}
ORDER BY ?projectName
```

**Expected Results:**
- project_1 (TRIPLE) and project_3 (BALKAN-HERITAGE)


## CQ_7.5

What is the duration of each project (time span between start and end dates)?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?startDate ?endDate
       ((?endDate - ?startDate) AS ?durationDays)
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:startDate ?startDate ;
           schema:endDate ?endDate .

  FILTER(LANG(?projectName) = "en")
}
ORDER BY DESC(?durationDays)
```

**Expected Results:**
- All 4 projects with calculated durations (project_4 longest at ~1826 days / 5 years)


## CQ_7.6

Which projects were active during a specific time period (e.g., year 2022)?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?alternateName ?startDate ?endDate
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:startDate ?startDate ;
           schema:endDate ?endDate .

  OPTIONAL { ?project schema:alternateName ?alternateName . }

  # Project active in 2022 if start <= 2022-12-31 AND end >= 2022-01-01
  FILTER(?startDate <= "2022-12-31"^^xsd:date && ?endDate >= "2022-01-01"^^xsd:date)
  FILTER(LANG(?projectName) = "en")
}
ORDER BY ?startDate
```

**Expected Results:**
- All 4 projects were active at some point during 2022


## CQ_7.7

What are all the identifier schemes used for projects and their corresponding identifier values?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?schemeLabel ?identifierValue
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           datacite:hasIdentifier ?identifier .

  ?identifier datacite:usesIdentifierScheme ?scheme ;
              litre:hasLiteralValue ?identifierValue .

  ?scheme rdfs:label ?schemeLabel .

  FILTER(LANG(?projectName) = "en")
}
ORDER BY ?project ?schemeLabel
```

**Expected Results:**
- project_1: Horizon 2020 → H2020-863420
- project_2: PRIN → PRIN-2018ABCD123
- project_3: FWF → FWF-P-34567, Getty → GETTY-KIM-2021-15
- project_4: ERC → ERC-ADG-101052789


## CQ_7.8

Which organizations fund or sponsor multiple projects?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?organization ?orgName (COUNT(DISTINCT ?project) AS ?projectCount)
WHERE {
  {
    # Organizations as funders
    ?project a triple:Project ;
             schema:funding ?grant .
    ?grant schema:funder ?organization .
  }
  UNION
  {
    # Organizations as sponsors
    ?project a triple:Project ;
             schema:funding ?grant .
    ?grant schema:sponsor ?organization .
  }

  ?organization schema:name ?orgName .
}
GROUP BY ?organization ?orgName
HAVING (COUNT(DISTINCT ?project) > 1)
ORDER BY DESC(?projectCount)
```

**Expected Results:**
- (Empty result set with current data - all organizations fund only one project)


## CQ_7.9

What keywords are most frequently associated with projects in the platform?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?keywordName (COUNT(?project) AS ?frequency)
WHERE {
  ?project a triple:Project ;
           schema:keywords ?keyword .

  ?keyword schema:name ?keywordName .
}
GROUP BY ?keywordName
ORDER BY DESC(?frequency) ?keywordName
```

**Expected Results:**
- All keywords with frequency 1 in current dataset


## CQ_7.10

Retrieve projects by searching for specific keywords in their names, descriptions, or acronyms?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT DISTINCT ?project ?projectName ?alternateName ?description
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName .

  OPTIONAL { ?project schema:alternateName ?alternateName . }
  OPTIONAL { ?project schema:description ?description . }

  # Search term
  FILTER(
    REGEX(?projectName, "heritage", "i") ||
    REGEX(?alternateName, "heritage", "i") ||
    REGEX(?description, "heritage", "i")
  )
}
```

**Expected Results:**
- project_3 (BALKAN-HERITAGE) - contains "heritage" in multiple fields


## CQ_7.11

Which organization is the organizer of a specific project?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?organizerName
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:organizer ?organizer .

  ?organizer schema:name ?organizerName .
}
```

**Expected Results:**
- project_1: Austrian Centre for Digital Humanities and Cultural Heritage
- project_2: University of Bologna...
- project_3: University of Vienna...


## CQ_7.12

What topics does a project "know about" (areas of expertise)?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?topicLabel
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:knowsAbout ?topic .

  ?topic rdfs:label ?topicLabel .
}
```

**Expected Results:**
- project_2: Migration Studies


## CQ_7.13

What is the main web page (URL) associated with the project?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?url
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:mainEntityOfPage ?url .
}
```

**Expected Results:**
- project_1: https://triple.eu/projects/1
- project_2: https://miguris.project.it
- project_4: https://erc.europa.eu/projects/hellenistic


## CQ_7.14

What is the language of the project content?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?language
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:inLanguage ?language .
}
```

**Expected Results:**
- project_1: en
- project_2: it
- project_3: en
- project_4: en


## CQ_7.15

What is the contact point email for a specific project?

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?project ?projectName ?email
WHERE {
  ?project a triple:Project ;
           schema:name ?projectName ;
           schema:contactPoint ?contact .

  ?contact schema:email ?email .
}
```

**Expected Results:**

## CQ_7.16

What is the type of a specific project (e.g., Research, Training, Network)?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?project ?projectName ?typeLabel
WHERE {
  ?project a triple:Project ;
           triple:hasProjectType ?type .

  ?type rdfs:label ?typeLabel .
  
  OPTIONAL { ?project schema:name ?projectName . }
}
```

**Expected Results:**
- project_1: Network/Infrastructure
- project_2: Research Project
