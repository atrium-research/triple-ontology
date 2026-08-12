# Documentation sources

Sources of the model documentation page, rendered by `scripts/build_docs.sh`
with the vendored pyLODE fork (`tools/pylode/`).

- `sections/NN-slug.md` — the narrative chapters (SKOS-Reference style). Each
  file has a `title:`/`terms:` front-matter; `terms` lists the page anchors the
  chapter discusses. The `<!-- definitions -->` marker positions the chapter's
  Vocabulary link-list.
- `figures/{anchor}.svg` — per-term Graffoo diagrams, hand-authored in yEd;
  the page embeds them automatically in the term's entity box.

Authoring rules: `.claude/skills/samod/references/documentation.md`.
