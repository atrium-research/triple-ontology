## Informal Competency Questions (Iteration 9)

## Question 1

### Identifier
CQ_9.1

### Question
Return all documents with "Open access" conditions.

### Expected Outcome
A list of documents.

### Result
* `document_1`

### Based on
Example 1


## Question 2

### Identifier
CQ_9.2

### Question
Return the vocabulary scheme to which `acc_embargoed-access` belongs.

### Expected Outcome
A vocabulary scheme.

### Result
* `conditions_of_access` vocabulary

### Based on
Example 2


## Question 3

### Identifier
CQ_9.3

### Question
Return all external COAR terms that exactly match the access conditions in the GoTriple vocabulary.

### Expected Outcome
A list of external URIs.

### Result
* `https://vocabularies.coar-repositories.org/access_rights/c_f1cf/` (Embargoed Access)
* `https://vocabularies.coar-repositories.org/access_rights/c_14cb/` (Metadata Only Access)
* `https://vocabularies.coar-repositories.org/access_rights/c_abf2/` (Open Access)
* `https://vocabularies.coar-repositories.org/access_rights/c_16ec/` (Restricted Access)

### Based on
Example 1
Example 2
Example 3
Example 4


## Question 4

### Identifier
CQ_9.4

### Question
Return the access condition of `document_23`.

### Expected Outcome
An access condition term.

### Result
* `acc_embargoed-access`

### Based on
Example 2


## Question 5

### Identifier
CQ_9.5

### Question
Return all access condition terms in the controlled vocabulary.

### Expected Outcome
A list of terms including the newly added COAR-aligned terms.

### Result
* `acc_embargoed-access`
* `acc_metadata-only-access`
* `acc_open-access`
* `acc_restricted-access`
* (... other access condition terms)

### Based on
Example 1
Example 2
Example 3
Example 4


## Question 6

### Identifier
CQ_9.6

### Question
Return all documents that have metadata-only access.

### Expected Outcome
A list of documents.

### Result
* `document_56`

### Based on
Example 3


## Question 7

### Identifier
CQ_9.7

### Question
Return the COAR external term that exactly matches `acc_open-access`.

### Expected Outcome
An external URI.

### Result
* `https://vocabularies.coar-repositories.org/access_rights/c_abf2/`

### Based on
Example 1
