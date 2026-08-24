# Documentation outline — chapters 4–13 (working document)

Authoring plan for the remaining narrative chapters of the model page. Consumed as
chapters get written: when a chapter lands in `sections/`, its entry here is done.
Every term of the consolidated model (170 at 3.1.0) is assigned to exactly one
chapter — the chapter that *claims* it in its front-matter `terms:` and lists it in
its Vocabulary section. Cross-references in prose link to the term's definition
wherever it is claimed. Each chapter follows the template fixed by chapter 3:
Preamble → narrative subsections → Vocabulary → Integrity Conditions → Example →
Notes (Integrity Conditions from `shapes/`, the Example from the home iteration's
ABox).

Status: chapters 1–3 written. Chapter 3 needs a small term-list **extension** (see
below). Term counts per chapter add up to 170.

**Figures.** Graffoo diagrams live **in the chapters**, embedded in the prose where
the pattern is narrated (`![caption](figures/slug.svg)`, italic caption line below
the image; hand-drawn in yEd, SVG export). A diagram is nearly always a
constellation of terms, so it belongs to the narrative, not to one entity card —
the per-term `--figures` card mechanism stays available but dormant. Chapter
figures use a descriptive kebab slug (they are not term anchors). Each chapter
below names its planned figure(s); drawing them is human-led (Claude supplies the
facts to draw).

---

## Ch. 1 — Introduction *(written; claims no terms)*

## Ch. 2 — The TRIPLE Data Model *(written; claims no terms)*

- **Figure** `figures/model-overview.svg` — the whole model at a glance: the six
  entity classes and the main relations between them. Embed in the existing
  overview prose once drawn (one-line markdown edit).

## Ch. 3 — Documents *(written; 14 terms — EXTEND to 22)*

Add to the front-matter and to the Vocabulary section, with one short paragraph
each in the existing subsections:

- **§3.2 The Life of a Record**: `schema:dateCreated`, `schema:dateModified`
  (record timestamps, alongside creativeWorkStatus/comment).
- **§3.3 Titles, Abstracts and Languages**: `schema:inLanguage`, `schema:Language`
  (the prose already discusses them — the terms were simply not claimed).
- **§3.1/3.2**: `schema:creator` (super-property of schema:author; hierarchy glue).
- **New subsection "Coverage"** (before the Vocabulary section; renumber what
  follows): `schema:spatialCoverage` + `schema:Place`,
  `schema:temporalCoverage` — what the content is *about* in space and time.
  Document-level description, not dataset-specific.
- **Figure** `figures/document-core.svg` (in §3.1, after the preamble) — Document
  with its descriptive core: headline/abstract, dates, the agent properties, the
  aggregator.

## Ch. 4 — Datasets, Media Objects and Semantic Artefacts *(19 terms)*

- **4.1 Preamble** — the three specialized entities, each presented **as an
  entity in its own right**. The *current* modeling makes them subclasses of
  Document (the chapter-3 core reaches them through inheritance), but the
  design trajectory is toward increasingly autonomous identities that keep a
  set of properties overlapping with Document — the prose must state the
  subclassing as today's state, never read as "a Dataset is just a Document
  with a type".
- **4.2 Datasets** — `triple:Dataset` and its structural superclasses
  (`schema:Dataset`, `dcat:Dataset`); the DCAT distribution pattern
  (`dcat:distribution`, `dcat:Distribution`, `dcat:accessURL`,
  `dcat:downloadURL`); size and format (`schema:size`, `schema:version`,
  `schema:encodingFormat`, `schema:fileFormat`); the spatial bounding box
  (`dcat:bbox` — the DCAT-specific complement of the document-level coverage
  of ch. 3); provider themes (`dcat:theme`, distinct from GoTriple
  classification — forward-ref ch. 8).
- **4.3 Media objects** — `triple:MediaObject`, `schema:MediaObject`,
  `schema:duration` (audio/video).
