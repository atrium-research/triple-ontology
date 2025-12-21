## Informal Competency Questions (Iteration 1)

## Question 1

### Identifier
CQ_1.1

### Question
Return the language associated with `document_1`.

### Expected Outcome
A language.

### Result
`language_10`

### Based on
Example 1
Example 2
Example 3

## Question 2

### Identifier
CQ_1.2

### Question
Return the identifiers associated with `document_1`.

### Expected Outcome
A list of identifiers.

### Result
* `identifier_2`
* `identifier_4`

### Based on
Example 1
Example 2
Example 3

## Question 4

### Identifier
CQ_1.4

### Question
Return all documents.

### Expected Outcome
A list of documents.

### Result
* `document_1`
* `document_45`
* `document_31`

### Based on
Example 1
Example 2
Example 3

## Question 5

### Identifier
CQ_1.5

### Question
Return all languages.

### Expected Outcome
A list of languages.

### Result
* `language_10`
* `language_2`

### Based on
Example 1
Example 2
Example 3

## Question 8

### Identifier
CQ_1.8

### Question
Return the title (headline) of `document_1` in English.

### Expected Outcome
The English title of the document.

### Result
"The Impact of Digital Humanities on SSH Research"@en

### Based on
Example 1

## Question 9

### Identifier
CQ_1.9

### Question
Return all titles (headlines) associated with `document_1`.

### Expected Outcome
A list of titles in all available languages.

### Result
* "The Impact of Digital Humanities on SSH Research"@en
* "L'impact des humanités numériques sur la recherche SHS"@fr

### Based on
Example 1

## Question 10

### Identifier
CQ_1.10

### Question
Return the abstract of `document_31`.

### Expected Outcome
The abstract of the document.

### Result
"An analysis of migration flows across European countries during the twentieth century."@en

### Based on
Example 3

## Question 11

### Identifier
CQ_1.11

### Question
Return the encoding format of all documents.

### Expected Outcome
A list of MIME types associated with documents.

### Result
* "application/pdf" (for `document_1`)
* "text/html" (for `document_31`)

### Based on
Example 1
Example 3

## Question 12

### Identifier
CQ_1.12

### Question
Return all documents in PDF format.

### Expected Outcome
A list of documents with encoding format "application/pdf".

### Result
* `document_1`

### Based on
Example 1

## Question 13

### Identifier
CQ_1.13

### Question
Return the landing page URL of `document_1`.

### Expected Outcome
The landing page URL.

### Result
"https://hal.archives-ouvertes.fr/hal-12345"

### Based on
Example 1

## Question 14

### Identifier
CQ_1.14

### Question
Return all URL-based identifiers (landing page, full text, source) for `document_1`.

### Expected Outcome
A list of URL identifiers.

### Result
* `identifier_landing_1` (https://hal.archives-ouvertes.fr/hal-12345)
* `identifier_fulltext_1` (https://hal.archives-ouvertes.fr/hal-12345/document)
* `identifier_source_1` (https://journals.openedition.org/dh/12345)

### Based on
Example 1

## Question 15

### Identifier
CQ_1.19

### Question
Return the source of `document_1`.

### Expected Outcome
The source entity (or string).

### Result
`document_journal`

### Based on
Example 1
