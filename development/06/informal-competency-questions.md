## Informal Competency Questions (Iteration 6)

## Question 1

### Identifier
CQ_6.1

### Question
Return all triples that have as subject the `profile_78`.

### Expected Outcome
A profile with all associated properties and values.

### Result
* fullname: `person_fullname_6`
* also known as: `profile_85`
* id: `profile_id_67`
* is claimed: True
* account: `account_78`

### Based on
Example 1


## Question 2

### Identifier
CQ_6.2

### Question
Return all claimed author of the `document_56`.

### Expected Outcome
a list of authors.

### Result
* `profile_56`
* `profile_09`
* `profile_123`

### Based on
Example 2


## Question 3

### Identifier
CQ_6.3

### Question
Return all profiles associated with `account_45`.

### Expected Outcome
a list of agents.

### Result
* `profile_34`
* `profile_43`
* `profile_243`

### Based on
Example 3


## Question 4

### Identifier
CQ_6.4

### Question
Return for `profile_34` the original profile.

### Expected Outcome
an Agent.

### Result
* `profile_243`

### Based on
Example 3


## Question 5

### Identifier
CQ_6.5

### Question
Return all the fullname defined for the account `account_45`.

### Expected Outcome
a list of string.

### Result
* `person_fullname_6`
* `person_fullname_87`

### Based on
Example 1