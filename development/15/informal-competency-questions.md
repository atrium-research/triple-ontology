# Informal Competency Questions (Iteration 15)

## Question 1
### Identifier
CQ_15.1

### Question
Which entities are mentioned in "Document 1"?

### Expected Outcome
A list of names/URIs: Ada Lovelace, Jane Doe, John Smith.

### Result
*   <http://www.wikidata.org/entity/Q7259> (Ada Lovelace)
*   `triple:JaneDoe` (Jane Doe)
*   `triple:person_1` (John Smith)
*   `triple:place_rome` (Rome)
*   `triple:concept_democracy` (Democracy)

### Based on
Motive Scenario

## Question 2
### Identifier
CQ_15.2

### Question
Which external entities (e.g., from Wikidata) are mentioned in "Document 1"?

### Expected Outcome
Ada Lovelace URI.

### Result
*   <http://www.wikidata.org/entity/Q7259>

## Question 3
### Identifier
CQ_15.3

### Question
Which newly discovered local entities are mentioned in "Document 1"?

### Expected Outcome
John Smith URI.

### Result
*   `triple:person_1`


## Question 4

### Identifier
CQ_15.4

### Question
Retrieve all annotations connected to the document via `schema:mentions`.

### Expected Outcome
Every annotation node attached to the document, with the entity it points at.

### Result
* `ann_101` → `wd:Q7259` (Ada Lovelace)
* `ann_102` → `triple:JaneDoe`
* `ann_103` → `triple:person_1`
* `ann_104` → `triple:place_rome`
* `ann_105` → `triple:concept_democracy`

### Based on
Motive Scenario



## Question 5

### Identifier
CQ_15.5

### Question
Return only Places mentioned.

### Expected Outcome
The mentioned entities that are typed as places.

### Result
* `triple:place_rome`

### Based on
Motive Scenario

