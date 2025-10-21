## Informal Competency Questions (Iteration 8)

## Question 1

### Identifier
CQ_8.1

### Question
Return all documents with type "Book part".

### Expected Outcome
A list of documents.

### Result
* `document_1`
* `document_45`

### Based on
Example 1
Example 2


## Question 2

### Identifier
CQ_8.2

### Question
Return the vocabulary scheme to which `typ_book-part` belongs.

### Expected Outcome
A vocabulary scheme.

### Result
* Document Types vocabulary

### Based on
Example 3


## Question 3

### Identifier
CQ_8.3

### Question
Return all external terms that exactly match `typ_book-part`.

### Expected Outcome
A list of external URIs.

### Result
* `https://vocabularies.coar-repositories.org/resource_types/c_3248/`

### Based on
Example 1
Example 3


## Question 4

### Identifier
CQ_8.4

### Question
Return the type of `document_1`.

### Expected Outcome
A document type term.

### Result
* `typ_book-part`

### Based on
Example 1


## Question 5

### Identifier
CQ_8.5

### Question
Return all document types in the controlled vocabulary.

### Expected Outcome
A list of terms including the newly added book part type.

### Result
* `typ_article`
* `typ_book`
* `typ_book-part`
* (... other document types)

### Based on
Example 3
