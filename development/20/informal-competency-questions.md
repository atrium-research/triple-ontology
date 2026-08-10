## Informal Competency Questions (Iteration 20)

## Question 1

### Identifier
CQ_20.1

### Question
Return all records of the same scholarly work, given its representative record.

### Expected Outcome
The representative itself plus every record that declares it as its representative.

### Result
* `document_it20_rep`
* `document_it20_dup`

### Based on
Example 1

## Question 2

### Identifier
CQ_20.2

### Question
Given a duplicate record, return the representative whose consolidated values are surfaced.

### Expected Outcome
The target of the duplicate's `isDuplicateOf` link.

### Result
* `document_it20_rep`

### Based on
Example 1

## Question 3

### Identifier
CQ_20.3

### Question
Return the deduplicated view: every document that is not a duplicate of another record.

### Expected Outcome
Representatives and singletons; duplicates are filtered out.

### Result
* `document_it20_rep`
* `document_it20_single`

### Based on
Example 1, Example 2

## Question 4

### Identifier
CQ_20.4

### Question
How many records does each work have, counting the representative?

### Expected Outcome
One row per representative with the size of its group.

### Result
* `document_it20_rep` → 2

### Based on
Example 1

## Question 5

### Identifier
CQ_20.5

### Question
Return each duplicate with its provider and the headline of its representative.

### Expected Outcome
The duplicate's own provenance beside the consolidated title it defers to.

### Result
* `document_it20_dup` → "base" → "De l'esthétique au présent"

### Based on
Example 1
