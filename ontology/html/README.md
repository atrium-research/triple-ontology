# Serving the TRIPLE ontology

This directory is what gets deployed under `https://gotriple.eu/ontology/`. One
subdirectory per artefact, each with the HTML documentation (`index.html` + `static/`)
and the RDF serializations (`ontology.ttl`, `ontology.rdf`, `ontology.jsonld`):

| directory | serves |
|---|---|
| `triple/` | the consolidated model — every class, property and identifier scheme |
| `discipline/` | the Discipline vocabulary (27 concepts) |
| `content-type/` | the ContentType vocabulary (23) |
| `access-condition/` | the AccessCondition vocabulary (10) |
| `license/` | the License vocabulary (13) |
| `project-type/` | the ProjectType vocabulary (8) |
| `ddc/` | the Dewey Decimal Classification proxies (53) |

## Resolution rules

Everything under `/ontology/` is decided by the **first path segment**: `triple` is the
model, one of the six vocabulary names is a vocabulary, anything else is 404. No lookup
tables: the fragment is always the last segment of the requested IRI, and the anchors
in the generated pages are guaranteed to match (verified at build time, 38/38 terms and
133/133 concepts).

| request | `Accept: text/html` (default) | `text/turtle`, `application/rdf+xml`, `application/ld+json` |
|---|---|---|
| `/ontology/triple` | `triple/index.html` | `triple/ontology.{ttl,rdf,jsonld}` |
| `/ontology/triple/{Term}` | `302` → `/ontology/triple#{Term}` | `triple/ontology.ttl` (etc.) |
| `/ontology/{voc}` | `{voc}/index.html` | `{voc}/ontology.ttl` (etc.) |
| `/ontology/{voc}/{key}` | `302` → `/ontology/{voc}#{key}` | `{voc}/ontology.ttl` (etc.) |
| anything else | **real 404** | **real 404** |

`{voc}` ∈ `discipline`, `content-type`, `access-condition`, `license`, `project-type`,
`ddc` — a closed list that changes only when a vocabulary is created.

Worked examples:

```
/ontology/triple/originalLicense      →  302  /ontology/triple#originalLicense
/ontology/triple/Document             →  302  /ontology/triple#Document
/ontology/discipline/musiq            →  302  /ontology/discipline#musiq
/ontology/ddc/930.1                   →  302  /ontology/ddc#930.1
/ontology/license                     →  200  license/index.html
/ontology/nonexistent                 →  404
```

Note that the *bridge classes* (`…/ontology/triple/License` and friends, capitalised)
are model terms and follow the model rule; the lowercase `…/ontology/license` is the
vocabulary. The two are different IRIs on purpose.

### Sketch (nginx)

```nginx
location = /ontology/triple { # negotiate: html → triple/index.html, rdf → triple/ontology.*
}
location ~ ^/ontology/(discipline|content-type|access-condition|license|project-type|ddc)$ {
    # negotiate: html → $1/index.html, rdf → $1/ontology.*
}
location ~ ^/ontology/(discipline|content-type|access-condition|license|project-type|ddc)/(.+)$ {
    # html → 302 /ontology/$1#$2 ; rdf → $1/ontology.*
}
location ~ ^/ontology/triple/([^/]+)$ {
    # html → 302 /ontology/triple#$1 ; rdf → triple/ontology.*
}
location /ontology/ { return 404; }   # never fall through to the frontend catch-all
```

Two requirements that are easy to miss:

- **404 must be a real 404.** Serving the frontend's not-found page with status 200
  poisons RDF clients, which then try to parse HTML as data.
- The redirects are plain string operations on the request path — the fragment is the
  last path segment, verbatim. Nothing needs to know which terms exist.

## Regenerating

From the repo root, venv active (see `CLAUDE.md`): `scripts/merge_iterations.py
--output ontology/triple.ttl` (model) and `scripts/build.py` (vocabularies, into
`build/`), then pyLODE — the customized fork in `~/netseven_work/lode/` (its
`PATCHES.md` documents the anchor scheme) — and copy `index.html` plus the three
serializations here. No post-processing: the `%23` anchor-encoding step is retired.
