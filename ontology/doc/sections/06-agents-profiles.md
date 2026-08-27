---
title: Agents and Profiles
terms: Profile foaf:Agent foaf:Person foaf:Organization schema:Person schema:Organization foaf:name foaf:givenName foaf:familyName schema:name schema:alternateName schema:jobTitle pronouns schema:affiliation registeredUser openToCollaboration schema:description schema:image schema:email schema:contactPoint schema:ContactPoint schema:url foaf:account foaf:OnlineAccount schema:knowsAbout schema:knowsLanguage foaf:topic_interest
---

### 6.1. Preamble

Two populations of agents meet on the platform: **authors extracted from
harvested document metadata** — names that arrived attached to a publication —
and **registered GoTriple users**, who created an account and curate their own
presence. The model deliberately gives both the same class, `triple:Profile`,
and tells them apart with one boolean, `triple:registeredUser`: an extracted
author who later registers becomes a richer version of the same thing, not a
different thing.

### 6.2. People and Organizations

A profile is a person or an organization: `triple:Profile` is a subclass of
the union of `foaf:Person` and `foaf:Organization` (with `schema:Person` and
`schema:Organization` as their Schema.org counterparts, and `foaf:Agent` above
both). Naming follows FOAF: every profile carries exactly one `foaf:name`, and
people may add `foaf:givenName` and `foaf:familyName`; `schema:alternateName`
records aliases and name variants. `schema:name` is the generic Schema.org
naming property, reserved in this model for *things* — projects, places,
defined terms — while agents are named with `foaf:name` (§3.9).

A person's professional context is `schema:jobTitle` and
`schema:affiliation` (the organization they belong to);
`triple:pronouns` carries the personal pronouns the user chose for their
profile (e.g. `"she/her"`).

### 6.3. The Profile

<!-- figure: figures/profile.svg — embed when drawn -->

What a registered user curates, an extracted author simply does not have:

- **Self-description** — `schema:description` (the free-text bio) and
  `schema:image` (the personal picture chosen by the user).
- **Contacts** — `schema:email`, `schema:contactPoint` (a
  `schema:ContactPoint` node), and `schema:url` for personal web pages.
- **The platform account** — `foaf:account` points to at most one
  `foaf:OnlineAccount`, the GoTriple account itself; a profile without one is
  an extracted author.
- **Collaboration** — `triple:openToCollaboration` states whether the user
  declared themselves open to collaborating with other GoTriple users.

### 6.4. Expertise and Interests

Three properties describe what an agent knows and cares about.
`schema:knowsAbout` carries the topics of expertise; Schema.org declares it
for Person and Organization, which is exactly the domain of a profile — and
its value is constrained *per class* (an `owl:allValuesFrom` on
`triple:Profile`), never globally, because a global range on somebody else's
property would type every use of it everywhere. `schema:knowsLanguage` lists
the languages the agent works in. `foaf:topic_interest` is the weaker signal:
a topic of *interest*, not a claim of expertise.

### 6.5. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 6.6. Integrity Conditions

From
[`shapes/entity.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/entity.shapes.ttl):

1. A profile carries exactly one internal id and exactly one ARK — and **no
   original identifier**: profiles are born inside the platform, not
   harvested (§5.5).
2. Exactly one `foaf:name`; at most one `foaf:account`.
3. A `foaf:OnlineAccount` — a platform-created entity — carries exactly one
   internal id.
4. Person identifiers (ORCID, ISNI, IdRef, the GoTriple id) follow the
   identifier pattern of §5, distinguished by their schemes.

### 6.7. Example

A registered user:

```turtle
<https://w3id.org/gto/profile/example> a triple:Profile , foaf:Person ;
    foaf:name "Marie Dupont" ;
    triple:registeredUser true ;
    triple:openToCollaboration true ;
    schema:jobTitle "Research fellow"@en ;
    schema:knowsAbout <http://semantics.gr/authorities/SSH-LCSH/example-concept> ;
    foaf:account [ a foaf:OnlineAccount ] ;
    datacite:hasIdentifier [ a datacite:Identifier ;
        datacite:usesIdentifierScheme datacite:orcid ;
        litre:hasLiteralValue "0000-0002-1825-0097" ] .
```
