# TRIPLE URI Conventions

Normative rules for minting and maintaining IRIs. Established at 3.0.0 (2026-08-10);
every rule below is enforced either by a script (named where it applies) or by review.
Resolution — what the server does with these IRIs — is specified in
`ontology/html/README.md`; this file is about *naming*.

## 1. Namespaces

| space | namespace | holds |
|---|---|---|
| model | `https://gotriple.eu/ontology/triple/` | every class, property and identifier scheme of the ontology |
| vocabulary | `https://gotriple.eu/ontology/{vocabulary}/` | the concepts of one controlled vocabulary |
| DDC proxies | `https://gotriple.eu/ontology/ddc/` | local proxies for Dewey classes (mapping targets only) |
| resources | `https://w3id.org/gto/{type}/{reference}` | the platform's data: documents, profiles, projects… |
| named graphs | the document's own IRI | one graph per document |

Separator is always the **slash**, never the hash (standardized in 2.1.0). Document
IRIs (the ontology, a vocabulary) carry **no trailing slash**; the namespace they open
is the same IRI plus `/`. Nothing else lives at the top of `…/ontology/` — a new name
there means a new vocabulary, which is a reviewed, deliberate act.

The model and the vocabularies are **siblings, not nested**: `…/ontology/triple/License`
is the bridge class (a model term), `…/ontology/license` is the vocabulary. Case and
path depth keep the two spaces disjoint.

## 2. Minting rules by kind

| kind | pattern | examples |
|---|---|---|
| class | `UpperCamelCase` | `Document`, `AccessCondition`, `Cluster` |
| object property | `lowerCamelCase`; `has{Class}` when it bridges to a vocabulary | `hasLicense`, `inCluster`, `aggregator` |
| datatype property | `lowerCamelCase` | `originalLicense`, `isDiscarded`, `confidence` |
| identifier scheme | `snake_case` ending in `_schema` | `internal_id_schema`, `gotriple_id_schema` |
| vocabulary | `kebab-case`, lowercase, English | `discipline`, `content-type`, `access-condition` |
| concept | **the production key, verbatim** | `musiq`, `typ_article`, `acr_open-access`, `other` |
| DDC proxy | the DDC notation | `780`, `930.1` |

The concept rule is the load-bearing one: a concept's local name is exactly the value
the GoTriple API emits for it, so mapping a record is namespace + key with no lookup.
Its consequences:

- the key is also asserted as `skos:notation`, so it exists as a queryable literal;
- concepts are **never minted speculatively** — a concept enters a vocabulary when the
  platform emits its key (checked against the corpus-wide `aggs` counts), with the
  reviewed exception of never-yet-observed tail terms inherited from provider lists;
- inconsistencies of the platform (bare `other`/`undefined` beside prefixed keys) are
  reproduced, not repaired: the IRI mirrors production, warts included.

Terms live **flat** in their namespace — no thematic sub-paths (`…/triple/Document/cluster`
is wrong). Grouping into documentation pages is an overlay that must stay reorganizable
without touching identifiers.

## 3. Term identity

- **One home per term**: a term is declared and documented by exactly one iteration
  (`scripts/check_model.py`, "one comment per term").
- **No axioms on foreign terms**: never `rdfs:range`/`domain`/`subPropertyOf` on a term
  we do not own, beyond verified restatements (`check_model.py` baseline). Constrain on
  the class via `owl:allValuesFrom`, or in `shapes/`.
- **No vocabulary individuals outside their vocabulary**: exemplar data must not mint
  `triple:cc_by_4_0`-style individuals; it points at the vocabulary concept.
- **No individual named as a namespace** (a subject IRI equal to a namespace with its
  trailing slash has an empty local name and can never resolve or anchor).
- A released IRI is **never renamed silently**: renaming is a breaking change, recorded
  in the CHANGELOG with a crosswalk.

## 4. External alignment

- `skos:exactMatch` asserts identity: at most **one per target vocabulary**, and only
  when the target's preferred label is equivalent to ours. Everything else — parts of
  composites, narrower/broader neighbours, classification classes (DDC) — is
  `skos:closeMatch`.
- Labels are **borrowed only across `skos:exactMatch`**, never across a close match
  (a close match's label names a different thing).
- Alignment targets are resolved and checked at review time: no links to redirect
  stubs, disambiguation or category pages — and no `exactMatch` to a target whose
  definition cannot be verified.
- **The exactMatches of one term must be mutually compatible**: identity is
  transitive, so `A exactMatch B` and `A exactMatch C` claims `B ≡ C` — if that
  is implausible (a Work-level class beside a record-level one), one of them is
  a close match. Structural reuse is `rdfs:subClassOf`'s job, not `exactMatch`'s:
  "every X is a Y" is a subclass axiom (`triple:Profile ⊑ foaf:Agent`), not an
  identity.

## 5. Documentation addresses

The HTML anchor of a term is derived from its IRI alone: own terms anchor under the
bare local name (`#originalLicense`, `#musiq`, `#780`), borrowed terms under their
prefixed name (`#foaf:Document`). This is what makes `…/triple/{Term} → …/triple#{Term}`
a pure string rule on the server. Anchors therefore never contain `#`, and every
namespace used by the model must have a declared prefix (else the anchor degrades to
the full IRI — checked at regeneration).

## 6. Versioning

`owl:versionInfo` (semantic) on the ontology and every vocabulary, single-sourced from
`ontology/metadata.ttl`; GitHub releases carry the artefacts. `owl:versionIRI` — dated,
in the OpenCitations style — is planned for the 3.0.0 release chore and not yet minted;
its pattern must not collide with the flat term space (this rules out bare
`…/triple/{X.Y.Z}` until the routing reserves a digits-only pattern).

## 7. URLs

A URL is handled by the **role it plays**, not by the field it arrives in:

| role | pattern | examples |
|---|---|---|
| **A** — identifies *this* record at a source, and several kinds must be told apart | identifier reification: `datacite:Identifier` + URL scheme + `litre:hasLiteralValue` | the Document's landing page, full text and source URLs |
| **B** — references *another* resource | direct object property, **URL as IRI** | `schema:isBasedOn`, `dcterms:references` |
| **C** — access point of a platform entity or distribution | direct property, **URL as IRI** | `schema:url`, `schema:mainEntityOfPage`, `dcat:accessURL`, `dcat:downloadURL` |

Outside the identifier reification a URL is **never a literal** (`"…"^^schema:URL`
is a dead end: it cannot be joined or dereferenced, and the triple changes shape
the day the resource enters the KG). Enforced by `shapes/url.shapes.ttl`
(`sh:nodeKind sh:IRI`). Established in iteration 21; the Document's role-A
treatment is the 3.0.0 identifier decision and predates it.
