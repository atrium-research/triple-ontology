# Motivating Scenario - Iteration 21

## Name
Links by role: reuse, references and access URLs

## General Description
The remaining ADR fields are all links, and the platform was carrying them in
three inconsistent shapes: URLs reified as identifiers, URLs as direct
properties, and URLs as typed literals (`"…"^^schema:URL`, plus a
`dcat:accessURL` literal that iteration 10's exemplar used without the model
ever declaring it). This iteration closes the fields and fixes the shape, under
one rule by the **role** the URL plays:

- **A. The URL identifies this record at a source** and several kinds must be
  told apart: the identifier pattern (datacite scheme + `litre:hasLiteralValue`)
  — the standing 3.0.0 decision for the Document's landing page, full text and
  source URLs. Unchanged.
- **B. The URL references another resource**: a direct object property with the
  URL as an IRI — `schema:isBasedOn` for derivation, `dcterms:references` for
  works the document refers to (the declared inverse of `dcterms:isReferencedBy`
  already in the model, closing an asymmetry left open by the ADR).
- **C. The URL is an access point**: a direct property with an IRI object —
  `schema:url` and `schema:mainEntityOfPage` on platform entities,
  `dcat:accessURL` (access page) and `dcat:downloadURL` (direct file) on
  `dcat:Distribution`, whose DCAT range `rdfs:Resource` demands IRIs.

A URL is **never a literal** outside the identifier reification: an IRI joins,
dereferences, and keeps the same triple shape if the referenced resource later
enters the KG. `shapes/url.shapes.ttl` enforces `sh:nodeKind sh:IRI`.

The occupation of a profile arrives from providers as a plain string: it is
carried by `schema:jobTitle` (range Text), not by `schema:hasOccupation`, whose
range demands an `Occupation` node. When an Occupation vocabulary exists,
`hasOccupation` will be added beside `jobTitle` without changing it.

## Examples
- Example 1: the article `document_it21_a` is a data paper based on an external
  dataset published on Zenodo (`schema:isBasedOn` → the Zenodo IRI) and refers
  the reader to the platform dataset `dataset_it21_b` (`dcterms:references`);
  the dataset declares the inverse (`dcterms:isReferencedBy`).
- Example 2: `dataset_it21_b` has one distribution: its access page on the
  provider's portal (`dcat:accessURL`) and the direct CSV file
  (`dcat:downloadURL`).
- Example 3: the profile `profile_it21_c` carries the provider-supplied
  occupation string "Research Software Engineer" as `schema:jobTitle`.
