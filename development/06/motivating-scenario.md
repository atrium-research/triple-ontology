# Motivating Scenario (Iteration 6)

## Name
Author profile and user account

## Description

### General description
The GoTriple platform provides its users with a system for creating a personal profile.
Within this profile, users can link a variety of personal research-related information, 
such as their ORCID, mobile phone number, etc. Furthermore, it enables users to associate with 
and thereby claim their publications within the platform. 
This functionality is particularly beneficial for the operation of the platform. 
In instances of name ambiguity, the information provided by the user facilitates a more 
straightforward disambiguation of publications (referred to as "documents" in the context of this ontology).

### Technical specification
To facilitate the connection between authors and user accounts within GoTriple, a profile-based system has been established:

**Author Profiles:**
- For each author extracted from a publication, a profile (`triple:Profile`) is created
- Each profile is an instance of `triple:Profile` (subclass of `foaf:Person`)
- Profiles have a unique identifier (`datacite:Identifier`) and a name (`schema:name`)
- Documents link to author profiles using `schema:author` property

**Profile Claiming:**
- A profile can be "claimed" by linking it to a user account (`foaf:OnlineAccount`) via `foaf:account`
- If a profile has a `foaf:account`, it is considered **claimed**
- If a profile has no `foaf:account`, it is considered **unclaimed**
- One user account can claim multiple profiles (e.g., handling name variations)

**Disambiguation:**
- When the same author appears with different name variations, multiple profiles are created
- The property `triple:alsoKnownAs` links an ambiguous profile to the original (canonical) profile
- The disambiguation system identifies which profile is the "original" representation
- All related profiles can be claimed by the same user account

## Example 1: Document with Claimed Profile and Disambiguation

**Scenario**: `document_1` has one author represented by `profile_1`.

**Key metadata:**
- Document: `document_1`
- Author profile: `profile_1`
- Profile name: "John Smith"
- Given name: "John"
- Family name: "Smith"
- Profile identifier: `agent_identifier_2345678998765`
- Claimed by: `account_1`
- Also known as: `profile_2` (original profile identified by disambiguation system)

**Explanation**: The author appears in the publication with the name "John Smith", but the GoTriple disambiguation system has identified that this is the same person as `profile_2` (which has the abbreviated name "J. Smith"). Both profiles have been claimed by the same user account (`account_1`), confirming they represent the same researcher.

## Example 2: Document with Multiple Authors (Claimed and Unclaimed)

**Scenario**: `document_56` has 4 authors, three of which are claimed and one unclaimed.

**Key metadata:**
- Document: `document_56`
- Author profiles:
  - `profile_56` (name: "Maria Rossi", given: "Maria", family: "Rossi") - **claimed** by `account_109`
  - `profile_09` (name: "M. Rossi", given: "M.", family: "Rossi") - **claimed** by `account_109`, also known as `profile_56`
  - `profile_123` (name: "Maria R. Rossi", given: "Maria R.", family: "Rossi") - **claimed** by `account_109`, also known as `profile_56`
  - `profile_23` (name: "Pierre Dupont", given: "Pierre", family: "Dupont") - **unclaimed** (no account)

**Explanation**: Three authors of this document have claimed their profiles through the same user account, and the disambiguation system recognizes that `profile_09` and `profile_123` are name variations of `profile_56` (the same researcher "Maria Rossi" appearing with different name formats). The fourth author has not yet created an account on the platform.

## Example 3: User Account with Multiple Claimed Profiles

**Scenario**: `account_109` has claimed three profiles representing the same researcher.

**Key metadata:**
- User account: `account_109`
- Claimed profiles:
  - `profile_56` (name: "Maria Rossi", given: "Maria", family: "Rossi") - original profile
  - `profile_09` (name: "M. Rossi", given: "M.", family: "Rossi") - also known as `profile_56`
  - `profile_123` (name: "Maria R. Rossi", given: "Maria R.", family: "Rossi") - also known as `profile_56`

**Explanation**: This demonstrates how the platform handles author disambiguation. The same researcher appears in different publications with slight name variations ("Maria Rossi", "M. Rossi", "Maria R. Rossi"). The user has claimed all three profiles, and the system has linked `profile_09` and `profile_123` to `profile_56` as the canonical representation. The decomposition into given and family names helps identify these as variants of the same person.
