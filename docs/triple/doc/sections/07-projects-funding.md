---
title: Projects and Funding
terms: Project schema:Project frapo:Grant schema:Grant schema:FundingScheme schema:funding schema:funder frapo:isOutputOf schema:organizer schema:sponsor schema:startDate schema:endDate
---

### 7.1. Preamble

Research projects are first-class resources of the platform, alongside the
documents they produce: GoTriple aggregates tens of thousands of SSH projects
from funder databases and registries, and a user can discover a project the
same way they discover a publication.

### 7.2. The Project

A `triple:Project` (subclass of `schema:Project`) has at least one name
(`schema:name`, possibly multilingual), a lifecycle bounded by
`schema:startDate` and `schema:endDate` (each at most once, as `xsd:date`),
and its human context: `schema:organizer` for the organization running it,
`schema:sponsor` for a body supporting it. The descriptive fields it shares
with documents — abstract, keywords, disciplines — are the ones of §3 and §8,
reached through the common machinery, and its identifiers follow §5.
`triple:hasProjectType` classifies it against the ProjectType vocabulary (§8).

### 7.3. Funding

<!-- figure: figures/funding-chain.svg — embed when drawn -->

Funding is a chain of three links: the project points with `schema:funding` to
a `schema:Grant` (aligned with `frapo:Grant`, FRAPO's grant class); the grant
points with `schema:funder` to the body that awarded it; and that body is a
`schema:FundingScheme` — the funding programme (H2020, FP7, Horizon Europe)
under which the grant was made. `schema:FundingScheme` is a pending Schema.org
term, subclass of `schema:Organization`, which is what makes it admissible as
a funder.

Funding schemes are deliberately **not a controlled vocabulary**: they are
individuals carried with their display names. The corpus decides this — the
set of scheme names is open (any funder database can introduce new ones), the
overwhelming majority of records concentrate on a handful of programmes, and a
vocabulary would freeze a list that the sources keep extending.

### 7.4. Projects and Their Outputs

The link between a research output and the project it came from is
`frapo:isOutputOf`: asserted on the document, pointing at the project. The
direction matches how the data arrives — a publication declares its funding
acknowledgement — and the inverse question ("what did this project produce?")
is one SPARQL pattern away.

### 7.5. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 7.6. Integrity Conditions

From
[`shapes/entity.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/entity.shapes.ttl):

1. A project follows the content-entity identifier profile: exactly one
   internal id, exactly one ARK, at least one original identifier (§5.5) —
   projects are harvested from source registries like documents are.
2. At least one `schema:name`; at most one start date and one end date, both
   `xsd:date`.
3. The subject-term rules (§8) apply to projects as to every content entity.

### 7.7. Example

A funded project and one of its outputs:

```turtle
<https://w3id.org/gto/project/example> a triple:Project ;
    schema:name "TRIPLE"@en ;
    schema:startDate "2019-10-01"^^xsd:date ;
    schema:endDate "2023-03-31"^^xsd:date ;
    triple:hasProjectType <https://gotriple.eu/ontology/project-type/funded> ;
    schema:funding [ a schema:Grant ;
        schema:funder [ a schema:FundingScheme ; schema:name "H2020" ] ] .

<https://w3id.org/gto/document/example>
    frapo:isOutputOf <https://w3id.org/gto/project/example> .
```
