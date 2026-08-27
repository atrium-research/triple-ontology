# Local patches to this pyLODE fork

Vendored into the triple-ontology repository on 2026-08-12 as `tools/pylode/` — from
this point on the tool is versioned with the ontology it builds. The log below records
every deviation from the original fork, oldest first.

## 2026-07-28 — Show qualified restrictions and term-level guidance

Motivation: the TRIPLE ontology declares its identifier requirements as qualified
cardinality restrictions (`hasIdentifier exactly 1 triple:ID`). The generated pages
rendered them as a bare `exactly 1`, dropping the class entirely, so four different
requirements on `triple:Document` looked identical and the identifier model was
invisible in the published documentation.

### 1. `pylode/parser.py` — `_parse_restriction`

`owl:onClass` and `owl:onDataRange` were never read. They are now attached to the
`values` of min/max/exact cardinality restrictions, which the template already renders
as links. `hasIdentifier op exactly 1` becomes `hasIdentifier op exactly 1 Internal ID`.

`owl:hasValue` pointing at an IRI was rendered as a quoted string
(`op value "http://purl.org/spar/datacite/ark"`). An IRI target is a term of the
ontology, so it is now emitted as a link with the right type badge, via the new helper
`_node_short_type`.

### 2. `pylode/parser.py` — `_collect_skos`

New helper replacing the inline SKOS loop that existed only in `_create_class`.
It splits the SKOS annotations into three destinations:

- `skos:example` → `element.examples` (own section, rendered verbatim in `<pre>`)
- `skos:scopeNote`, `skos:note` → `element.scope_notes` (own "Usage" section)
- everything else → `element.skos_properties` ("External Alignment", as before)

It is now called for **classes, properties and named individuals**; previously no SKOS
annotation on a property or an individual was collected at all.

For individuals it is called with `alignment=False`, because they already list their
non-SKOS-core annotations under "has assertions" — otherwise `skos:exactMatch` would
appear twice on every vocabulary concept. The three guidance predicates are excluded
from that assertions list (`exclude_props`) for the same reason.

### 3. `pylode/model.py`

`examples`, `scope_notes` and `skos_properties` moved onto `Element`, so classes,
properties and individuals all carry them. `skos_properties` was removed from `Class`,
where it now comes from the base class.

### 4. `pylode/templates/`

`base.html` (classes) and `property_entity.html` (properties **and** individuals, which
share this template) gained a "Usage" box and an "Example" box before the existing
"External Alignment" box. `static/extra.css` gained `.usage-box` and `.example-box`,
the latter with `white-space: pre-wrap` so snippets keep their line breaks.

### Verification

Regenerated all 11 TRIPLE modules. The 6 entity modules now show the identifier
requirements with their class. The 5 vocabulary modules (individual-heavy) show
**zero non-whitespace differences**, i.e. no regression. Dangling-anchor count
unchanged (only external datatypes such as `xsd:date`, pre-existing behaviour).

A backup of the pre-patch `pylode/` package was taken before editing.

## 2026-08-10 — Short, derivable anchors

Motivation: term documentation was addressed as `page#<full-IRI>` (e.g.
`…/Document#https://gotriple.eu/ontology/triple/hasContentType`) — unguessable, and the
inner `#` of external terms forced the `%23` percent-encoding post-processing step.
TRIPLE now derives the anchor from the IRI alone: a term of the documented ontology gets
its bare local name (`originalLicense`, `musiq`), a borrowed term its prefixed name
(`foaf:Document`). Verified collision-free on all TRIPLE pages.

### 1. `pylode/model.py`
`Element.anchor` — the short HTML id, alongside the existing `url`.

### 2. `pylode/parser.py`
- `_local_namespace()`: reads `vann:preferredNamespaceUri` off the ontology node; this
  is what decides "own term" vs "borrowed term". Ontologies without it keep prefixed
  or full-IRI anchors.
- `_anchor(uri)`: local name if the IRI starts with the local namespace (last path/hash
  segment), else `prefix:name` via the namespace manager (auto-generated `nsN` prefixes
  excluded), else the full IRI as before.
- `_resolve_url` now emits `#<anchor>`; the four Element/Class/Property/Individual
  constructors and the inline restriction-target elements all carry `anchor`.

### 3. `pylode/templates/`
`id="{{ x.anchor or x.uri }}"` on the two entity divs; all 12 internal
`href="#{{ x.uri }}"` sites switched to `anchor or uri` (regex pass).

