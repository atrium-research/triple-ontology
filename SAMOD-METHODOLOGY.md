# SAMOD Methodology

## Simplified Agile Methodology for Ontology Development

SAMOD (Simplified Agile Methodology for Ontology Development) is an iterative, test-driven approach for developing ontologies that emphasizes incremental development, continuous validation, and thorough documentation.

## Core Principles

- **Iterative Development**: Build the ontology incrementally through repeated cycles
- **Test-Driven Approach**: Define competency questions before modeling
- **Data-Centric**: Validate against real-world instance data
- **Human-Centered**: Prioritize understandability and documentation
- **Agile & Flexible**: Adapt to changing requirements while maintaining integrity

## The Three-Phase Cycle

Each SAMOD iteration consists of three phases that produce a complete, tested modelet:

### Phase 1: Define a New Test Case

**Objective**: Identify and document a specific use case to be addressed by the ontology.

**Artifacts Created**:

1. **Motivating Scenario** (`motivating-scenario.md`)
   - Natural language description of the real-world use case
   - Context and background for the requirements
   - Stakeholder needs and goals

2. **Informal Competency Questions** (`informal-competency-questions.md`)
   - Natural language questions the ontology must answer
   - Capture functional requirements
   - Examples: "What documents are authored by a specific person?" or "Which projects were funded by a given organization?"

3. **Glossary of Terms** (`glossary-of-terms.md`)
   - Domain-specific terminology definitions
   - Clarify meaning of key concepts
   - Establish shared vocabulary

4. **Modelet Design** (`modelet.graphml`, `modelet.png`)
   - Small ontology fragment (max 7-9 entities)
   - Visual diagram using Graffoo notation
   - Design principles:
     - **Keep it small**: Focus on specific use case
     - **Middle-out approach**: Neither purely top-down nor bottom-up
     - **Reuse patterns**: Leverage existing design patterns
     - **Self-explanatory names**: Use clear, descriptive entity names

### Phase 2: Merge Current Model with Modelet

**Objective**: Integrate the new modelet into the existing ontology model.

**Activities**:

1. **Combine Models**
   - Merge new modelet with current ontology
   - Identify overlapping concepts

2. **Semantic Collapse**
   - Consolidate semantically identical entities
   - Ensure consistency across iterations

3. **Update Test Cases**
   - Revise existing test cases to work with merged model
   - Add new test cases for modelet functionality

4. **Formal Testing**
   - Run SPARQL queries against the integrated model
   - Verify competency questions are answered correctly

**Artifacts Created/Updated**:

- **TBOX.ttl**: Terminological Box (classes, properties, restrictions)
- **ABOX.ttl**: Assertional Box (instance data for testing)
- **Formal Competency Questions** (`formal-competency-questions.md`): SPARQL queries

### Phase 3: Refactor Current Model

**Objective**: Improve model quality, documentation, and maintainability.

**Activities**:

1. **Documentation Enhancement**
   - Add `rdfs:label` annotations
   - Add `rdfs:comment` descriptions
   - Document design decisions

2. **Knowledge Reuse**
   - Identify opportunities to reuse existing ontologies
   - Map to external standards (FOAF, Dublin Core, Schema.org, etc.)
   - Establish alignments with related vocabularies

3. **Technology Optimization**
   - Leverage reasoner capabilities
   - Use appropriate OWL constructs
   - Optimize for query performance

4. **Comprehensive Testing**
   - Run all formal competency questions
   - Validate model integrity
   - Check for inconsistencies or errors

**Artifacts Updated**:

- Refined TBOX.ttl and ABOX.ttl
- Updated diagrams
- Enhanced documentation

## Working with SAMOD in This Repository

### Repository Structure

```
development/
├── 01/  # Iteration 1
│   ├── motivating-scenario.md
│   ├── informal-competency-questions.md
│   ├── glossary-of-terms.md
│   ├── formal-competency-questions.md
│   ├── TBOX.ttl
│   ├── ABOX.ttl
│   ├── modelet.graphml
│   └── modelet.png
├── 02/  # Iteration 2
│   └── ...
└── 07/  # Iteration 7

diagrams/     # Refactored diagrams (cumulative view after each iteration)
sparql/       # Refactored SPARQL queries for final ontology
```

### How to Navigate an Iteration

1. **Understand the Context**: Read `motivating-scenario.md`
2. **Review Requirements**: Check `informal-competency-questions.md`
3. **Learn the Terminology**: Study `glossary-of-terms.md`
4. **Examine the Model**: View `modelet.png` and `TBOX.ttl`
5. **See Examples**: Review `ABOX.ttl` instance data
6. **Validate**: Run SPARQL queries from `formal-competency-questions.md`

### Adding a New Iteration

To extend the ontology with a new iteration:

1. Create a new numbered directory (e.g., `development/08/`)
2. **Phase 1: Define Test Case**
   - Write `motivating-scenario.md`
   - Create `informal-competency-questions.md`
   - Define terms in `glossary-of-terms.md`
   - Design visual model in `modelet.graphml` (using yEd Graph Editor)
   - Export diagram to `modelet.png`

3. **Phase 2: Merge**
   - Create `TBOX.ttl` with classes, properties, and restrictions
   - Create `ABOX.ttl` with test instances
   - Write `formal-competency-questions.md` with SPARQL queries
   - Validate queries return expected results

4. **Phase 3: Refactor**
   - Add documentation to TBOX
   - Align with external ontologies
   - Update consolidated diagrams in `diagrams/`
   - Update refactored SPARQL in `sparql/`

### Best Practices

- **Small Increments**: Keep each iteration focused on a specific use case
- **Test Continuously**: Always validate with SPARQL queries
- **Document Thoroughly**: Explain design decisions and terminology
- **Reuse Extensively**: Leverage existing ontologies and patterns
- **Visual Communication**: Maintain clear, readable Graffoo diagrams
- **Version Control**: Track changes to understand ontology evolution

## Key Artifacts Reference

| Artifact | Purpose | Format |
|----------|---------|--------|
| Motivating Scenario | Describe use case context | Markdown |
| Informal Competency Questions | Natural language requirements | Markdown |
| Glossary of Terms | Define domain terminology | Markdown |
| Modelet Diagram | Visual representation | GraphML + PNG |
| TBOX | Classes, properties, restrictions | RDF/Turtle |
| ABOX | Test instance data | RDF/Turtle |
| Formal Competency Questions | SPARQL test queries | Markdown + SPARQL |

## Tools Used

- **yEd Graph Editor**: For creating and editing Graffoo diagrams (.graphml files)
- **Protégé**: For ontology editing and reasoning
- **SPARQL Endpoint**: For testing formal competency questions
- **RDF/Turtle Editors**: For manual editing of TBOX and ABOX files

## References

- SAMOD Official Documentation: https://essepuntato.it/samod/
- Graffoo Notation: Visual notation for OWL ontologies
- OWL 2 Web Ontology Language: W3C standard for ontology representation
