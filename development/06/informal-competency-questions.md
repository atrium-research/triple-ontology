## Informal Competency Questions (Iteration 6)

## Question 1

### Identifier
CQ_6.1

### Question
Return all information about `profile_1`.

### Expected Outcome
A profile with all associated properties and values.

### Result
* type: `triple:Profile`
* identifier: `agent_identifier_2345678998765`
* account: `account_1`
* name: "John Smith"

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