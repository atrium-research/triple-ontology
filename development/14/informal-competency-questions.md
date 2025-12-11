# Informal Competency Questions - Iteration 14

## Question 1

### Identifier
CQ_14.1

### Question
Which research projects produced a specific document, dataset, semantic artefact, or media object as an output?

### Expected Outcome
List of research projects that generated the specified research artifact

### Result
* `triple:project-digital-humanities` → produced `triple:document-dh-methods`
* `triple:project-cultural-heritage` → produced `triple:ontology-cultural-heritage`
* `triple:project-migration-studies` → produced `triple:dataset-migration-interviews`, `triple:audio-interview-001`

### Based on
Examples 1, 2, and 3

## Question 2

### Identifier
CQ_14.2

### Question
What research outputs (documents, datasets, semantic artefacts, media objects) were produced by a specific research project?

### Expected Outcome
List of research artifacts that were generated as outputs of the specified project

### Result
* `triple:project-digital-humanities` → `triple:document-dh-methods`
* `triple:project-cultural-heritage` → `triple:ontology-cultural-heritage`
* `triple:project-migration-studies` → `triple:dataset-migration-interviews`, `triple:audio-interview-001`

### Based on
Examples 1, 2, and 3

## Question 3

### Identifier
CQ_14.3

### Question
Which documents, papers, or other creative works reference or cite a specific semantic artefact, dataset, or media object?

### Expected Outcome
List of citing resources that reference the specified research artifact

### Result
* `triple:ontology-cultural-heritage` → referenced by `triple:paper-heritage-analysis`
* `triple:dataset-migration-interviews` → referenced by `triple:analysis-urban-migration`
* `triple:audio-interview-001` → referenced by `triple:analysis-urban-migration`

### Based on
Examples 2 and 3

## Question 4

### Identifier
CQ_14.4

### Question
For a given semantic artefact, dataset, or media object, what are both its originating project and its citing documents?

### Expected Outcome
Combined information showing the production context (project) and usage context (citations) of a research artifact

### Result
* `triple:ontology-cultural-heritage` → produced by `triple:project-cultural-heritage`, referenced by `triple:paper-heritage-analysis`
* `triple:dataset-migration-interviews` → produced by `triple:project-migration-studies`, referenced by `triple:analysis-urban-migration`
* `triple:audio-interview-001` → produced by `triple:project-migration-studies`, referenced by `triple:analysis-urban-migration`

### Based on
Examples 2 and 3

## Question 5

### Identifier
CQ_14.5

### Question
Which research artifacts use the FRAPO property (frapo:isOutputOf) for linking to their originating projects?

### Expected Outcome
List of research artifacts that use the standard FRAPO vocabulary for project relationships

### Result
* `triple:document-dh-methods` → frapo:isOutputOf `triple:project-digital-humanities`
* `triple:ontology-cultural-heritage` → frapo:isOutputOf `triple:project-cultural-heritage`
* `triple:dataset-migration-interviews` → frapo:isOutputOf `triple:project-migration-studies`
* `triple:audio-interview-001` → frapo:isOutputOf `triple:project-migration-studies`

### Based on
Examples 1, 2, and 3