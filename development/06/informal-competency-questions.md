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
* given name: "John"
* family name: "Smith"
* also known as: `profile_2`

### Based on
Example 1


## Question 2

### Identifier
CQ_6.2

### Question
Return all claimed authors of `document_56`.

### Expected Outcome
A list of author profiles that have been claimed by a user account.

### Result
* `profile_56` (claimed by account_109)
* `profile_09` (claimed by account_109)
* `profile_123` (claimed by account_109)

### Based on
Example 2


## Question 3

### Identifier
CQ_6.3

### Question
Return all profiles claimed by `account_109`.

### Expected Outcome
A list of profiles claimed by the user account.

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
Return the original profile for `profile_123`.

### Expected Outcome
The canonical profile identified by the disambiguation system.

### Result
* `profile_56`

### Based on
Example 3


## Question 5

### Identifier
CQ_6.5

### Question
Return all names (fullnames) associated with profiles claimed by `account_109`.

### Expected Outcome
A list of names from all profiles claimed by the account.

### Result
* "Maria Rossi"
* "M. Rossi"
* "Maria R. Rossi"

### Based on
Example 3


## Question 6

### Identifier
CQ_6.6

### Question
Return all profiles with family name "Rossi" and their given names.

### Expected Outcome
A list of profiles sharing the same family name with their given name variations.

### Result
* `profile_56` - given name: "Maria", family name: "Rossi"
* `profile_09` - given name: "M.", family name: "Rossi"
* `profile_123` - given name: "Maria R.", family name: "Rossi"

### Based on
Example 2 and Example 3