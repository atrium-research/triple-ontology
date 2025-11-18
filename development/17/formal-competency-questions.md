# Formal Competency Questions - Iteration 17

## CQ_17.1

Find the research projects that produced a specific document as an output.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX frapo: <http://purl.org/cerif/frapo/>

SELECT ?project ?projectName WHERE {
  triple:document-dh-methods frapo:isOutputOf ?project .
  ?project schema:name ?projectName .
}
```

**Expected result:**
- `triple:project-digital-humanities` → "Digital Humanities Research Initiative"

## CQ_17.2

Find all research outputs produced by a specific research project.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX frapo: <http://purl.org/cerif/frapo/>

SELECT ?output ?outputName ?outputType WHERE {
  ?output frapo:isOutputOf triple:project-migration-studies ;
          schema:name ?outputName ;
          rdf:type ?outputType .
  FILTER(?outputType != owl:NamedIndividual)
}
```

**Expected result:**
- `triple:dataset-migration-interviews` → "Migration Interview Dataset" → `triple:Dataset`
- `triple:audio-interview-001` → "Interview with Migrant Family - Naples" → `triple:MediaObject`

## CQ_17.3

Find all documents that reference or cite a specific semantic artefact.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?citingDocument ?documentName WHERE {
  triple:ontology-cultural-heritage dcterms:isReferencedBy ?citingDocument .
  ?citingDocument schema:name ?documentName .
}
```

**Expected result:**
- `triple:paper-heritage-analysis` → "Analysis of Digital Heritage Frameworks"

## CQ_17.4

For a given dataset, find both its originating project and any documents that reference it.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX frapo: <http://purl.org/cerif/frapo/>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?project ?projectName ?citingDocument ?documentName WHERE {
  triple:dataset-migration-interviews frapo:isOutputOf ?project ;
                                      dcterms:isReferencedBy ?citingDocument .
  ?project schema:name ?projectName .
  ?citingDocument schema:name ?documentName .
}
```

**Expected result:**
- `triple:project-migration-studies` → "Migration Patterns in Southern Europe" → `triple:analysis-urban-migration` → "Urban Migration Patterns: A Mediterranean Perspective"

## CQ_17.5

Find all research artifacts that use FRAPO properties to link to their originating projects.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX frapo: <http://purl.org/cerif/frapo/>

SELECT ?artifact ?artifactName ?project ?projectName WHERE {
  ?artifact frapo:isOutputOf ?project ;
            schema:name ?artifactName .
  ?project schema:name ?projectName .
}
```

**Expected result:**
- `triple:document-dh-methods` → "Digital Methods in Historical Research" → `triple:project-digital-humanities` → "Digital Humanities Research Initiative"
- `triple:ontology-cultural-heritage` → "Cultural Heritage Preservation Ontology" → `triple:project-cultural-heritage` → "European Cultural Heritage Ontology Project"
- `triple:dataset-migration-interviews` → "Migration Interview Dataset" → `triple:project-migration-studies` → "Migration Patterns in Southern Europe"
- `triple:audio-interview-001` → "Interview with Migrant Family - Naples" → `triple:project-migration-studies` → "Migration Patterns in Southern Europe"

## CQ_17.6

Find all research artifacts (of any type) that were both produced by projects and are referenced by other works.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX frapo: <http://purl.org/cerif/frapo/>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?artifact ?artifactName ?project ?projectName ?citingWork ?citingWorkName WHERE {
  ?artifact frapo:isOutputOf ?project ;
            dcterms:isReferencedBy ?citingWork ;
            schema:name ?artifactName .
  ?project schema:name ?projectName .
  ?citingWork schema:name ?citingWorkName .
}
```

**Expected result:**
- `triple:ontology-cultural-heritage` → "Cultural Heritage Preservation Ontology" → `triple:project-cultural-heritage` → "European Cultural Heritage Ontology Project" → `triple:paper-heritage-analysis` → "Analysis of Digital Heritage Frameworks"
- `triple:dataset-migration-interviews` → "Migration Interview Dataset" → `triple:project-migration-studies` → "Migration Patterns in Southern Europe" → `triple:analysis-urban-migration` → "Urban Migration Patterns: A Mediterranean Perspective"
- `triple:audio-interview-001` → "Interview with Migrant Family - Naples" → `triple:project-migration-studies` → "Migration Patterns in Southern Europe" → `triple:analysis-urban-migration` → "Urban Migration Patterns: A Mediterranean Perspective"