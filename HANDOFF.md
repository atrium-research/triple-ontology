# Handoff — taking the TRIPLE ontology to 100 % on FOOPS!

State as of **2026-09-30**. Every number below was measured, not estimated, with
FOOPS! v0.4.0 (https://github.com/oeg-upm/fair_ontologies) — the reference FAIR
validator for ontologies. Read §1 first: the public instance at
https://foops.linkeddata.es **cannot see gotriple.eu at all** (§2.1), so it will
report ~4 % whatever you do until the edge is fixed. Measure locally.

## 0. Where we are

| run | what was assessed | score |
|---|---|---|
| public instance | `https://gotriple.eu/ontology/triple` | **4.2 %** — every URL on the host "not resolvable" (TLS, see §2.1) |
| public instance | OpenCitations OCO, as a control | 72.9 % — the validator itself works |
| local, JDK 21 | `https://gotriple.eu/ontology/triple` (what is deployed today) | **64.9 %** — resolution tests all green |
| local, JDK 21 | the same file, before today's change, served from localhost | 60.8 % |
| local, JDK 21 | the file **with today's five metadata triples**, same conditions | **77.1 %** |
| local, JDK 21, 2026-10-01 | the same file, after the edge started refusing Java clients | 62.5 % — see §2.1 |
| projection | today's file once deployed at the canonical IRI | **81.2 %** |

Today's change (uncommitted at the time of writing): five triples in
`ontology/metadata.ttl` — `dcterms:license`, `dcterms:publisher`, `dcterms:issued`,
`dcterms:source`, `dcterms:bibliographicCitation` — propagated to the model and,
through `build.py`, license and publisher to the six vocabularies. See the
CHANGELOG entry of 2026-09-30.

**How the score is computed.** FOOPS! runs 24 checks; the overall score is the
*mean of each check's passed/total ratio*. So a check is worth **1/24 ≈ 4.17
points**, and a check with sub-tests (e.g. `OM3`, six of them) moves in sixths.
Everything in §3 is priced with that rule.

## 1. How to measure (before and after every step)

```bash
python scripts/fair_check.py                 # the deployed canonical IRI
python scripts/fair_check.py --local         # ontology/triple.ttl, not deployed yet
python scripts/fair_check.py --min 80        # exit 1 below 80 % (release chore)
python scripts/fair_check.py --json out.json # keep the full report
```

The script runs the same FOOPS! release as the public instance (v0.4.0) on the
local JVM: it downloads the jar once into `build/foops/` (git-ignored), starts
the server, assesses, prints the table and stops the server. Needs a JDK ≥ 11.

Before assessing, it checks whether a **non-browser client** can dereference the
ontology IRI and the current versionIRI — FOOPS! is one, and so is every RDF
client. If the edge refuses it, the script says so up front, because the
resolution checks (`URI1`, `CN1`, `DOC1`, `VER2`) will then fail for reasons
that have nothing to do with the ontology (§2.1).

With `--local` two checks fail by construction and are marked as such: `URI2`
(the localhost URL is not the ontology IRI) and `PURL1`. Compare localhost runs
with localhost runs, canonical-IRI runs with canonical-IRI runs.

Do not use the public instance (https://foops.linkeddata.es) until §2.1 is done.

## 2. Preconditions — nothing below counts until these two are done

### 2.1 Let machine clients through the gotriple.eu edge — *ops*

Two independent problems on the same edge, both found while assessing.

**TLS 1.3 only.** TLS 1.2 is refused:

```
$ openssl s_client -connect gotriple.eu:443 -servername gotriple.eu -tls1_2
... alert protocol version ...
```

The public FOOPS! instance's JVM does not negotiate 1.3, hence its 4 %. Fix in
nginx: `ssl_protocols TLSv1.2 TLSv1.3;`.

**Non-browser User-Agents get 502** (the Anubis bot filter in front of the
site). Measured 2026-10-01: `Accept: text/turtle` with a browser UA → `200
text/turtle`; with `curl/…` or `Java/…` → `502`. On 2026-09-30 a Java UA still
got 200, so the filter was tightened in between — and the local FOOPS! score on
the same file dropped from 77.1 % to 62.5 % (`URI1`, `DOC1`, `VER2` fail).

For a Linked Data host this is the bigger defect of the two: the whole point of
`/ontology/` is to be dereferenced by machines, and a 502 tells them the server
is broken rather than that they are being filtered. `/ontology/` (and, later,
the resource resolver) must be **exempt from the bot challenge** — Anubis
supports per-path bypass rules. `kg.gotriple.eu` is not behind the filter.

**Verify both:**

```bash
curl --tls-max 1.2 -s -o /dev/null -w '%{http_code}\n' -A 'Java/21' \
     -H 'Accept: text/turtle' https://gotriple.eu/ontology/triple      # 200
python scripts/fair_check.py                                           # no warning
```

### 2.2 Deploy the current `docs/` — *deploy*

Commit and deploy the pending change so the canonical IRI serves the new header.

**Verify:**

```bash
curl -s -H 'Accept: text/turtle' https://gotriple.eu/ontology/triple | grep -E 'dcterms:(license|publisher|issued|bibliographicCitation|source)'
```

Five lines expected. Then run §1 against the canonical IRI: **expect ≈ 81 %**.

## 3. The remaining checks, ranked by yield per effort

Each subsection says what the check actually tests (read from the FOOPS!
source, `src/main/java/entities/Ontology.java` and `entities/checks/`), the exact
action, who does it, and how to verify.

### 3.1 `OM3` — status · *repo, one triple* · **+0.7**

FOOPS! reads `bibo:status` (`http://purl.org/ontology/bibo/status`) or
`mod:status`. Add to `ontology/metadata.ttl`:

```turtle
@prefix bibo: <http://purl.org/ontology/bibo/> .
    ...
    bibo:status <http://purl.org/ontology/bibo/status/published> ;
```

The merge binds prefixes from a fixed list — `scripts/merge_iterations.py`,
around lines 168–181 (`Namespace(...)` + `merged_graph.bind(...)`). Add
`BIBO = Namespace("http://purl.org/ontology/bibo/")` and `bind("bibo", BIBO)`,
otherwise the model serialises the property as `ns1:status` and the
documentation anchors degrade (URI-CONVENTIONS §5). Then
`merge_iterations.py`, `check_model.py`, `build_docs.sh docs`.

**Verify:** `OM3` goes from `3/6` to `4/6`.

### 3.2 `FIND2` (first half) — prefix.cc · *5 minutes* · **+2.1**

`FIND2` has two sub-tests: the prefix is found on **prefix.cc**, and on **LOV**
(§3.3). For prefix.cc: go to https://prefix.cc/triple — if the prefix is free the
page offers to register it. Namespace must be **exactly**
`https://gotriple.eu/ontology/triple/` (trailing slash), i.e. identical to
`vann:preferredNamespaceUri`, because FOOPS! compares the two.

Caveat: at the time of writing the check says *"Error when retrieving prefix"*,
not *"not found"* — prefix.cc was not answering at all (also unreachable from
here). If it stays red after registration, wait and re-run: it is the registry,
not the entry.

**Verify:** `curl -s https://prefix.cc/triple.file.json` returns the namespace;
`FIND2` goes to `1/2`.

### 3.3 `FIND3`, `FIND_3_BIS`, `FIND2` (second half) — LOV · *submission + review* · **+10.4**

The biggest single item. `FIND3` downloads LOV's full vocabulary list and looks
for our **namespace**; `FIND_3_BIS` checks that the ontology's metadata is
retrievable from the registry (so it survives the ontology going offline); the
second half of `FIND2` looks the prefix up in LOV's API. All three are the same
registration.

Submit at https://lov.linkeddata.es/dataset/lov/suggest with the ontology IRI.
LOV's own acceptance criteria are already met after today's change: a
dereferenceable IRI with content negotiation, `vann:preferredNamespacePrefix`
and `…Uri`, `dcterms:title`/`description`/`creator`, labels on every term, and
a **license** (this was the blocker until today). LOV's crawler must be able to
reach the host: **do §2.1 first** or the submission fails silently on TLS.

Review by LOV curators takes days to weeks.

**Verify:** `curl -s "https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/info?vocab=triple"`
returns JSON (today: 404); `FIND2` `2/2`, `FIND3` and `FIND_3_BIS` green.

### 3.4 `OM3` — DOI · *release process* · **+0.7**

FOOPS! reads `bibo:doi`. Enable the **Zenodo ↔ GitHub integration** on the
repository: every GitHub release then gets a DOI (plus a concept DOI for all
versions). Put it in `metadata.ttl` as `bibo:doi "10.5281/zenodo.NNNNNN"` at the
release chore, next to `owl:versionIRI` (samod skill, release checklist). Worth
more than the 0.7 points: it makes the ontology citable and `bibliographicCitation`
can carry the DOI.

### 3.5 `OM3` — logo · *needs an asset* · **+0.7**

FOOPS! reads `foaf:logo` or `schema:logo`, an IRI to an image. There is no logo
today (`docs/static/LODELogo.png` is pyLODE's, not ours). If one is produced,
put it under `docs/static/`, reference it as
`foaf:logo <https://gotriple.eu/ontology/static/triple-logo.png>`. Last in the
list on purpose: the only step that requires producing something, for less
than a point.

### 3.6 `PURL1` — the last 4.2 points, and a decision, not a task

`PURL1` passes only if the **ontology IRI itself** is on a persistent-identifier
register: w3id, purl, DOI, W3C, perma.cc, linked.data.gov.au, data.europa.eu,
dbpedia.org. `https://gotriple.eu/ontology/triple` is none of these, by the
decision recorded at 3.0.0 (the ontology stays on gotriple.eu; the *resources*
went to `w3id.org/gto/`).

There is no trick around it: submitting a w3id alias that redirects to
gotriple.eu makes `PURL1` pass and `URI2` fail (the `owl:Ontology` IRI would
differ from the URL assessed) — net zero. Passing `PURL1` means **renaming every
term IRI** to a w3id namespace: a breaking change for every consumer, a
crosswalk in the CHANGELOG, a new `versionIRI` line, all the exemplar ABOXes and
SPARQL mirrors. That is not worth 4 points; it would only be worth doing if the
project decides, for its own reasons, that the ontology should live on w3id.

**Ceiling without §3.6: 95.8 %.** That is a better score than OpenCitations'
72.9 % and it is the honest target of this handoff.

## 4. Score ledger

| step | check(s) | cumulative (canonical IRI) |
|---|---|---|
| today, deployed (§2.2) | OM1, OM2, OM4.1, OM4.2, OM5.2 green | **81.2 %** |
| §3.1 status | OM3 4/6 | 81.9 % |
| §3.2 prefix.cc | FIND2 1/2 | 84.0 % |
| §3.3 LOV | FIND2 2/2, FIND3, FIND_3_BIS | 94.4 % |
| §3.4 DOI | OM3 5/6 | 95.1 % |
| §3.5 logo | OM3 6/6 | **95.8 %** |
| §3.6 w3id IRI (not recommended) | PURL1 | 100 % |

## 5. Repository hygiene that belongs to the same work

None of these moves the FOOPS! score; all of them keep it from regressing.

- **`LICENSE` file.** The ontology now declares CC BY 4.0 in its data, but the
  repository has no license file and GitHub detects none. Add
  `LICENSE` (CC BY 4.0 text) at the root so the two agree.
- **Header invariant in `scripts/check_model.py`.** A fifth check — *the
  `owl:Ontology` node carries `dcterms:license`, `publisher`, `issued`,
  `bibliographicCitation`* — so a future edit of `metadata.ttl` cannot silently
  drop them. Same pattern as the existing four.
- **Run `scripts/fair_check.py` at the release chore** and paste the score in
  the CHANGELOG entry; `--min` can gate the release on it.
- **`build.py` shared list.** Vocabularies inherit `dcterms:license` and
  `publisher` (they are in `load_shared_metadata()`), but not `issued`, `source`
  or the citation. Extend the list if the vocabularies are ever assessed on
  their own.
- **`build.py` re-stamps `dcterms:modified`** with today's date on every
  vocabulary at every build, changed or not. Harmless for FOOPS!, misleading for
  everyone else; the date should come from the sidecar.

## 6. What will *not* move the score

Already green, so effort there is wasted: labels and descriptions (`VOC3`/`VOC4`,
30/30 terms), vocabulary reuse (`VOC1`/`VOC2`), versioning (`VER1`/`VER2`:
`owl:versionIRI` resolves), content negotiation and HTML/RDF availability
(`URI1`, `CN1`, `DOC1`, `RDF1`), open protocol (`HTTP1`), ontology ID (`URI2`).
Adding more `rdfs:comment`s, more alignments, or more restrictions changes
nothing here — FOOPS! measures findability, access and metadata, not modelling
quality. For modelling quality use OOPS! (same group) or the SHACL shapes in
`shapes/`.
