# Informal Competency Questions (Iteration 18)

## Question 1

### Identifier
CQ_18.1

### Question
Which disciplines were assigned to a given document, and with what confidence?

### Expected Outcome
Pairs of Discipline concept and trust score, read from the classification annotations targeting the document.

### Result
* `document_it18_1` → `Discipline/methods_and_statistics` → 0.87
* `document_it18_2` → `Discipline/political_science` → 0.55

### Based on
Example 1 and Example 2

## Question 2

### Identifier
CQ_18.2

### Question
Which documents were classified under a discipline with confidence of at least 0.8?

### Expected Outcome
Only documents whose classification annotations carry a trust score greater than or equal to the threshold.

### Result
* `document_it18_1`

### Based on
Example 1 and Example 2

## Question 3

### Identifier
CQ_18.3

### Question
What are the keywords (knows_about) of a given document, with their labels and, when available, their external URI?

### Expected Outcome
The DefinedTerm entities linked to the document, with multilingual names and optional sameAs link.

### Result
* `document_it18_1` → "Text mining"@en / "Fouille de textes"@fr → `wikidata:Q676880`
* `document_it18_2` → "Public opinion"@en → (no external URI)

### Based on
Example 1 and Example 2

## Question 4

### Identifier
CQ_18.4

### Question
Which language versions of a document's title are machine translations?

### Expected Outcome
The headline literals whose language tag appears among the document's machine-translated languages.

### Result
* `document_it18_1` → "Digital methods and SSH research"@en
* `document_it18_1` → "Métodos digitais e a pesquisa em CSH"@pt

### Based on
Example 1

## Question 5

### Identifier
CQ_18.5

### Question
For which documents does the detected language differ from the language originally declared by the provider?

### Expected Outcome
Documents where the pipeline's language detection disagrees with the provider's raw language value (iteration 17), useful for auditing the ingestion.

### Result
* `document_it18_2` → detected "en", provider said "und"

### Based on
Example 2
