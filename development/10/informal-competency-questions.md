## Informal Competency Questions (Iteration 10)

## Question 1

### Identifier
CQ_10.1

### Question
Return all identifiers that use the DOI scheme.

### Expected Outcome
A list of identifiers.

### Result
* `identifier_1`
* `identifier_24`

### Based on
Example 1
Example 2


## Question 2

### Identifier
CQ_10.2

### Question
Return the identifier scheme used by `identifier_23`.

### Expected Outcome
An identifier scheme.

### Result
* `triple:issn`

### Based on
Example 2


## Question 3

### Identifier
CQ_10.3

### Question
Return all documents that have a DOI identifier.

### Expected Outcome
A list of documents.

### Result
* `document_1`
* `document_45`

### Based on
Example 1
Example 2


## Question 4

### Identifier
CQ_10.4

### Question
Return all identifier schemes defined in the ontology.

### Expected Outcome
A list of identifier schemes.

### Result
* `triple:doi`
* `triple:issn`
* `triple:isbn`
* `triple:handle`

### Based on
Example 1
Example 2
Example 3
Example 4


## Question 5

### Identifier
CQ_10.5

### Question
Return all identifiers of `document_45` along with their schemes.

### Expected Outcome
A list of identifiers with their respective schemes.

### Result
* `identifier_23` uses `triple:issn`
* `identifier_24` uses `triple:doi`

### Based on
Example 2


## Question 6

### Identifier
CQ_10.6

### Question
Return the literal value of the DOI identifier for `document_1`.

### Expected Outcome
A string literal.

### Result
* "10.1234/example.2024.001"

### Based on
Example 1


## Question 7

### Identifier
CQ_10.7

### Question
Return all documents that have an ISBN identifier.

### Expected Outcome
A list of documents.

### Result
* `document_99`

### Based on
Example 4


## Question 8

### Identifier
CQ_10.8

### Question
Return all identifiers and their schemes for `document_78`.

### Expected Outcome
An identifier with its scheme.

### Result
* `identifier_90` uses `triple:handle`

### Based on
Example 3