- **4.4 Semantic artefacts** — `triple:SemanticArtefact`, `mod:SemanticArtefact`,
  `adms:representationTechnique` (ontologies, vocabularies, models as resources).
- **4.5 Vocabulary · 4.6 Integrity Conditions** (shape profiles per entity)
  **· 4.7 Example** (iterations 14/15/17 ABoxes).
- **Figures**: `figures/specialized-documents.svg` (in §4.1 — the three entities
  with their structural superclasses and the Document inheritance as it stands
  today); `figures/dataset-distribution.svg` (in §4.2 — Dataset →
  dcat:distribution → Distribution with accessURL/downloadURL and the
  format/size datatypes).

Terms: triple:Dataset schema:Dataset dcat:Dataset dcat:Distribution
dcat:distribution dcat:accessURL dcat:downloadURL dcat:bbox dcat:theme
schema:size schema:version schema:encodingFormat schema:fileFormat
schema:duration triple:MediaObject schema:MediaObject triple:SemanticArtefact
mod:SemanticArtefact adms:representationTechnique

*(schema:spatialCoverage, schema:Place, schema:temporalCoverage moved to the
ch. 3 extension: coverage is document-level description.)*

## Ch. 5 — Identifiers *(21 terms)*

- **5.1 Preamble** — the design decision: **no identifier subclasses**; the scheme
  *is* the kind. History note: the 3.0.0 retirement of the class-per-kind model.
- **5.2 The identifier pattern** — the reified identifier:
  `datacite:hasIdentifier` → `datacite:Identifier` blank node →
  `datacite:usesIdentifierScheme` (a `datacite:IdentifierScheme` individual) +
  `litre:hasLiteralValue` (the value carrier — and why it is litre:, not the
  nonexistent datacite:hasIdentifierValue).
- **5.3 The sixteen schemes** — nine from DataCite (ark, doi, handle, isbn, isni,
  issn, orcid, researcherid, uri) and seven minted by TRIPLE (internal_id,
  original_id, gotriple_id, idref, landing_page_url, full_text_url, source_url).
  What each identifies and for which entity. The three URL schemes get their
  narrative depth in ch. 12.
- **5.4 Vocabulary · 5.5 Integrity Conditions** (the per-entity mandatory
  identifiers: every Document exactly one internal and one original id, etc. —
  from `shapes/`) **· 5.6 Example**.
- **Figure** `figures/identifier-pattern.svg` (in §5.2) — the reified identifier:
  entity → hasIdentifier → Identifier → usesIdentifierScheme + hasLiteralValue,
  with two contrasting scheme individuals (a doi and internal_id).

Terms: datacite:Identifier datacite:IdentifierScheme datacite:hasIdentifier
datacite:usesIdentifierScheme litre:hasLiteralValue datacite:ark datacite:doi
datacite:handle datacite:isbn datacite:isni datacite:issn datacite:orcid
datacite:researcherid datacite:uri triple:internal_id_schema
triple:original_id_schema triple:gotriple_id_schema triple:idref_schema
triple:landing_page_url_schema triple:full_text_url_schema
triple:source_url_schema

## Ch. 6 — Agents and Profiles *(27 terms)*

- **6.1 Preamble** — two populations, one model: authors extracted from harvested
  metadata and registered GoTriple users; both are `triple:Profile`.
- **6.2 People and organizations** — `foaf:Agent`, `foaf:Person`/`schema:Person`,
  `foaf:Organization`/`schema:Organization`; naming (`foaf:name`,
  `foaf:givenName`, `foaf:familyName`, `schema:name`, `schema:alternateName`);
  `schema:jobTitle`, `triple:pronouns`; `schema:affiliation`.
- **6.3 The profile** — `triple:Profile` and the registered/harvested divide
  (`triple:registeredUser`); self-description (`schema:description`,
  `schema:image`); contact (`schema:email`, `schema:contactPoint`,
  `schema:ContactPoint`, `schema:url` for personal pages); external accounts
  (`foaf:account`, `foaf:OnlineAccount`); `triple:openToCollaboration`.
