# Informal Competency Questions - Iteration 12

## Semantic Artefact Resource Type

## Question 1

### Identifier
CQ_12.1

### Question
What are all the semantic artifacts available in the GoTriple platform with their basic metadata (title, abstract, publisher)?

### Expected Outcome
List of semantic artifacts with their titles, abstracts, and publisher information

### Result
* `TRIPLE SSH Thesaurus` → "Controlled vocabulary for Social Sciences and Humanities research classification", "GoTriple Consortium"
* `SKOS Art History Vocabulary` → "Comprehensive vocabulary for art historical concepts and terminology", "Digital Humanities Institute"
* `Medieval Studies Ontology` → "Formal ontology for medieval studies research domain", "University of Bologna"

### Based on
Example 1, Example 2, and Example 3

## Question 2

### Identifier
CQ_12.2

### Question
Which semantic artifacts have DOI or Handle identifiers and what are their persistent identifiers?

### Expected Outcome
List of semantic artifacts with their DOI or Handle persistent identifiers

### Result
* `TRIPLE SSH Thesaurus` → "DOI: 10.5281/zenodo.1234567"
* `Medieval Studies Ontology` → "Handle: hdl:1234.5/medieval-ontology"

### Based on
Example 1 and Example 3

## Question 3

### Identifier
CQ_12.3

### Question
What are the different representation techniques used by semantic artifacts in the platform?

### Expected Outcome
List of representation techniques/methodologies used to structure semantic content

### Result
* `SKOS vocabulary`
* `OWL ontology`
* `XML schema`
* `RDF Schema`

### Based on
Example 1, Example 2, and Example 3

## Question 4

### Identifier
CQ_12.4

### Question
Which semantic artifacts are referenced by documents in the platform and what documents reference them?

### Expected Outcome
List of semantic artifacts and the documents that cite or reference them

### Result
* `TRIPLE SSH Thesaurus` → "Digital Humanities Methodology Paper"
* `Medieval Studies Ontology` → "Carolingian Renaissance Research Article"

### Based on
Example 1 and Example 3

## Question 5

### Identifier
CQ_12.5

### Question
What are the different file formats available for semantic artifacts and their download URLs?

### Expected Outcome
List of semantic artifacts with their file formats and access URLs

### Result
* `TRIPLE SSH Thesaurus` → "application/rdf+xml", "https://thesaurus.gotriple.eu/download/rdf"
* `SKOS Art History Vocabulary` → "text/turtle", "https://vocab.arthistory.eu/skos.ttl"
* `Medieval Studies Ontology` → "application/owl+xml", "https://ontology.medieval.unibo.it/owl"

### Based on
Example 1, Example 2, and Example 3


## Question 6

### Identifier
CQ_12.6

### Question
Return all semantic artifacts that have DOI identifiers using class-based approach.

### Expected Outcome
A list of semantic artifacts with valid DOI identifiers.

### Result
* `thesaurus-ssh` → 10.5281/zenodo.thesaurus.ssh.v2
* `vocab-arthistory` → 10.5281/zenodo.vocab.arthistory.v1  
* `ontology-medieval` → 10.5281/zenodo.ontology.medieval.v09

### Based on
Example 1, Example 2, and Example 3


## Question 7

### Identifier
CQ_12.7

### Question
Return all semantic artifacts that have URI identifiers using class-based approach.

### Expected Outcome
A list of semantic artifacts with their namespace URI identifiers.

### Result
* `thesaurus-ssh` → https://gotriple.eu/thesaurus/ssh#
* `vocab-arthistory` → https://vocab.arthistory.eu/skos#
* `ontology-medieval` → https://ontology.medieval.unibo.it/owl#

### Based on
Example 1, Example 2, and Example 3


## Question 8

### Identifier
CQ_12.8

### Question
Return all semantic artifacts with their identifier types and values.

### Expected Outcome
A comprehensive list of semantic artifacts with all their identifier types (DOI, Handle, URI, platform identifiers).

### Result
* `thesaurus-ssh` → DOI: 10.5281/zenodo.thesaurus.ssh.v2, URI: https://gotriple.eu/thesaurus/ssh#
* `vocab-arthistory` → DOI: 10.5281/zenodo.vocab.arthistory.v1, URI: https://vocab.arthistory.eu/skos#
* `ontology-medieval` → URI: https://ontology.medieval.unibo.it/owl#

### Based on
Example 1, Example 2, and Example 3

### Based on
Example 1, Example 2, and Example 3


## Question 9

### Identifier
CQ_12.9

### Question
What are the licenses associated with the semantic artifacts?

### Expected Outcome
List of semantic artifacts and their licenses.

### Result
* `TRIPLE SSH Thesaurus` → CC BY 4.0
* `SKOS Art History Vocabulary` → CC0 1.0
* `Medieval Studies Ontology` → CC BY-NC 4.0

### Based on
Example 1, Example 2, and Example 3


## Question 10

### Identifier
CQ_12.10

### Question
What are the access conditions for the semantic artifacts?

### Expected Outcome
List of semantic artifacts and their access conditions.

### Result
* `TRIPLE SSH Thesaurus` → Open Access
* `SKOS Art History Vocabulary` → Open Access
* `Medieval Studies Ontology` → Restricted Access

### Based on
Example 1, Example 2, and Example 3
