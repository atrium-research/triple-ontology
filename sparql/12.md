# Formal Competency Questions - Iteration 12

## Semantic Artefact Resource Type

## CQ_12.1

Retrieve all semantic artifacts with their basic metadata (title, abstract, publisher)

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?artifact ?title ?abstract ?publisherName WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           schema:abstract ?abstract ;
           schema:publisher ?publisher .
  ?publisher foaf:name ?publisherName .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "Controlled vocabulary for Social Sciences and Humanities research classification used in the GoTriple discovery platform. Provides standardized terminology for SSH domains." → "GoTriple Consortium"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "Comprehensive vocabulary for art historical concepts and terminology. Covers periods, movements, techniques, and cultural contexts in art history research." → "Digital Humanities Institute"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "Formal ontology for medieval studies research domain. Provides semantic modeling of medieval historical periods, events, places, and scholarly concepts." → "University of Bologna"

## CQ_12.2

Find semantic artifacts with DOI or Handle persistent identifiers

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://www.essepuntato.it/2010/06/literalreification/>

SELECT ?artifact ?title ?identifierValue ?schemeLabel WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           datacite:hasIdentifier ?identifier .
  ?identifier litre:hasLiteralValue ?identifierValue ;
             datacite:usesIdentifierScheme ?scheme .
  ?scheme rdfs:label ?schemeLabel .
  FILTER(?scheme = datacite:doi || ?scheme = datacite:handle)
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "10.5281/zenodo.thesaurus.ssh.v2" → "datacite:doi"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "21.11130/00-THESAURUS-SSH-V2" → "datacite:handle"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "10.5281/zenodo.vocab.arthistory.v1" → "datacite:doi"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "21.11130/00-VOCAB-ARTHISTORY-V1" → "datacite:handle"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "10.5281/zenodo.ontology.medieval.v09" → "datacite:doi"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "21.11130/00-ONTOLOGY-MEDIEVAL-V09" → "datacite:handle"

## CQ_12.3

List all representation techniques used by semantic artifacts

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT DISTINCT ?technique WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:encodingFormat ?technique .
}
```

**Expected result:**
- "SKOS vocabulary"
- "OWL ontology"

## CQ_12.4

Find semantic artifacts and the documents that reference them

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
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
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `triple:document-dh-methodology` → "Digital Humanities Methodology Paper"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `triple:document-carolingian` → "Carolingian Renaissance Research Article"

## CQ_12.5

Retrieve semantic artifacts with their file formats and download URLs

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?artifact ?title ?fileFormat WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           schema:fileFormat ?fileFormat .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "application/rdf+xml"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "text/turtle"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "application/owl+xml"


## CQ_12.6

Return all semantic artifacts that have a DOI identifier.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://www.essepuntato.it/2010/06/literalreification/>

SELECT ?artifact ?title ?identifierValue WHERE {
  ?artifact a triple:SemanticArtefact ;
            schema:headline ?title ;
            datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme datacite:doi ;
              litre:hasLiteralValue ?identifierValue .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "10.5281/zenodo.thesaurus.ssh.v2"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "10.5281/zenodo.vocab.arthistory.v1"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "10.5281/zenodo.ontology.medieval.v09"


## CQ_12.7

Return all semantic artifacts that have a URI identifier.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://www.essepuntato.it/2010/06/literalreification/>

SELECT ?artifact ?title ?identifierValue WHERE {
  ?artifact a triple:SemanticArtefact ;
            schema:headline ?title ;
            datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme datacite:uri ;
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
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://www.essepuntato.it/2010/06/literalreification/>

SELECT ?artifact ?title ?scheme ?value WHERE {
  ?artifact a triple:SemanticArtefact ;
            schema:headline ?title ;
            datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme ?scheme ;
              litre:hasLiteralValue ?value .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `triple:full_text_url_schema` → "https://thesaurus.gotriple.eu/download/rdf"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `triple:landing_page_url_schema` → "https://thesaurus.gotriple.eu/landing"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `triple:internal_id_schema` → "gotriple:thesaurus:ssh:v2.1"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `datacite:ark` → "ark:/12345/semantic-thesaurus-ssh-v2"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `triple:original_id_schema` → "gotriple_thesaurus_ssh_v21"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `datacite:doi` → "10.5281/zenodo.thesaurus.ssh.v2"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `datacite:handle` → "21.11130/00-THESAURUS-SSH-V2"
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → `datacite:uri` → "https://gotriple.eu/thesaurus/ssh#"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `triple:full_text_url_schema` → "https://vocab.arthistory.eu/skos.ttl"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `triple:landing_page_url_schema` → "https://vocab.arthistory.eu/landing"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `triple:source_url_schema` → "https://getty.edu/research/tools/vocabularies/aat/"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `triple:internal_id_schema` → "dhi:vocab:arthistory:v1.3"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `datacite:ark` → "ark:/12345/semantic-vocab-arthistory-v1"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `triple:original_id_schema` → "dhi_vocab_arthistory_v13"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `datacite:doi` → "10.5281/zenodo.vocab.arthistory.v1"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `datacite:handle` → "21.11130/00-VOCAB-ARTHISTORY-V1"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → `datacite:uri` → "https://vocab.arthistory.eu/skos#"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `triple:full_text_url_schema` → "https://ontology.medieval.unibo.it/owl"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `triple:landing_page_url_schema` → "https://ontology.medieval.unibo.it/landing"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `triple:internal_id_schema` → "unibo:ontology:medieval:v0.9"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `datacite:ark` → "ark:/12345/semantic-ontology-medieval-studies"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `triple:original_id_schema` → "unibo_ontology_medieval_v09"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `datacite:doi` → "10.5281/zenodo.ontology.medieval.v09"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `datacite:handle` → "21.11130/00-ONTOLOGY-MEDIEVAL-V09"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → `datacite:uri` → "https://ontology.medieval.unibo.it/owl#"


## CQ_12.9

Return all semantic artifacts with their license.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?artifact ?title ?license WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           triple:hasLicense ?lic .
  ?lic rdfs:label ?license .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "CC BY 4.0"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "CC0 1.0"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "CC BY-NC 4.0"


## CQ_12.10

Return all semantic artifacts with their access conditions.

```sparql
PREFIX schema: <https://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?artifact ?title ?access WHERE {
  ?artifact a triple:SemanticArtefact ;
           schema:headline ?title ;
           triple:hasConditionOfAccess ?acc .
  ?acc rdfs:label ?access .
}
```

**Expected result:**
- `triple:thesaurus-ssh` → "TRIPLE SSH Thesaurus" → "Open Access"
- `triple:vocab-arthistory` → "SKOS Art History Vocabulary" → "Open Access"
- `triple:ontology-medieval` → "Medieval Studies Ontology" → "Restricted Access"
