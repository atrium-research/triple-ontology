# SAMOD iteration — file templates

Paste these into a fresh `development/NN/` directory and fill in. Placeholders in `[square brackets]`.

---

## `motivating-scenario.md`

```markdown
# Motivating Scenario - Iteration [NN]

## Name
[Brief descriptive name of the iteration focus]

## General Description
[Domain problem or requirement. Context, stakeholders, why this iteration
is needed for the GoTriple platform.]

## Technical Specification
- [Ontology design decisions]
- [Mapping requirements to external standards (Schema.org, FOAF, SKOS, …)]
- [Compatibility requirements with existing iterations]

## Examples
- Example 1: [Concrete real-world instance — will become ABox]
- Example 2: [Concrete real-world instance — will become ABox]
```

Guidelines:
- Examples must be concrete enough to translate *directly* into ABox individuals. "User wants to search" is too vague; "Document D1 published by organization O1 in 2022 with DOI 10.x/y" is right.
- Keep Name ≤ 8 words.

---

## `informal-competency-questions.md`

```markdown
## Informal Competency Questions (Iteration [NN])

## Question 1

### Identifier
CQ_[NN].1

### Question
[Natural-language question — what must the ontology be able to answer?]

### Expected Outcome
[Type and format of expected result: "a list of URIs", "one string", …]

### Result
* `example_entity_1` → [value]
* `example_entity_2` → [value]

### Based on
Example [k]
```

Guidelines:
- One `## Question N` block per CQ.
- Expected results must reference the *actual* ABox individuals you will create.
- Mark dependencies: if CQ_NN.3 reuses data from CQ_NN.1, say so in *Based on*.

---

## `glossary-of-terms.md`

```markdown
# Glossary of Terms (Iteration [NN])

| Term                           | Definition                                                                                                |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| `namespace:ClassName`          | Short technical definition. Reference the source ontology.                                                |
| `namespace:propertyName`       | Short technical definition. Reference the source ontology.                                                |
| `triple:LocalClass`            | Project-defined class — full definition.                                                                  |
| `triple:localProperty`         | Project-defined property — full definition.                                                               |
| `Domain Term`                  | Domain-specific term with no namespace (used only if it later becomes part of the TBox).                  |
```

**Hard rule — TBox only.** Every row must be a name that appears in `TBOX.ttl`. Do not list ABox individuals. Do not list `pt:network` or `ct:typ_article` and so on unless the concept scheme itself is introduced in this iteration's TBox.

---

## `TBOX.ttl`

```turtle
@prefix :         <https://gotriple.eu/ontology/triple/> .
@prefix triple:   <https://gotriple.eu/ontology/triple/> .
@prefix owl:      <http://www.w3.org/2002/07/owl#> .
@prefix rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:     <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:      <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:     <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms:  <http://purl.org/dc/terms/> .
@prefix schema:   <https://schema.org/> .
@prefix foaf:     <http://xmlns.com/foaf/0.1/> .
@prefix datacite: <http://purl.org/spar/datacite/> .
@prefix litre:    <http://www.essepuntato.it/2010/06/literalreification/> .

# ---- Classes --------------------------------------------------------

triple:MyClass a owl:Class ;
    rdfs:label "My Class"@en ;
    rdfs:comment "Definition of MyClass in the TRIPLE ontology."@en ;
    rdfs:subClassOf [ external class if any ] ;
    skos:exactMatch <http://external.example/MyClass> .

# ---- External references (label in prefix:LocalName form) -----------

schema:CreativeWork a owl:Class ;
    rdfs:label "schema:CreativeWork"@en .

foaf:Person a owl:Class ;
    rdfs:label "foaf:Person"@en .

# ---- Properties -----------------------------------------------------

triple:myRelation a owl:ObjectProperty ;
    rdfs:label "my relation"@en ;
    rdfs:domain triple:MyClass ;
    rdfs:range schema:CreativeWork ;
    rdfs:subPropertyOf [ external property if any ] .
```

Rules:
- Every TBox entity: `rdfs:label` + `rdfs:comment` (English minimum).
- External classes/properties referenced in the modelet must be declared with label `prefix:LocalName`.
- Prefer reusing existing patterns from `patterns/*.ttl` before inventing new shapes.

---

## `ABOX.ttl`

```turtle
@prefix triple:   <https://gotriple.eu/ontology/triple/> .
@prefix rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:     <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:      <http://www.w3.org/2001/XMLSchema#> .
@prefix schema:   <https://schema.org/> .
@prefix foaf:     <http://xmlns.com/foaf/0.1/> .
@prefix datacite: <http://purl.org/spar/datacite/> .
@prefix litre:    <http://www.essepuntato.it/2010/06/literalreification/> .

# ---- Example 1 ------------------------------------------------------

triple:example_1 a triple:MyClass ;
    rdfs:label "Example 1"@en ;
    triple:myRelation triple:referenced_work_1 ;
    datacite:hasIdentifier [
        a datacite:Identifier ;
        datacite:usesIdentifierScheme triple:internal_id_schema ;
        litre:hasLiteralValue "example_1" ] ,
      [ a datacite:Identifier ;
        datacite:usesIdentifierScheme datacite:ark ;
        litre:hasLiteralValue "ark:/12345/example-1" ] ,
      [ a datacite:Identifier ;
        datacite:usesIdentifierScheme triple:original_id_schema ;
        litre:hasLiteralValue "source-system-0001" ] .

triple:referenced_work_1 a schema:CreativeWork ;
    schema:name "Referenced Work 1"@en .
```

Rules:
- One named individual per MS Example.
- Every individual typed (`a <Class>`).
- Identifiers are plain `datacite:Identifier` nodes: never an identifier subclass, always exactly one `datacite:usesIdentifierScheme` and one `litre:hasLiteralValue`.
- Content entities (Document, Dataset, MediaObject, SemanticArtefact, Project) need all three mandatory identifiers — internal id, ARK PID, source id — or `scripts/validate.py` fails.
- Declare in the TBOX every scheme individual the ABOX uses.
- Properties with class ranges (`schema:publisher`, `schema:spatialCoverage`, `schema:keywords`, `schema:inLanguage`, …) take instance URIs, never bare literals.

---

## `formal-competency-questions.md`

````markdown
## Formal Competency Questions (Iteration [NN])

## CQ_[NN].1

[Natural-language restatement of the CQ.]

```sparql
PREFIX triple:   <https://gotriple.eu/ontology/triple/>
PREFIX schema:   <https://schema.org/>
PREFIX rdfs:     <http://www.w3.org/2000/01/rdf-schema#>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre:    <http://www.essepuntato.it/2010/06/literalreification/>

SELECT ?x ?y WHERE {
  ?x a triple:MyClass ;
     triple:myRelation ?y .
}
```

**Expected result:**
- `triple:example_1` → `triple:referenced_work_1`
````

Rules:
- One section per CQ.
- Include *all* needed `PREFIX` declarations in every query (queries are run in isolation).
- Expected result rows mirror the ABox.

---

## `modelet.graphml` / `modelet.png`

Author in yEd with Graffoo stencils. Export PNG at the end.

If you reverse-engineer a diagram from a stable TBox instead:

```bash
source scripts/venv/bin/activate
python scripts/ttl_to_graphml_classes.py \
    --input  development/NN/TBOX.ttl \
    --output development/NN/modelet.graphml
```

Then open in yEd, apply layout, export PNG.