- **6.4 Expertise and interests** — `schema:knowsAbout` (and why its value is
  constrained per class, not globally), `schema:knowsLanguage`,
  `foaf:topic_interest`.
- **6.5 Vocabulary · 6.6 Integrity Conditions** (profile identifier requirements;
  ORCID/IdRef) **· 6.7 Example**.
- **Figure** `figures/profile.svg` (in §6.3) — Profile between its two natures
  (Person/Organization), with contact, accounts, and the expertise properties.

Terms: foaf:Agent foaf:Person foaf:Organization schema:Person schema:Organization
schema:ContactPoint foaf:OnlineAccount triple:Profile foaf:name foaf:givenName
foaf:familyName schema:name schema:alternateName schema:jobTitle triple:pronouns
triple:registeredUser triple:openToCollaboration schema:description schema:image
schema:email schema:contactPoint schema:url foaf:account schema:knowsAbout
schema:knowsLanguage foaf:topic_interest schema:affiliation

## Ch. 7 — Projects and Funding *(12 terms)*

- **7.1 Preamble** — research projects as first-class resources alongside
  documents.
- **7.2 The project** — `triple:Project` ⊑ `schema:Project`; lifecycle
  (`schema:startDate`, `schema:endDate`); people and bodies
  (`schema:organizer`, `schema:sponsor`); descriptive fields reused from the
  document core (name, description, keywords — cross-refs, not re-claims).
- **7.3 Funding** — the grant chain: `schema:funding` → `schema:Grant` /
  `frapo:Grant` → `schema:funder` → `schema:FundingScheme` (the pending-schema
  status of FundingScheme and why it is admissible as a funder). Why funding
  schemes are individuals with display names and **not** a controlled vocabulary
  (open set; corpus evidence).
- **7.4 Projects and their outputs** — `frapo:isOutputOf` linking documents to
  projects.
- **7.5 Vocabulary · 7.6 Integrity Conditions · 7.7 Example** (iteration 18/19).
- **Figure** `figures/funding-chain.svg` (in §7.3) — Project → funding → Grant →
  funder → FundingScheme, plus Document → isOutputOf → Project.

Terms: triple:Project schema:Project frapo:Grant schema:Grant
schema:FundingScheme schema:funding schema:funder frapo:isOutputOf
schema:organizer schema:sponsor schema:startDate schema:endDate

## Ch. 8 — Classification and Controlled Vocabularies *(19 terms)*

- **8.1 Preamble** — the two-level design: six vocabularies published as sibling
  artefacts (namespace + production key, no lookup tables) and the bridge
  classes inside the model.
- **8.2 The bridge classes** — `triple:Discipline`, `triple:ContentType`,
  `triple:ConditionOfAccess`, `triple:License`, `triple:ProjectType`: each ⊑
  `skos:Concept` plus its DCMI superclass where one exists
  (`dcterms:RightsStatement`, `dcterms:LicenseDocument`).
- **8.3 The linking properties** — `triple:hasContentType`,
  `triple:hasConditionOfAccess`, `triple:hasLicense`, `triple:hasProjectType`,
  `sioc:topic` (the 27-discipline classification), and their DCMI
  super-properties (`dcterms:type`, `dcterms:subject`, `dcterms:accessRights`,
  `dcterms:license`) — the hierarchy that makes generic DC queries work.
- **8.4 The SKOS layer** — `skos:Concept`, `skos:prefLabel`, `skos:definition`;
  concept keys verbatim from production; external matches (COAR, CC, SPDX,
  UNESCO — pointer to ch. 13 for the mapping machinery).
- **8.5 Vocabulary · 8.6 Integrity Conditions** (exactly-one classification
  constraints from shapes) **· 8.7 Example**.
