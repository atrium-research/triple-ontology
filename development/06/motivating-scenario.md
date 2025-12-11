# Motivating Scenario (Iteration 6)

## Name
Author profile and user account

## Description

### General description
The GoTriple platform provides its users with a system for creating a personal profile.
Within this profile, users can link a variety of personal research-related information, 
such as their ORCID, mobile phone number, etc. Furthermore, it enables users to associate 
their publications within the platform. 
This functionality is particularly beneficial for the operation of the platform. 
In instances of name ambiguity, the information provided by the user facilitates a more 
straightforward disambiguation of publications (referred to as "documents" in the context of this ontology).

### Technical specification
To facilitate the connection between authors and user accounts within GoTriple, a profile-based system has been established:

**Author Profiles:**
- For each author extracted from a publication, a profile (`triple:Profile`) is created
- Each profile is an instance of `triple:Profile` (can be either `foaf:Person` or `foaf:Organization`)
- Profiles have a unique identifier (`datacite:Identifier`) and a name (`schema:name`)
- Documents link to author profiles using `schema:author` property

**Profile and User Accounts:**
- A profile can be linked to a user account (`foaf:OnlineAccount`) via `foaf:account`
- If a profile has a `foaf:account`, it is associated with a user
- If a profile has no `foaf:account`, it is not associated with any user
- One user account can be associated with multiple profiles (e.g., handling name variations)

**Disambiguation:**
- When the same author appears with different name variations, multiple profiles are created
- All related profiles can be associated with the same user account

## Example 1: Document with Claimed Profile and Disambiguation

**Scenario**: `document_1` has one author represented by `profile_1`.

**Key metadata:**
- Document: `document_1`
- Author profile: `profile_1`
- Profile name: "John Smith"
- Profile identifier: `agent_identifier_2345678998765`
- Associated with: `account_1`

**Explanation**: The author appears in the publication with the name "John Smith". The profile has been associated with user account `account_1`.

## Example 2: Document with Multiple Authors (Associated and Unassociated)

**Scenario**: `document_56` has 4 authors, three of which are associated with an account and one unassociated.

**Key metadata:**
- Document: `document_56`
- Author profiles:
  - `profile_56` (name: "Maria Rossi") - associated with `account_109`
  - `profile_09` (name: "M. Rossi") - associated with `account_109`
  - `profile_123` (name: "Maria R. Rossi") - associated with `account_109`
  - `profile_23` (name: "Pierre Dupont") - not associated with any account

**Explanation**: Three authors of this document have their profiles associated with the same user account (`profile_56`, `profile_09`, and `profile_123` are all associated with `account_109`). The fourth author has not yet created an account on the platform.

## Example 3: User Account with Multiple Associated Profiles

**Scenario**: `account_109` is associated with three profiles representing the same researcher.

**Key metadata:**
- User account: `account_109`
- Associated profiles:
  - `profile_56` (name: "Maria Rossi")
  - `profile_09` (name: "M. Rossi")
  - `profile_123` (name: "Maria R. Rossi")

**Explanation**: This demonstrates how the platform handles author profiles. A researcher may appear in different publications with slight name variations ("Maria Rossi", "M. Rossi", "Maria R. Rossi"). The user account can be associated with all three profiles.
