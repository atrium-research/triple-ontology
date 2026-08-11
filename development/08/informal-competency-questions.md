## Informal Competency Questions (Iteration 8)

## Question 1

### Identifier
CQ_8.1

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
CQ_8.2

### Question
Return the identifier scheme used by `identifier_23`.

### Expected Outcome
An identifier scheme.

### Result
* `datacite:issn`

### Based on
Example 2


## Question 3

### Identifier
CQ_8.3

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
CQ_8.4

### Question
Return all identifier schemes defined in the ontology.

### Expected Outcome
A list of identifier schemes.

### Result
* `datacite:doi`
* `datacite:issn`
* `datacite:isbn`
* `datacite:handle`
* `datacite:ark`
* `triple:original_id_schema`
* `triple:internal_id_schema`

### Based on
Example 1
Example 2
Example 3
Example 4


## Question 5

### Identifier
CQ_8.5

### Question
Return all identifiers of `document_45` along with their schemes.

### Expected Outcome
A list of identifiers with their respective schemes.

### Result
* `triple:identifier_internal_45` → `triple:internal_id_schema`
* `triple:identifier_pid_45` → `datacite:ark`
* `triple:identifier_original_45` → `triple:original_id_schema`
* `triple:identifier_23` → `datacite:issn`
* `triple:identifier_24` → `datacite:doi`

### Based on
Example 2


## Question 6

### Identifier
CQ_8.6

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
CQ_8.7

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
CQ_8.8

### Question
Return all identifiers and their schemes for `document_78`.

### Expected Outcome
An identifier with its scheme.

### Result
* `triple:identifier_internal_78` → `triple:internal_id_schema`
* `triple:identifier_pid_78` → `datacite:ark`
* `triple:identifier_original_78` → `triple:original_id_schema`
* `triple:identifier_90` → `datacite:handle`

### Based on
Example 3


## Question 9

### Identifier
CQ_8.9

### Question
Return all identifiers with their schemes and literal values.

### Expected Outcome
Every identifier node of the exemplars, with its scheme and its literal value.

### Result
* 17 identifier nodes in total, e.g.:
* `identifier_1` → `datacite:doi` → "10.1234/example.2024.001"
* `identifier_90` → `datacite:handle` → "11234/5678-abcd-efgh"
* `identifier_internal_1` → `triple:internal_id_schema` → "TRIPLE_DOC_001"

### Based on
Examples 1, 2, 3, 4


## Question 10

### Identifier
CQ_8.10

### Question
Return all documents that have a DOI identifier.

### Expected Outcome
Every document carrying an identifier whose scheme is `datacite:doi`.

### Result
* `triple:document_1`
* `triple:document_45`

### Based on
Examples 1, 2, 3, 4


## Question 11

### Identifier
CQ_8.11

### Question
Return all documents that have an ISSN identifier.

### Expected Outcome
Every document carrying an identifier whose scheme is `datacite:issn`.

### Result
* `triple:document_45`

### Based on
Examples 1, 2, 3, 4


## Question 12

### Identifier
CQ_8.12

### Question
Return all identifier values by type.

### Expected Outcome
The scheme/value pairs of the standard bibliographic identifiers (DOI, Handle, ISSN, ISBN).

### Result
* `datacite:doi` → "10.1234/example.2024.001"
* `datacite:doi` → "10.5678/journal.2024.045"
* `datacite:issn` → "1234-5678"
* `datacite:handle` → "11234/5678-abcd-efgh"
* `datacite:isbn` → "978-3-16-148410-0"

### Based on
Examples 1, 2, 3, 4