### Consequences for the TRIPLE pipeline
The `%23` post-processing step (issue #32 convention) is retired: no anchor contains
`#` any more. Dangling short anchors to undeclared externals (`xsd:date`,
`skos:Concept`) replace the previous dangling full-IRI anchors — same pre-existing
class of issue, unchanged count.

Addendum (same day): the ontology / concept-scheme node itself — IRI equal to the local
namespace minus the trailing slash, e.g. `…/ontology/ddc` with namespace `…/ontology/ddc/`
— fell through to the full-IRI fallback. It now anchors under its own last segment
(`#ddc`). Found by the anchor-coverage review.

## 2026-08-11 — Narrative chapters (SKOS-Reference-style sections)

Motivation: the TRIPLE model page is a flat term dump; the target structure is the
SKOS Reference — numbered thematic chapters with prose, each owning its terms, with
integrity conditions and examples after the definitions.

### 1. `pylode/sections.py` (new)

Parses a directory of numbered markdown files (`01-introduction.md`) with a minimal
front-matter (`title`, `terms`). `terms` lists page ANCHORS (bare local name for own
terms, `prefix:LocalName` for borrowed ones). Prose is rendered with python-markdown
(`tables`, `fenced_code`). An optional `<!-- definitions -->` marker splits the prose:
what follows it renders AFTER the term definitions (integrity conditions, examples).

### 2. `pylode/cli.py`

New `--sections DIR` option. Terms claimed by a chapter are removed from the trailing
standard listings; unknown or doubly-assigned terms produce a WARNING; the count of
still-unassigned terms is echoed (goal state: 0, everything owned by a chapter).

### 3. `pylode/templates/`

The class entity markup moved from `base.html` into `class_entity.html` (include),
so chapters can render mixed entities (classes via `class_entity.html`, properties
and individuals via `property_entity.html`). Chapters render before the standard
sections, numbered 1..N; the standard sections continue the numbering and are now
skipped when empty. The automatic "Introduction" (dc:description) is suppressed when
chapters are present. Anchors are untouched: a term keeps its id wherever it renders.

`static/extra.css` gained `.narrative-section .prose` rules (tables, code blocks).

### Addendum (stesso giorno) — ToC W3C-TR e rifiniture

- `sections.py`: ogni `<h3>` della prosa riceve un id derivato (`sec-{capitolo}-{slug}`)
  e la lista dei sottotitoli è esposta al template (`subs_before` / `subs_after`).
- `base.html`: il ToC è annidato (capitolo → sottosezioni); l'heading "Vocabulary" non è
  più emesso dal template — lo scrive la prosa del capitolo, che ne controlla la
  numerazione, e l'elenco termini si aggancia sotto l'ultimo heading pre-marker.
- `static/extra.css`: container a tutta larghezza (override dei width fissi di yeti),
  ritmo dei titoli stile SKOS Reference (h2 3em, h3 di prosa 2.2em senza filo navy,
  h3 delle entità invariato), ToC senza bullet con gerarchia indentata,
  `.description ul` con `padding-left: 2em` (i marker non toccano più il bordo del box).
- Appendice **Term Index** (`cli.py` + `base.html`): quando i capitoli sono attivi, prima
  dei Namespaces la pagina chiude con l'indice alfabetico completo di TUTTI i termini
  (soli link, per genere), qualunque capitolo li definisca. Le sezioni standard di coda
  restano il contenitore dei termini non ancora assegnati e spariscono da sole quando
  si svuotano.

### Correzione di rotta (stesso giorno) — capitoli come overlay puro

La semantica precedente (i capitoli "reclamano" i termini e li rendono al proprio
interno) è sostituita su richiesta: i capitoli narrativi sono SOLO documentazione —
prosa più l'elenco "Vocabulary" del capitolo, i cui link saltano alle definizioni.
TUTTE le entità restano nelle sezioni standard di coda (Classes, Object Properties,
Datatype Properties, Annotation Properties, Named Individuals), complete come nel
LODE classico: sono loro il riferimento e l'indice. L'appendice "Term Index" è stata
rimossa perché ridondante. La CLI ora riporta la copertura (quanti termini sono
citati da almeno un capitolo) come metrica informativa, senza filtrare nulla.
- Backlink entità → capitolo (`model.py` Element.chapter, `cli.py`, entrambi i template):
  ogni termine citato da un capitolo mostra "Discussed in §N. Title" sotto l'IRI, così
  la scheda di riferimento rimanda alla narrativa. Figure per termine via `--figures DIR`
  (`{ancora}.png`, ":" → "-"), rese contenute (960×615) e cliccabili per la vista piena.

## 2026-08-24 — External Alignment: link dereferenziabili e spaziatura

Il box "External Alignment" rendeva il valore (`skos:exactMatch`/`closeMatch`)
come testo puro. Nei due template entità il valore che inizia per `http` diventa
`<a href target="_blank" rel="noopener">` — il riferimento esterno si apre in
un'altra tab per essere analizzato. In `static/extra.css`: `word-break` per gli
IRI lunghi, e i tre box guida (`.skos-box`, `.usage-box`, `.example-box`)
passano da `padding: 15px` a `18px 28px` — il contenuto si scosta dalle pareti
del box (correzione su feedback: il punto era la distanza dai bordi, non lo
spacing tra le coppie dt/dd).

## 2026-08-24 — Label multilingue come chip

Le label non-inglesi erano una lista puntata "Alternative Labels:" con la lingua
appesa al testo (`Projet @fr`) — cinque righe per tre parole, moltiplicate sui
concetti dei vocabolari (sei lingue ciascuno). Ora: una sola riga sotto l'IRI,
badge col codice lingua (`.lang-tag`, chip bordato navy su #F4FFFF) + label,
separatore `·`, lingue in ordine alfabetico stabile.

- `parser.py` `_extract_preferred_and_others`: le "altre" label diventano coppie
  `(lang, value)` ordinate per codice lingua; `_get_comment_with_translations`
  (stesso helper) riformatta i commenti tradotti come prima.
- `class_entity.html` + `property_entity.html`: blocco "Alternative Labels"
  sostituito dalla riga `p.labels` subito sotto l'IRI.
- `static/extra.css`: `.lang-tag`, `.label-item` (nowrap), `p.labels`.

## 2026-08-24 — Figure nei capitoli

Decisione: i diagrammi Graffoo vivono nella prosa dei capitoli (un diagramma è quasi
sempre una costellazione di termini, non un termine solo), embedded con la sintassi
markdown standard `![caption](figures/slug.svg)` — nessuna modifica di codice, solo
`static/extra.css`: `.narrative-section .prose img` con la stessa resa del figure-box
delle schede (centrata, max 960×615, bordo). Il meccanismo per-termine `--figures`
resta disponibile ma dormiente.