- **Figure** `figures/classification-two-level.svg` (spanning §8.2–8.3) — one
  worked path: Document → hasConditionOfAccess → coa:acr_open-access, with the
  bridge class ⊑ skos:Concept + dcterms:RightsStatement and the property ⊑
  dcterms:accessRights, showing how model and vocabulary artefacts meet.

Terms: triple:Discipline triple:ContentType triple:ConditionOfAccess
triple:License triple:ProjectType triple:hasContentType
triple:hasConditionOfAccess triple:hasLicense triple:hasProjectType sioc:topic
dcterms:type dcterms:subject dcterms:accessRights dcterms:license
dcterms:RightsStatement dcterms:LicenseDocument skos:Concept skos:prefLabel
skos:definition

## Ch. 9 — Original Values *(14 terms)*

- **9.1 Preamble** — the aggregation problem: GoTriple normalizes, but the
  provider's raw value must survive. The naming rule: original + normalized
  field name (originalInLanguage, originalAdditionalType,
  originalConditionOfAccess, originalLicense, originalDatePublished,
  originalSource).
- **9.2 The six original properties** — each one paired with the normalized
  property it shadows, and its Dublin Core Elements super-property
  (`dc:language`, `dc:type`, `dc:rights`, `dc:date`, `dc:source`) — why the
  legacy DC Elements namespace is exactly right for raw, uninterpreted strings.
- **9.3 Provenance** — `dcterms:source` (the harvesting source),
  `dcterms:provenance` + `dcterms:ProvenanceStatement` (custody statements).
- **9.4 Vocabulary · 9.5 Integrity Conditions · 9.6 Example**.
- **Figure** `figures/original-values.svg` (in §9.2) — one Document carrying a
  normalized pair (inLanguage → Language) beside its raw shadow
  (originalInLanguage → literal), with the dc: super-property arrows.

Terms: triple:originalInLanguage triple:originalAdditionalType
triple:originalConditionOfAccess triple:originalLicense
triple:originalDatePublished triple:originalSource dc:language dc:type dc:rights
dc:date dc:source dcterms:source dcterms:provenance dcterms:ProvenanceStatement

## Ch. 10 — Annotations and Enrichment *(16 terms)*

- **10.1 Preamble** — what the GoTriple pipeline adds to a record, and how the
  model keeps it distinguishable from provider data.
- **10.2 The annotation pattern** — Web Annotation as enrichment provenance:
  `oa:Annotation` with `oa:hasTarget` (the resource), `oa:hasBody` (the assigned
  concept/term), `oa:motivatedBy` (an `oa:Motivation`: `oa:classifying` for
  disciplines, `oa:tagging` for keywords, `oa:identifying` for entity linking),
  `dcterms:creator` (the pipeline), `triple:confidence` (the SKG-IF trust
  score).
- **10.3 Detected subjects** — `schema:about` (SSH-LCSH concepts from
  enrichment), `schema:mentions`, and their broad range (`schema:Thing`).
- **10.4 Language services** — `triple:detectedLanguage`,
  `triple:machineTranslatedLanguage` (which title/abstract literals are machine
  output).
- **10.5 Curation flags** — `triple:isDiscarded`.
- **10.6 Vocabulary · 10.7 Integrity Conditions · 10.8 Example**.
- **Figure** `figures/annotation-pattern.svg` (in §10.2) — Annotation with
  hasTarget (a Document), hasBody (a concept), motivatedBy (oa:classifying),
  creator and confidence.

Terms: oa:Annotation oa:Motivation oa:hasBody oa:hasTarget oa:motivatedBy
oa:classifying oa:identifying oa:tagging dcterms:creator triple:confidence
triple:isDiscarded triple:detectedLanguage triple:machineTranslatedLanguage
schema:about schema:mentions schema:Thing

## Ch. 11 — Deduplication *(2 terms)*

