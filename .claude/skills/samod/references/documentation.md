# Documentation style — the SKOS-Reference-shaped model page

Established 2026-08-12 while prototyping the 3.x documentation. The model page
(`ontology/html/triple/`) is organized like the W3C SKOS Reference: numbered
narrative chapters on top, the complete term reference at the bottom.

## Source layout (in this repository)

| What | Where |
|---|---|
| Narrative chapters | `ontology/doc/sections/NN-slug.md` (order = filename number) |
| Per-term Graffoo diagrams | `ontology/doc/figures/{anchor}.svg` (or `.png`; `:` in the anchor becomes `-`) — hand-authored in yEd (Graffoo palette), human-led |
| Build wrapper | `scripts/build_docs.sh [output-base]` — builds ALL seven pages (model + six vocabularies, serializations included; recompiles the vocabularies first) plus the landing card index at the root (`scripts/build_index.py`). No argument = preview; `ontology/html` = official pages |

The generator is the **vendored pyLODE fork** in `tools/pylode/` (see
`tools/pylode/PATCHES.md` for every deviation from upstream); it runs on the
`scripts/` virtualenv:

```bash
scripts/build_docs.sh                 # anteprima in build/docs-preview/{triple,discipline,...} (git-ignored)
scripts/build_docs.sh ontology/html   # promozione alle pagine ufficiali (modello + 6 vocabolari)
```

## Chapter file format

```markdown
---
title: Documents
terms: Document schema:headline schema:abstract aggregator
---
### 3.1. Preamble
prose…
### 3.4. Vocabulary
intro line…
<!-- definitions -->
### 3.5. Integrity Conditions
prose…
```

- `terms` lists the page **anchors** of the terms the chapter discusses: bare
  local name for `triple:` terms, `prefix:LocalName` for borrowed ones.
- The chapter's **Vocabulary link-list renders at the `<!-- definitions -->`
  marker** — write the "N.x. Vocabulary" heading right before it. Without the
  marker the list follows the whole prose.
- Prose `###` headings get derived ids (`sec-{chapter}-{heading-slug}`) and feed
  the nested ToC automatically. Subsection numbers (`3.1.`, `3.2.`) are written
  by hand in the markdown; renumber when restructuring a chapter.
- Unknown terms produce a generation WARNING; the CLI also reports coverage
  (terms referenced by at least one chapter / total). Goal state: full coverage.

## The depth rule (where each kind of text belongs)

- **Chapters carry the depth**: motivations, lifecycles, distinctions, edge
  cases, worked examples, integrity conditions in natural language. Prose costs
  the RDF nothing and is versioned as markdown.
- **Entity boxes stay terse** — they are reference cards, and their guidance
  lives *in the RDF* at the term's home iteration, so it ships with every
  serialization:
  - `rdfs:comment` — one per term per language (enforced by `check_model.py`);
  - `skos:scopeNote` — the "Usage" box: one solid paragraph, no essays;
  - `skos:example` — the "Example" box: one compact Turtle snippet.
- Chapters and entities cross-link both ways: the Vocabulary list points down to
  the definitions; every cited term shows "Discussed in §N" back to its chapter.
- Chapters are an **overlay**: they never touch IRIs or anchors, and the term
  definitions always live in the reference sections at the bottom of the page
  (URI-CONVENTIONS §2: grouping is reorganizable without touching identifiers).

## Diagrams

Diagrams are **hand-authored** in yEd with the Graffoo palette (like the
iteration modelets, issue #34) and exported to
`ontology/doc/figures/{anchor}.svg` — the page embeds them automatically in the
term's entity box (contained size, click for full view). Claude can draft the
neighbourhood facts of a class (superclasses, restriction arcs, targets,
cardinalities) from the model as input for the drawing; the drawing itself is
human-led. After a model change, re-check the affected diagrams by hand: they
are not regenerated.
