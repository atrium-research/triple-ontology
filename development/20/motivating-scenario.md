# Motivating Scenario - Iteration 20

## Name
Deduplication as a directed link to the representative record

## General Description
GoTriple harvests the same scholarly work from several providers: the platform
computes which records describe the same work and elects one of them — the
*representative* — whose consolidated values are surfaced to users. Iteration 05
modelled this with a dedicated `triple:Cluster` node and a `triple:inCluster`
property. That model has been retired: production has no cluster entity (the
representative is itself a document, and the siblings reference its identifier as
their `cluster_id`), a cluster node would have to be minted with a fabricated IRI,
and — with one named graph per document — it would live in no document's graph,
requiring its own maintenance cycle. Verified empirically on a QLever instance:
the node model and the link model answer the same competency questions, but only
the node model leaves orphan structures behind when a record is withdrawn.

The replacement is a single directed property: a duplicate record points at the
representative record with `triple:isDuplicateOf`. The direction carries the
role — the representative is the target and asserts nothing. Records with no
`isDuplicateOf` in either direction are singletons. The property specialises
`prov:alternateOf` ("alternate entities present aspects of the same thing"),
whose symmetry is exactly what the specialisation adds direction to.

## Technical Specification
- `triple:isDuplicateOf`: object property, `rdfs:subPropertyOf prov:alternateOf`.
  Subject and object are records of the same content entity (here exemplified on
  `triple:Document`; the same link applies to the other content entities).
- The representative carries no dedup assertion: its role is being the target.
- The API fields derive: `is_duplicate` = has an outgoing `isDuplicateOf`;
  `is_cluster` = is a target; `cluster_id` = the target's identifier;
  `cluster_children_count` = COUNT of incoming links + 1.
- Chains are ill-formed (a representative is never itself a duplicate) and
  self-links are ill-formed: both are checked in `shapes/`, not in OWL.
- The deduplicated view filters with `FILTER NOT EXISTS { ?d triple:isDuplicateOf ?r }`.

## Examples
- Example 1: the work "De l'esthétique au présent" (De Boeck Supérieur, 1998) is
  harvested twice. The record from HAL/Isidore (`document_it20_rep`) is elected
  representative and carries the consolidated values: content type book, topics
  Philosophy and Sociology, French. The record from BASE (`document_it20_dup`)
  is its duplicate and points at it with `triple:isDuplicateOf`.
- Example 2: the document "Revendication. Obligation de revendiquer, Application,
  Biens confisqués" (`document_it20_single`) was harvested once: no dedup link in
  either direction — a singleton, present as-is in the deduplicated view.
