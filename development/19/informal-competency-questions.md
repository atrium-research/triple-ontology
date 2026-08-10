## Informal Competency Questions (Iteration 19)

## Question 1

### Identifier
CQ_19.1

### Question
What are the given name and the family name of the person behind a GoTriple profile?

### Expected Outcome
A list of profiles with their given name and family name (only for profiles that carry them).

### Result
* `profile_it19_1` → "Sofia", "Rossi"

### Based on
Example 1

## Question 2

### Identifier
CQ_19.2

### Question
Which disciplines is a profile interested in, either chosen by the user or automatically detected from the author's publications?

### Expected Outcome
A list of discipline concepts linked to the profile.

### Result
* `profile_it19_1` → `disc:cultural_heritage_and_museology`
* `profile_it19_1` → `disc:methods_and_statistics`

### Based on
Example 1

## Question 3

### Identifier
CQ_19.3

### Question
Which thesaurus keywords does a profile declare to know about?

### Expected Outcome
A list of structured keywords (defined terms) with their names.

### Result
* `profile_it19_1` → `kw_distant-reading_it19` ("Distant reading")

### Based on
Example 1

## Question 4

### Identifier
CQ_19.4

### Question
Which languages does a profile know?

### Expected Outcome
A list of languages linked to the profile.

### Result
* `profile_it19_1` → `language_it_it19` ("Italian")
* `profile_it19_1` → `language_en_it19` ("English")

### Based on
Example 1

## Question 5

### Identifier
CQ_19.5

### Question
Which organization is a profile affiliated with?

### Expected Outcome
The organization(s) the profile declared as affiliation, with their names.

### Result
* `profile_it19_1` → `organization_it19_1` ("University of Bologna")

### Based on
Example 1

## Question 6

### Identifier
CQ_19.6

### Question
What are the persistent identifiers of the persons behind GoTriple profiles, with their scheme and value?

### Expected Outcome
A list of (profile, identifier scheme, literal value) tuples covering the person PIDs (ORCID, IdRef, ISNI) and the OPERAS/GoTriple id, excluding the internal Elasticsearch id.

### Result
* `profile_it19_1` → `datacite:orcid` → "0000-0002-1825-0097"
* `profile_it19_1` → `triple:gotriple_id_schema` → "sofia_rossi_operas_0001"
* `profile_it19_1` → `triple:idref_schema` → "123456789"
* `profile_it19_2` → `datacite:isni` → "0000000121032683"

### Based on
Example 1 and Example 2

## Question 7

### Identifier
CQ_19.7

### Question
Which profiles belong to registered GoTriple users who are open to collaboration?

### Expected Outcome
The list of profiles with both flags set to true.

### Result
* `profile_it19_1`

### Based on
Example 1 and Example 2

## Question 8

### Identifier
CQ_19.8

### Question
What are the profile-card attributes of a registered user: self-description, pronouns, photo, personal web page and date of the last GoTriple update?

### Expected Outcome
One row with the optional descriptive attributes of the profile.

### Result
* `profile_it19_1` → "Digital historian working on computational analysis of cultural heritage collections."@en, "she/her", `https://gotriple.eu/media/profile/sofia-rossi.jpg`, `https://sofia-rossi.example.org`, "2026-06-15"

### Based on
Example 1

## Question 9

### Identifier
CQ_19.9

### Question
Which documents is a profile the author of (the `author_of` field, retrieved as the inverse of `schema:author`)?

### Expected Outcome
A list of (profile, document) pairs.

### Result
* `profile_it19_1` → `document_it19_1`
* `profile_it19_2` → `document_it19_1`

### Based on
Example 3

## Question 10

### Identifier
CQ_19.10

### Question
What are the internal id and the GoTriple persistent identifier (the `id` and `pid` fields) of a profile?

### Expected Outcome
One row per profile with the internal Elasticsearch id and, when present, the persistent identifier minted by GoTriple.

### Result
* `profile_it19_1` → "sofia_rossi_x8KfvrDgWBlxpw8Ve9U5I", "ark:/12345/profile-sofia-rossi"
* `profile_it19_2` → "joao_almeida_p2QhtsFjYDnzrw7Xg1W7K", "ark:/12345/profile-joao-almeida"

### Based on
Example 1 and Example 2
