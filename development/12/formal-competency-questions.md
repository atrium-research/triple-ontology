# Formal Competency Questions - Iteration 12

## Semantic Artefact Resource Type

## CQ_12.1

Retrieve all semantic artifacts with their basic metadata (title, abstract, publisher)

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?artifact ?title ?abstract ?publisherName WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           schema:abstract ?abstract ;
           schema:publisher ?publisher .
  ?publisher schema:name ?publisherName .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus", "Controlled vocabulary for Social Sciences and Humanities research classification", "GoTriple Consortium"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary", "Comprehensive vocabulary for art historical concepts and terminology", "Digital Humanities Institute"
- `triple:ontology-medieval` → "Medieval Studies Ontology", "Formal ontology for medieval studies research domain", "University of Bologna"

## CQ_12.2

Find semantic artifacts with DOI or Handle persistent identifiers

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?artifact ?title ?identifierValue ?schemeLabel WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           datacite:hasIdentifier ?identifier .
  ?identifier litre:hasLiteralValue ?identifierValue ;
             datacite:usesIdentifierScheme ?scheme .
  ?scheme rdfs:label ?schemeLabel .
  FILTER(?scheme = triple:doi || ?scheme = triple:handle)
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus", "10.5281/zenodo.1234567", "DOI"
- `triple:ontology-medieval` → "Medieval Studies Ontology", "hdl:1234.5/medieval-ontology", "Handle"

## CQ_12.3

List all representation techniques used by semantic artifacts

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT DISTINCT ?technique WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:encodingFormat ?technique .
}
```

**Expected result:**
- "SKOS vocabulary"
- "OWL ontology"  
- "XML schema"
- "RDF Schema"

## CQ_12.4

Find semantic artifacts and the documents that reference them

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?artifact ?artifactTitle ?document ?documentTitle WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?artifactTitle ;
           dcterms:isReferencedBy ?document .
  ?document a triple:Document ;
           schema:headline ?documentTitle .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus", `triple:document-dh-methodology` → "Digital Humanities Methodology Paper"
- `triple:ontology-medieval` → "Medieval Studies Ontology", `triple:document-carolingian` → "Carolingian Renaissance Research Article"

## CQ_12.5

Retrieve semantic artifacts with their file formats and download URLs

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>

SELECT ?artifact ?title ?fileFormat WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           schema:fileFormat ?fileFormat .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus", "application/rdf+xml"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary", "text/turtle"
- `triple:ontology-medieval` → "Medieval Studies Ontology", "application/owl+xml"


## CQ_12.6

Return all semantic artifacts that have DOI identifiers using class-based approach.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?artifact ?title ?identifierValue WHERE {
  ?artifact a triple:SemanticArtefact ;
            schema:headline ?title ;
            datacite:hasIdentifier ?identifier .
  ?identifier a triple:DOI ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "10.5281/zenodo.thesaurus.ssh.v2"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "10.5281/zenodo.vocab.arthistory.v1"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "10.5281/zenodo.ontology.medieval.v09"


## CQ_12.7

Return all semantic artifacts that have URI identifiers using class-based approach.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?artifact ?title ?identifierValue WHERE {
  ?artifact a triple:SemanticArtefact ;
            schema:headline ?title ;
            datacite:hasIdentifier ?identifier .
  ?identifier a triple:URI ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "https://gotriple.eu/thesaurus/ssh#"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "https://vocab.arthistory.eu/skos#"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "https://ontology.medieval.unibo.it/owl#"


## CQ_12.8

Return all semantic artifacts with their identifier types and values.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?artifact ?title ?identifierType ?value WHERE {
  ?artifact a triple:SemanticArtefact ;
            schema:headline ?title ;
            datacite:hasIdentifier ?identifier .
  ?identifier a ?identifierType ;
              litre:hasLiteralValue ?value .
  FILTER (?identifierType IN (triple:DOI, triple:Handle, triple:URI, triple:ID, triple:PID))
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `triple:DOI` → "10.5281/zenodo.thesaurus.ssh.v2"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `triple:URI` → "https://gotriple.eu/thesaurus/ssh#"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `triple:DOI` → "10.5281/zenodo.vocab.arthistory.v1"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `triple:URI` → "https://ontology.medieval.unibo.it/owl#"

