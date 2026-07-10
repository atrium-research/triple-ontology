# Informal Competency Questions (Iteration 17)

## Question 1

### Identifier
CQ_17.1

### Question
What are all the original (as-received) metadata values of a given document?

### Expected Outcome
The list of raw provider values (type, language, publication date, license, conditions of access) preserved for the document.

### Result
* `originalType` → "journalArticle"
* `originalLanguage` → "eng"
* `originalDatePublished` → "03/05/2021"
* `originalLicense` → "CC BY 4.0"
* `originalConditionsOfAccess` → "info:eu-repo/semantics/openAccess"

### Based on
Example 1

## Question 2

### Identifier
CQ_17.2

### Question
For each document, what is the original type received from the provider and which Content Type was it normalized to?

### Expected Outcome
Pairs of raw type string and normalized Content Type concept, allowing the normalization to be audited.

### Result
* `document_it17_1` → "journalArticle" / `ContentType/article`
* `document_it17_2` → "COAR text" / `ContentType/text`

### Based on
Example 1 and Example 2

## Question 3

### Identifier
CQ_17.3

### Question
Which documents were received with a specific raw access rights statement (e.g. `info:eu-repo/semantics/openAccess`)?

### Expected Outcome
The list of documents whose original conditions of access match the given raw string.

### Result
* `document_it17_1`

### Based on
Example 1

## Question 4

### Identifier
CQ_17.4

### Question
Which rights-related information (in the Dublin Core sense) was received from the provider for a given document, regardless of whether it is a license or an access condition?

### Expected Outcome
All values of properties that refine `dc:rights` (i.e. both `originalLicense` and `originalConditionsOfAccess`), demonstrating the Dublin Core interoperability of the sub-property pattern.

### Result
* `document_it17_1` → "CC BY 4.0"
* `document_it17_1` → "info:eu-repo/semantics/openAccess"

### Based on
Example 1

## Question 5

### Identifier
CQ_17.5

### Question
What is the raw source statement received from the provider for a given document, and which original provider values were received for a dataset?

### Expected Outcome
The verbatim source string of the document and the raw type/language/license strings preserved on the dataset.

### Result
* `document_it17_1` → "Journal of Digital Humanities, 12(3), 2021"
* `dataset_it17_1` → "Dataset/csv", "French", "https://spdx.org/licenses/CC-BY-4.0.html"

### Based on
Example 1 and Example 3
