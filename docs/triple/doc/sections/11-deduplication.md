---
title: Deduplication
terms: isDuplicateOf prov:alternateOf
---

### 11.1. Preamble

A document is the record of *one* provider's description (§3.1), so the same
publication legitimately appears many times in the corpus — once per source
that describes it. Deduplication is how the platform relates those records
without destroying them.

The design went through a real alternative. An earlier model reified the
group: a `Cluster` entity, with every member record pointing into it. It was
retired in favor of the current design — **one directed link**,
`triple:isDuplicateOf`, from each duplicate record straight to the elected
representative. The cluster still exists, but as a *view* (the set of records
sharing a representative), not as an entity that must be minted, named and
maintained; and the common operation — "give me the representative" — became a
single triple instead of a join through a hub node.

### 11.2. The Duplicate Link

<!-- figure: figures/deduplication-link.svg — embed when drawn -->

`triple:isDuplicateOf` reads: *this record is a duplicate; the resource it
describes is represented by the record it points at.* The direction is fixed
— duplicate → representative — and a representative never points anywhere: it
is recognizable precisely by carrying no outgoing link. A consumer collapsing
a result list keeps every record without a link and replaces every record
with one by its target. Nothing is merged: each record keeps its provider,
its identifiers and its original values.

The property is a sub-property of `prov:alternateOf` — PROV's "two entities
presenting aspects of the same thing". The alignment is deliberately to the
*weak* PROV notion: `prov:alternateOf` is reflexive, symmetric and transitive
by specification, while `triple:isDuplicateOf` adds the direction and the
single-hop discipline that PROV does not have — every duplicate statement is
also a correct alternateOf statement, but not vice versa.

Deduplication does not assert FRBR identity: the linked records may describe
different expressions or manifestations of the same work (§3.2). The link
means "same resource *for discovery*", which is the platform's notion of
sameness.

### 11.3. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 11.4. Integrity Conditions

From
[`shapes/dedup.shapes.ttl`](https://github.com/atrium-research/triple-ontology/blob/main/shapes/dedup.shapes.ttl):

1. A record has **at most one** representative.
2. **No chains**: a representative is never itself a duplicate
   (`isDuplicateOf/isDuplicateOf` is empty).
3. **No self-loops**: a record never declares itself its own representative.

### 11.5. Example

Three providers, one publication:

```turtle
<https://w3id.org/gto/document/hal-1234>  triple:isDuplicateOf
    <https://w3id.org/gto/document/openedition-5678> .
<https://w3id.org/gto/document/base-9012> triple:isDuplicateOf
    <https://w3id.org/gto/document/openedition-5678> .
# openedition-5678 carries no link: it is the representative.
```
