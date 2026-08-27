---
title: Datasets, Media Objects and Semantic Artefacts
terms: Dataset schema:Dataset dcat:Dataset dcat:Distribution dcat:distribution dcat:accessURL dcat:downloadURL dcat:bbox dcat:theme schema:size schema:version schema:encodingFormat schema:fileFormat schema:duration MediaObject schema:MediaObject SemanticArtefact mod:SemanticArtefact adms:representationTechnique
---

### 4.1. Preamble

Beyond publications, GoTriple describes three further kinds of research output,
each an entity in its own right: research data (`triple:Dataset`), audio-visual
material (`triple:MediaObject`) and formal knowledge representations
(`triple:SemanticArtefact`). A record becomes one of them by its content type.

In the current model the three classes are subclasses of `triple:Document`, so
everything of §3 — the descriptive core, the identifiers, the original values,
the classification — reaches them through inheritance. That subclassing is
today's mechanics, not the entities' essence: the design direction is toward
increasingly autonomous identities that keep a set of properties overlapping
with Document. This chapter describes what is *specific* to each.

<!-- figure: figures/specialized-documents.svg — embed when drawn -->

### 4.2. Datasets

A `triple:Dataset` is research data as a resource. Its structural superclasses
place it in both worlds: `schema:Dataset` on the Schema.org side,
`dcat:Dataset` on the DCAT side — and it is the DCAT half that carries the
data-specific structure.

Access to the data follows the **DCAT distribution pattern**: the dataset
points with `dcat:distribution` to one or more `dcat:Distribution` nodes, each
a concrete way of obtaining the data. A distribution carries `dcat:accessURL`
(the page where the data is reached) and/or `dcat:downloadURL` (the file
itself), plus its technical description: `schema:encodingFormat` (media type)
or `schema:fileFormat`, and `schema:size`. `schema:version` states which
release of the dataset the record describes.

<!-- figure: figures/dataset-distribution.svg — embed when drawn -->

Two more DCAT properties complete the picture. `dcat:bbox` gives the spatial
bounding box of the data — the DCAT-specific complement of the document-level
coverage of §3.5. `dcat:theme` carries the thematic category the *source
provider* originally assigned, from the provider's own vocabulary: it is
deliberately distinct from the GoTriple classification (§8), which is uniform
across the corpus.

### 4.3. Media Objects

A `triple:MediaObject` is an audio, video or image resource
(`schema:MediaObject` is its structural superclass). Its medium is what
distinguishes it: the encoding (`schema:encodingFormat`), the size, and — for
time-based media — `schema:duration`, an ISO 8601 duration such as `"PT42M"`.

### 4.4. Semantic Artefacts

A `triple:SemanticArtefact` is a formal knowledge representation described as a
resource: an ontology, a controlled vocabulary, a terminology, a model. The
identity comes from MOD (`mod:SemanticArtefact`, the Metadata for Ontology
Description vocabulary). `adms:representationTechnique` states how the artefact
is expressed (OWL, SKOS, …); `schema:version` which release the record
describes.

### 4.5. Vocabulary

The terms of this chapter, in reading order — each links to its full definition
in the reference sections at the bottom of this document:

<!-- definitions -->

### 4.6. Integrity Conditions

From [`shapes/`](https://github.com/atrium-research/triple-ontology/tree/main/shapes):

1. The three classes share the content-entity identifier profile of §5: exactly
   one internal id, exactly one ARK, at least one original identifier.
2. A `dcat:Distribution` carries its `dcat:accessURL` and `dcat:downloadURL` as
   IRIs, never as literals (`url.shapes.ttl`).
3. The subject-term rules of §8 and §10 (disciplines, thesaurus concepts) apply
   to all three classes exactly as to documents.

### 4.7. Example

A dataset with one distribution:

```turtle
<https://w3id.org/gto/dataset/example> a triple:Dataset ;
    schema:headline "Survey on digital reading practices"@en ;
    dcat:distribution [ a dcat:Distribution ;
        dcat:accessURL <https://data.example.org/survey2020> ;
        dcat:downloadURL <https://data.example.org/survey2020.csv> ;
        schema:encodingFormat "text/csv" ] ;
    schema:temporalCoverage "2019/2020" ;
    schema:spatialCoverage [ a schema:Place ; schema:name "France" ] .
```

### 4.8. Notes

**Why DCAT and not only Schema.org.** Schema.org describes a dataset as a
creative work; DCAT describes how to *get* it. The distribution pattern is the
part GoTriple actually needs — one dataset, several concrete access routes,
each with its own format — and no Schema.org construct expresses it as
directly.
