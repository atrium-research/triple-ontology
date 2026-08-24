# Serving the TRIPLE ontology

This directory is what gets deployed under `https://gotriple.eu/ontology/`. One
subdirectory per artefact, each with the HTML documentation (`index.html` + `static/`)
and the RDF serializations (`ontology.ttl`, `ontology.rdf`, `ontology.jsonld`):

| directory | serves |
|---|---|
| `triple/` | the consolidated model — every class, property and identifier scheme |
| `discipline/` | the Discipline vocabulary (27 concepts) |
| `content-type/` | the ContentType vocabulary (23) |
| `condition-of-access/` | the ConditionOfAccess vocabulary (10) |
| `license/` | the License vocabulary (13) |
| `project-type/` | the ProjectType vocabulary (7) |
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
| `/ontology/triple/{X.Y.Z}` | the **archived snapshot** of that release (`200`, forever) | its own `ontology.{ttl,rdf,jsonld}` |
| `/ontology/triple/{Term}` | `302` → `/ontology/triple#{Term}` | `triple/ontology.ttl` (etc.) |
| `/ontology/{voc}` | `{voc}/index.html` | `{voc}/ontology.ttl` (etc.) |
| `/ontology/{voc}/{key}` | `302` → `/ontology/{voc}#{key}` | `{voc}/ontology.ttl` (etc.) |
| anything else | **real 404** | **real 404** |

`{voc}` ∈ `discipline`, `content-type`, `condition-of-access`, `license`, `project-type`,
`ddc` — a closed list that changes only when a vocabulary is created.

Worked examples:

```
/ontology/triple/originalLicense      →  302  /ontology/triple#originalLicense
/ontology/triple/Document             →  302  /ontology/triple#Document
/ontology/discipline/musiq            →  302  /ontology/discipline#musiq
/ontology/ddc/930.1                   →  302  /ontology/ddc#930.1
/ontology/license                     →  200  license/index.html
/ontology/triple/3.1.0                →  200  archived snapshot of release 3.1.0
/ontology/nonexistent                 →  404
```

Note that the *bridge classes* (`…/ontology/triple/License` and friends, capitalised)
are model terms and follow the model rule; the lowercase `…/ontology/license` is the
vocabulary. The two are different IRIs on purpose.

### Sketch (nginx)

```nginx
location = /ontology/triple { # negotiate: html → triple/index.html, rdf → triple/ontology.*
}
location ~ ^/ontology/(discipline|content-type|condition-of-access|license|project-type|ddc)$ {
    # negotiate: html → $1/index.html, rdf → $1/ontology.*
}
location ~ ^/ontology/(discipline|content-type|condition-of-access|license|project-type|ddc)/(.+)$ {
    # html → 302 /ontology/$1#$2 ; rdf → $1/ontology.*
}
location ~ ^/ontology/triple/(\d+\.\d+\.\d+)(/.*)?$ {
    # archived release snapshot: serve archive/$1/… with content negotiation, 200 forever.
    # MUST be evaluated before the term rule below. No TRIPLE term begins with a digit.
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

## Versioned snapshots

Every published release stays resolvable forever (OpenCitations-style):
`/ontology/triple/{X.Y.Z}` serves the frozen page and serializations of that release,
never a redirect to current. At deployment time each release's directory is unpacked
from the GitHub release archive (`ontology/html/` inside the tag) into the versioned
path and never touched again. The semver pattern is reserved before the term rule —
safe because no TRIPLE term begins with a digit, and DDC notations carry at most one
dot. The same layout applies to the vocabularies; an unchanged vocabulary keeps the
versionIRI of the last release that changed it.

## Regenerating

From the repo root, venv active (see `CLAUDE.md`): `scripts/merge_iterations.py
--output ontology/triple.ttl` (model), then `scripts/build_docs.sh ontology/html` —
one command regenerates all seven pages (the model plus the six vocabularies, each
with its `index.html`, `static/` and `.ttl`/`.rdf`/`.jsonld` serializations),
recompiling the vocabularies via `scripts/build.py` first so no page is rendered
from stale input. Renderer: the vendored pyLODE fork in `tools/pylode/` (its
`PATCHES.md` documents the anchor scheme and the chapter system). No
post-processing: the `%23` anchor-encoding step is retired. Without an argument
the same build lands in `build/docs-preview/` for inspection.