- **11.1 Preamble** — one record per provider (ch. 3's scope note), so the same
  work appears many times; the design history: why the Cluster entity was
  retired in favor of a direct link (iteration 20, "strada C").
- **11.2 The duplicate link** — `triple:isDuplicateOf` (semantics, direction,
  what a consumer must do to collapse a result list), `prov:alternateOf` as its
  external alignment (reflexive/symmetric/transitive caveats).
- **11.3 Vocabulary · 11.4 Integrity Conditions** (dedup shape) **· 11.5
  Example** (iteration 20).
- **Figure** `figures/deduplication-link.svg` (in §11.2) — three provider records
  of the same work collapsed by isDuplicateOf links (direction shown).

Terms: triple:isDuplicateOf prov:alternateOf

*Shortest chapter; if it reads too thin next to the others it can merge into
ch. 12 as "Deduplication, Links and URLs" — decide at writing time.*

## Ch. 12 — Links and URLs *(6 terms)*

- **12.1 Preamble** — URLs play three roles in GoTriple: identifiers (the three
  URL schemes of ch. 5), links between resources, and external identity
  references. The URL-as-identifier decision (reified with a scheme, not a plain
  property).
- **12.2 The three URL schemes in practice** — landing page, full text, source
  URL: which entity carries which, mandatory-ness (prose over the ch. 5
  definitions).
- **12.3 Links between works** — `dcterms:references` / `dcterms:isReferencedBy`
  (citations), `schema:isBasedOn` (derivation).
- **12.4 External identity** — `schema:sameAs` (Wikidata & co.),
  `schema:mainEntityOfPage`; the `schema:URL` datatype class.
- **12.5 Vocabulary · 12.6 Integrity Conditions** (URL shape) **· 12.7 Example**.
- **Figure**: none planned (the three-roles distinction is a table in prose; a
  diagram is optional if §12.2 turns out to need one).

Terms: dcterms:references dcterms:isReferencedBy schema:isBasedOn schema:sameAs
schema:mainEntityOfPage schema:URL

## Ch. 13 — External Alignments *(12 terms)*

- **13.1 Preamble** — the reuse policy: no owl:imports; materialized declarations
  of every borrowed term with contextual comments at the term's home (the OCO
  style); `prefix:LocalName` labels; the one-home-per-term rule.
- **13.2 The mapping properties** — `skos:exactMatch` vs `skos:closeMatch` (when
  each is asserted, for model terms and for vocabulary concepts), and why
  owl:equivalentClass is used sparingly.
- **13.3 The alignment classes** — the pure-alignment superclasses/equivalents,
  ontology by ontology: FOAF (`foaf:Document`), CIDOC CRM (`crm:E31_Document`,
  `crm:E7_Activity`, `crm:E90_Symbolic_Object` — note open investigation, issue
  #37), FaBiO (`fabio:Work`, `fabio:ScholarlyWork`, `fabio:Dataset`), SSHOC
  (`sshoc:SHE1_Dataset`, `sshoc:SHE3_SSH_Project`, `sshoc:SHE8_Publication`).
- **13.4 Vocabulary · 13.5 Notes** (no integrity conditions or example: alignment
  asserts no data constraints).
- **Figure**: none (alignments read better as the per-ontology narrative + the
  term links; no constellation to draw).

Terms: skos:exactMatch skos:closeMatch foaf:Document crm:E31_Document
crm:E7_Activity crm:E90_Symbolic_Object fabio:Work fabio:ScholarlyWork
fabio:Dataset sshoc:SHE1_Dataset sshoc:SHE3_SSH_Project sshoc:SHE8_Publication

---

**Count check**: 22 (ch. 3 extended) + 19 + 21 + 27 + 12 + 19 + 14 + 16 + 2 + 6 +
12 = **170** — every term of the 3.1.0 model claimed exactly once.

**Standing design note (applies to every chapter, ch. 4 above all).** Dataset,
MediaObject and SemanticArtefact are Document subclasses *today*; the design
trajectory is toward entities with their own identity, keeping a property set
that overlaps with Document. Write the prose so that the entity's identity leads
and the inheritance is stated as the current mechanics — never as its essence.
