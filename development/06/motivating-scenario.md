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
To facilitate the connection between an author agent and an account within GoTriple, 
a sophisticated mechanism has been established. 
For each author extracted from a publication, a temporary profile is created. 
Each profile is assigned an ID and the full name of the author derived from the corresponding publication(s).
Furthermore, in cases of ambiguity, the profile ID may be linked to another profile,
which the disambiguation system deems as the original. Ultimately, every profile is linked to a user account. 
If the account is associated with any publication and author, 
the profile corresponding to that author is considered claimed; otherwise, it will default to remaining unclaimed.

## Example 1
`document_1` has as the author of the publication. This author is represented by the `profile_78`, 
which has `author_fullname_6` as fullname and corresponds 
to another author that the system recognised as the original,
associated with `profile_85`. The profile created for the author of this document is claimed by a user 
who has created a user account on the platform: `account_78`.

## Example 2
`document_56` has 3 author associated respectively with three profiles: `profile_56`, `profile_09`, `profile_123`.
Each of these profile is a claimed. The `document_56` has 1 author associated with `profile_23`, who is not claimed by any account.

## Example 3
`account_45` have claimed 3 profiles: `profile_34`, `profile_43`, `profile_243`.
`profile_34` and `profile_43` has as original profile `profile_243`
