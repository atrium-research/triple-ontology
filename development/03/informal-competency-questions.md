## Informal Competency Questions (Iteration 3)

## Question 1

### Identifier
CQ_3.1

### Question
Which agents are connected to `document_1`, and in which role?

### Expected Outcome
A list of (role, agent) pairs.

### Result
* `schema:author` → `triple:author_34`
* `schema:provider` → `triple:provider_9`
* `schema:provider` → `triple:provider_45`

### Based on
Example 1


## Question 2

### Identifier
CQ_3.2

### Question
Return all authors of `document_1` with their names.

### Expected Outcome
A list of authors with their name.

### Result
* `triple:author_34` → "name_45"

### Based on
Example 1


## Question 3

### Identifier
CQ_3.3

### Question
Return all providers of `document_1` with their names.

### Expected Outcome
A list of providers with their name.

### Result
* `triple:provider_9` → "name_3"
* `triple:provider_45` → "name_1"

### Based on
Example 1


## Question 4

### Identifier
CQ_3.4

### Question
Return all agents (persons and organizations) associated with `document_1` in any role.

### Expected Outcome
A list of agents with their name and their type.

### Result
* `triple:author_34` → "name_45" → `foaf:Person`
* `triple:provider_45` → "name_1" → `foaf:Organization`
* `triple:provider_9` → "name_3" → `foaf:Organization`

### Based on
Example 1


## Question 5

### Identifier
CQ_3.5

### Question
Return all documents authored by a specific person (`author_34`).

### Expected Outcome
A list of documents.

### Result
* `triple:document_1`

### Based on
Example 1


## Question 6

### Identifier
CQ_3.6

### Question
Who is the contact point for a specific document?

### Expected Outcome
The contact point of the document, with its e-mail address.

### Result
* `triple:contact_point_1` → "contact@example.org"

### Based on
Example 1
