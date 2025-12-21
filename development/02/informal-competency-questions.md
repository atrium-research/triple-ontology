# Informal Competency Questions (Iteration 2)

## Question 1

### Identifier
CQ_2.1

### Question
What license is associated with `document_1`?

### Expected Outcome
The license term from the License Vocabulary.

### Result
* `cc_by_4_0` (Creative Commons Attribution 4.0)

### Based on
Example 1


## Question 2

### Identifier
CQ_2.2

### Question
What are the access conditions for `document_2`?

### Expected Outcome
The access conditions term from the Access Conditions Vocabulary.

### Result
* `open_access`

### Based on
Example 2


## Question 3

### Identifier
CQ_2.3

### Question
What type of document is `document_3`?

### Expected Outcome
The content type term from the Content Type Vocabulary.

### Result
* `article`

### Based on
Example 3


## Question 4

### Identifier
CQ_2.4

### Question
What disciplines is `document_4` associated with?

### Expected Outcome
A list of discipline terms from the Discipline Vocabulary.

### Result
* `digital_humanities`
* `linguistics`

### Based on
Example 4


## Question 5

### Identifier
CQ_2.5

### Question
What external entity does the license term `cc_by_4_0` match exactly?

### Expected Outcome
The external URI that is an exact match.

### Result
* `https://creativecommons.org/licenses/by/4.0/`

### Based on
Example 1


## Question 6

### Identifier
CQ_2.6

### Question
What external entities does the access term `open_access` closely match?

### Expected Outcome
External URIs that are close matches.

### Result
* `http://purl.org/coar/access_right/c_abf2` (COAR Open Access)

### Based on
Example 2


## Question 7

### Identifier
CQ_2.7

### Question
Return all documents that are licensed under Creative Commons licenses (any CC license).

### Expected Outcome
A list of documents with CC licenses.

### Result
* `document_1` (has `cc_by_4_0`)

### Based on
Example 1


## Question 8

### Identifier
CQ_2.8

### Question
Return all documents that are of type "Article" and are Open Access.

### Expected Outcome
Documents that match both criteria.

### Result
* (Would return documents matching both criteria)

### Based on
Examples 2 and 3


## Question 9

### Identifier
CQ_2.9

### Question
For a given document, return all its classification metadata (license, access conditions, type, and disciplines).

### Expected Outcome
A consolidated view of all vocabulary terms linked to the document.

### Result
* License, Access Condition, Content Type, and Disciplines for the document.

### Based on
All Examples


## Question 10

### Identifier
CQ_2.10

### Question
List all imported vocabulary modules in the ontology.

### Expected Outcome
The URIs of the imported ontology modules.

### Result
* `content_types`, `conditions_of_access`, `licenses`, `disciplines` modules.

### Based on
Ontology imports
