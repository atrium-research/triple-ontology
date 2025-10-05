## Informal Competency Questions (Iteration 11)

## Question 1

### Identifier
CQ_11.1

### Question
Return all entities mentioned by `document_1`.

### Expected Outcome
A list of entities (documents, persons, projects, organizations).

### Result
* `document_45`
* `person_23`

### Based on
Example 1


## Question 2

### Identifier
CQ_11.2

### Question
Return all documents mentioned by `document_89`.

### Expected Outcome
A list of documents.

### Result
* `document_100`
* `document_101`
* `document_102`

### Based on
Example 3


## Question 3

### Identifier
CQ_11.3

### Question
Return all documents that mention `person_78`.

### Expected Outcome
A list of documents.

### Result
* `document_34`

### Based on
Example 4


## Question 4

### Identifier
CQ_11.4

### Question
Return all projects mentioned in any document.

### Expected Outcome
A list of projects.

### Result
* `project_12`

### Based on
Example 2


## Question 5

### Identifier
CQ_11.5

### Question
Return all organizations mentioned by `document_67`.

### Expected Outcome
A list of organizations.

### Result
* `organization_5`

### Based on
Example 2


## Question 6

### Identifier
CQ_11.6

### Question
Return all people mentioned by `document_34`.

### Expected Outcome
A list of persons.

### Result
* `person_78`

### Based on
Example 4


## Question 7

### Identifier
CQ_11.7

### Question
Return all documents that mention at least one other document.

### Expected Outcome
A list of documents that have citations/references.

### Result
* `document_1`
* `document_89`

### Based on
Example 1
Example 3


## Question 8

### Identifier
CQ_11.8

### Question
Return all entities mentioned by `document_67` with their types.

### Expected Outcome
A list of entities with their respective types.

### Result
* `project_12` (type: Project)
* `organization_5` (type: Organization)

### Based on
Example 2
