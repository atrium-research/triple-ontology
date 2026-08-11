## Informal Competency Questions (Iteration 6)

## Question 1

### Identifier
CQ_6.1

### Question
Return all information about `profile_1`.

### Expected Outcome
A profile with all associated properties and values.

### Result
* <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> → <http://www.w3.org/2002/07/owl#NamedIndividual>
* <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> → `triple:Profile`
* `datacite:hasIdentifier` → `triple:identifier_pid_profile_1`
* `datacite:hasIdentifier` → `triple:agent_identifier_2345678998765`
* `foaf:account` → `triple:account_1`
* `foaf:name` → "John Smith"
* <http://www.w3.org/2000/01/rdf-schema#comment> → "Profile associated with account_1"

### Based on
Example 1


## Question 2

### Identifier
CQ_6.2

### Question
Return all authors of `document_56` that are associated with a user account.

### Expected Outcome
A list of author profiles that are associated with a user account.

### Result
* `profile_56` (associated with account_109)
* `profile_09` (associated with account_109)
* `profile_123` (associated with account_109)

### Based on
Example 2


## Question 3

### Identifier
CQ_6.3

### Question
Return all profiles associated with `account_109`.

### Expected Outcome
A list of profiles associated with the user account.

### Result
* `profile_56`
* `profile_09`
* `profile_123`

### Based on
Example 3


## Question 4

### Identifier
CQ_6.4

### Question
Return all names (fullnames) of profiles associated with `account_109`.

### Expected Outcome
A list of names from all profiles associated with the account.

### Result
* "Maria Rossi"
* "M. Rossi"
* "Maria R. Rossi"

### Based on
Example 3


## Question 5

### Identifier
CQ_6.5

### Question
Return all unassociated profiles (profiles without an account).

### Expected Outcome
A list of profiles that are not associated with any user account.

### Result
* `profile_23` - name: "Pierre Dupont"

### Based on
Example 2

## Question 6

### Identifier
CQ_6.6

### Question
Return all documents authored by profiles associated with `account_109`.

### Expected Outcome
A list of documents with the profile that authored each of them.

### Result
* `document_56` - `profile_56`
* `document_67` - `profile_56`
* `document_56` - `profile_09`
* `document_98` - `profile_09`
* `document_56` - `profile_123`
* `document_42` - `profile_123`

### Based on
Example 3
