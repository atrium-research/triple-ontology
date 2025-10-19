# TRIPLE Ontology Refactoring Plan

**Date:** 2025-10-19
**Version:** 1.0
**Status:** Planning Phase

---

## Executive Summary

This document outlines a comprehensive refactoring plan for the TRIPLE ontology to improve query performance, reduce complexity, and enhance interoperability with Schema.org. The plan focuses on two major architectural changes:

1. **Simplifying role-based relationships** by replacing SPAR PRO complex patterns with direct Schema.org properties
2. **Implementing OWL 2 punning** for document types to enable zero-hop queries while maintaining SKOS alignments

**Expected Impact:**
- **Query complexity reduction:** 50-75% fewer triple patterns
- **Maintenance improvement:** Simpler model, standard vocabularies
- **Interoperability:** Better Schema.org alignment for LOD integration

---

## Table of Contents

1. [Development Tasks](#development-tasks)
2. [Task 1: Role Pattern Simplification](#task-1-role-pattern-simplification)
3. [Task 2: Document Type Punning](#task-2-document-type-punning)
4. [Implementation Strategy](#implementation-strategy)
5. [Migration Path](#migration-path)
6. [Testing Plan](#testing-plan)
7. [Risks and Mitigations](#risks-and-mitigations)

---

## Development Tasks

### Overview

| Task | Priority | Complexity | Impact | Estimated Effort |
|------|----------|------------|--------|------------------|
| **Task 1: Role Pattern Simplification** | HIGH | Medium | Very High | 3-5 days |
| **Task 2: Document Type Punning** | HIGH | Low | High | 1-2 days |

---

## Task 1: Role Pattern Simplification

### Problem Statement

**Current Implementation:** SPAR PRO pattern with `RoleInTime` intermediaries

```turtle
# Current pattern (4-8 triple patterns per query)
?document pro:isDocumentContextFor ?roleInTime .
?roleInTime pro:withRole pro:author .
?roleInTime pro:isHeldBy ?person .
?person foaf:name ?name .
OPTIONAL {
  ?roleInTime tvc:atTime ?timeInterval .
  ?timeInterval ti:hasIntervalStartDate ?startDate .
  ?timeInterval ti:hasIntervalEndDate ?endDate .
}
```

**Query Complexity:** 4 mandatory + 4 optional = **8 triple patterns**

**Issues:**
- ❌ Overly complex for simple author/contributor queries
- ❌ Poor performance on large datasets
- ❌ Difficult to understand for non-experts
- ❌ Limited Schema.org alignment

---

### Current Roles in TRIPLE Ontology

Analysis of `/releases/2025-10-14/serializations/triple.ttl` identified the following roles:

#### SPAR PRO Roles (Standard)

| Role | Current URI | Type | Location |
|------|-------------|------|----------|
| **Author** | `pro:author` | `pro:Role`, `owl:NamedIndividual` | Lines 15-16 |
| **Publisher** | `pro:publisher` | `pro:Role`, `owl:NamedIndividual` | Lines 21-22 |
| **Producer** | `pro:producer` | `pro:Role`, `owl:NamedIndividual` | Lines 18-19 |

#### Custom TRIPLE Roles

| Role | Current URI | Type | Location | Label |
|------|-------------|------|----------|-------|
| **Contributor** | `triple:contributor` | `pro:Role`, `owl:NamedIndividual` | Lines 53-54 | - |
| **Funder** | `triple:funder` | `pro:Role`, `owl:NamedIndividual` | Lines 64-65 | - |
| **Provider** | `triple:provider` | `pro:Role`, `owl:NamedIndividual` | Lines 74-75 | - |
| **Aggregator** | `triple:aggregator` | `pro:Role`, `owl:NamedIndividual` | Lines 50-51 | - |
| **Primary Producer** | `triple:primaryProducer` | `pro:Role`, `owl:NamedIndividual` | Lines 70-72 | "primary producer" |

**Total Roles:** 8 (3 standard PRO + 5 custom TRIPLE)

---

### Schema.org Mapping

#### Direct Mappings (Schema.org v29.3)

| TRIPLE Role | Schema.org Property | Domain | Range | Status |
|-------------|---------------------|--------|-------|--------|
| `pro:author` | `schema:author` | `CreativeWork` | `Person`, `Organization` | ✅ **Direct match** |
| `triple:contributor` | `schema:contributor` | `CreativeWork` | `Person`, `Organization` | ✅ **Direct match** |
| `pro:publisher` | `schema:publisher` | `CreativeWork` | `Person`, `Organization` | ✅ **Direct match** |
| `pro:producer` | `schema:producer` | `CreativeWork` | `Person`, `Organization` | ✅ **Direct match** |
| `triple:funder` | `schema:funder` | Various | `Person`, `Organization` | ✅ **Direct match** |
| `triple:provider` | `schema:provider` | Various | `Person`, `Organization` | ✅ **Direct match** |

#### No Direct Schema.org Match

| TRIPLE Role | Recommended Alternative | Reasoning |
|-------------|------------------------|-----------|
| `triple:aggregator` | `schema:contributor` with role qualifier | No direct Schema.org equivalent; use contributor with note |
| `triple:primaryProducer` | `schema:producer` | Primary producer is a specialization of producer |

---

### Proposed Solution

**Replace PRO pattern with direct Schema.org properties**

```turtle
# Proposed pattern (1-2 triple patterns)
?document schema:author ?person .
?person schema:name ?name .
```

**Query Complexity:** **2 triple patterns** (75% reduction!)

---

### Implementation Details

#### 1. Property Definitions

**Add to ontology core:**

```turtle
# Object Properties for Roles
schema:author a owl:ObjectProperty ;
    rdfs:label "author"@en ;
    rdfs:comment "The author of this content"@en ;
    rdfs:domain foaf:Document ;
    rdfs:range [ owl:unionOf (foaf:Person foaf:Organization) ] ;
    rdfs:subPropertyOf schema:creator .

schema:contributor a owl:ObjectProperty ;
    rdfs:label "contributor"@en ;
    rdfs:comment "A secondary contributor to the CreativeWork"@en ;
    rdfs:domain foaf:Document ;
    rdfs:range [ owl:unionOf (foaf:Person foaf:Organization) ] .

schema:publisher a owl:ObjectProperty ;
    rdfs:label "publisher"@en ;
    rdfs:comment "The publisher of the creative work"@en ;
    rdfs:domain foaf:Document ;
    rdfs:range [ owl:unionOf (foaf:Person foaf:Organization) ] .

schema:producer a owl:ObjectProperty ;
    rdfs:label "producer"@en ;
    rdfs:comment "The person or organization who produced the work"@en ;
    rdfs:domain foaf:Document ;
    rdfs:range [ owl:unionOf (foaf:Person foaf:Organization) ] .

schema:funder a owl:ObjectProperty ;
    rdfs:label "funder"@en ;
    rdfs:comment "A person or organization that supports through funding"@en ;
    rdfs:domain foaf:Document ;
    rdfs:range [ owl:unionOf (foaf:Person foaf:Organization) ] .

schema:provider a owl:ObjectProperty ;
    rdfs:label "provider"@en ;
    rdfs:comment "The service provider, organization, or individual that provides the data"@en ;
    rdfs:domain foaf:Document ;
    rdfs:range [ owl:unionOf (foaf:Person foaf:Organization) ] .
```

#### 2. Document Class Restrictions

**Update `foaf:Document` restrictions:**

```turtle
foaf:Document a owl:Class ;
    rdfs:label "document"@en ;
    rdfs:subClassOf schema:CreativeWork ;

    # Optional author (0 or more)
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty schema:author ;
        owl:allValuesFrom [ owl:unionOf (foaf:Person foaf:Organization) ]
    ] ;

    # Optional contributor (0 or more)
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty schema:contributor ;
        owl:allValuesFrom [ owl:unionOf (foaf:Person foaf:Organization) ]
    ] ;

    # Optional publisher (0 or 1)
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty schema:publisher ;
        owl:maxCardinality 1
    ] ;

    # Other role properties...
    .
```

#### 3. Data Migration Example

**Before (PRO pattern):**
```turtle
:document_1 a foaf:Document ;
    pro:isDocumentContextFor :role_1 .

:role_1 a pro:RoleInTime ;
    pro:withRole pro:author ;
    pro:isHeldBy :person_1 ;
    tvc:atTime :time_interval_1 .

:person_1 a foaf:Person ;
    foaf:name "John Doe" .

:time_interval_1 a ti:TimeInterval ;
    ti:hasIntervalStartDate "2020-01-01"^^xsd:date ;
    ti:hasIntervalEndDate "2020-12-31"^^xsd:date .
```

**After (Schema.org direct):**
```turtle
:document_1 a foaf:Document ;
    schema:author :person_1 ;
    schema:datePublished "2020-01-01"^^xsd:date .  # Use document date instead

:person_1 a foaf:Person ;
    schema:name "John Doe" .
```

---

### Query Comparison

#### Query: Get all authors of a document

**Current (PRO pattern):**
```sparql
PREFIX pro: <http://purl.org/spar/pro/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name WHERE {
  :document_1 pro:isDocumentContextFor ?role .
  ?role pro:withRole pro:author .
  ?role pro:isHeldBy ?person .
  ?person foaf:name ?name .
}
# 4 triple patterns
```

**Proposed (Schema.org):**
```sparql
PREFIX schema: <http://schema.org/>

SELECT ?name WHERE {
  :document_1 schema:author ?person .
  ?person schema:name ?name .
}
# 2 triple patterns (50% reduction)
```

#### Query: Get documents by author name

**Current:**
```sparql
SELECT ?document WHERE {
  ?document pro:isDocumentContextFor ?role .
  ?role pro:withRole pro:author .
  ?role pro:isHeldBy ?person .
  ?person foaf:name "John Doe" .
}
# 4 triple patterns
```

**Proposed:**
```sparql
SELECT ?document WHERE {
  ?document schema:author ?person .
  ?person schema:name "John Doe" .
}
# 2 triple patterns (50% reduction)
```

---

### Temporal Information Strategy

**Question:** What about temporal role information (start/end dates)?

**Options:**

#### Option A: Document-level dates (Recommended)
```turtle
# Most roles align with document publication
:document_1 schema:author :person_1 ;
    schema:datePublished "2020-01-01"^^xsd:date .
```

**Pro:** Simple, covers 90% of use cases
**Con:** Cannot express author active period if different from publication

#### Option B: Reification for temporal roles (if needed)
```turtle
# Only for cases where role time differs from document time
:document_1 schema:author :person_1 .

:authorship_statement_1 a rdf:Statement ;
    rdf:subject :document_1 ;
    rdf:predicate schema:author ;
    rdf:object :person_1 ;
    schema:startDate "2020-01-01"^^xsd:date ;
    schema:endDate "2020-12-31"^^xsd:date .
```

**Pro:** Preserves temporal precision
**Con:** More complex, use only when necessary

---

### Files to Modify

#### Core Ontology Files

1. **`releases/2025-10-14/serializations/triple.ttl`**
   - Lines 232-238: Remove `pro:isDocumentContextFor` property
   - Lines 235-238: Remove `pro:withRole` property
   - Lines 242-270: Remove `pro:RoleInTime` class definition
   - Lines 280-321: Update `foaf:Document` restrictions
   - Add new Schema.org property definitions

2. **Iteration Files (for historical consistency)**
   - `development/03/TBOX.ttl` - Remove PRO pattern, add Schema.org
   - `development/03/ABOX.ttl` - Migrate data examples
   - `development/05/TBOX.ttl` - Update role definitions
   - `development/06/TBOX.ttl` - Update author profile patterns

---

### Benefits

| Benefit | Impact |
|---------|--------|
| **Query Simplification** | 50-75% reduction in patterns |
| **Performance** | Faster SPARQL execution |
| **Maintainability** | Standard vocabulary, less custom code |
| **Interoperability** | Direct Schema.org alignment |
| **Developer Experience** | Easier to understand and use |

---

### Risks

| Risk | Mitigation |
|------|------------|
| **Loss of temporal precision** | Use Option B (reification) where needed |
| **Breaking existing queries** | Provide migration path and dual support period |
| **Data migration effort** | Automated SPARQL UPDATE scripts |

---

## Task 2: Document Type Punning

### Problem Statement

**Current Implementation:** Document types as `skos:Concept` with `dc:type` property

```turtle
# Current pattern (2 triple patterns)
?document dc:type triple:typ_article .
?document a foaf:Document .
```

**Issues:**
- ⚠️ Uses Dublin Core (older standard)
- ⚠️ Requires property hop to get type
- ⚠️ Limited reasoning capabilities

---

### Proposed Solution

**OWL 2 Punning:** Document type terms as both `owl:Class` and `skos:Concept`

```turtle
# Type as BOTH class and concept (punning)
doctypes:Article a owl:Class , skos:Concept ;
    rdfs:subClassOf schema:ScholarlyArticle ;
    skos:inScheme doctypes:DocumentTypes ;
    skos:exactMatch <https://vocabularies.coar-repositories.org/.../c_6501/> ;
    skos:exactMatch schema:ScholarlyArticle .

# Document uses rdf:type directly
:document_1 a :Document ,
              doctypes:Article .  # Direct class membership
```

**Query Pattern:**
```sparql
# Zero-hop query! (1 triple pattern)
?document a doctypes:Article .
```

---

### Implementation Details

#### 1. Create Modular Vocabulary File

**New file:** `vocabularies/document-types.ttl`

```turtle
@prefix : <https://gotriple.eu/vocabulary/document-types#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix schema: <http://schema.org/> .
@prefix coar: <https://vocabularies.coar-repositories.org/resource_types/> .

<https://gotriple.eu/vocabulary/document-types> a owl:Ontology ;
    rdfs:label "GoTriple Document Types Vocabulary"@en ;
    rdfs:comment "Controlled vocabulary for SSH document types using OWL 2 punning"@en ;
    owl:versionInfo "2.0.0" ;
    rdfs:comment "This ontology uses OWL 2 punning for SKOS alignment"@en .

# ConceptScheme
:DocumentTypes a skos:ConceptScheme ;
    rdfs:label "Document Types"@en ;
    skos:prefLabel "GoTriple Document Types"@en .

# ========================================
# DOCUMENT TYPES (OWL 2 Punning Pattern)
# ========================================

:Article a owl:Class , skos:Concept ;
    rdfs:label "Article"@en ;
    rdfs:subClassOf schema:ScholarlyArticle ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Article"@en ;
    skos:altLabel "Research Article"@en ;
    skos:definition "Scholarly article presenting original research"@en ;
    skos:exactMatch coar:c_6501 ;
    skos:exactMatch schema:ScholarlyArticle .

:BookPart a owl:Class , skos:Concept ;
    rdfs:label "Book Part"@en ;
    rdfs:subClassOf schema:Chapter ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Book Part"@en ;
    skos:altLabel "Book Chapter"@en ;
    skos:definition "Chapter or section of a book"@en ;
    skos:exactMatch coar:c_3248 ;
    skos:exactMatch schema:Chapter .

:Dataset a owl:Class , skos:Concept ;
    rdfs:label "Dataset"@en ;
    rdfs:subClassOf schema:Dataset ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Dataset"@en ;
    skos:definition "Collection of structured research data"@en ;
    skos:exactMatch coar:c_ddb1 ;
    skos:exactMatch schema:Dataset .

:Book a owl:Class , skos:Concept ;
    rdfs:label "Book"@en ;
    rdfs:subClassOf schema:Book ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Book"@en ;
    skos:exactMatch coar:c_2f33 ;
    skos:exactMatch schema:Book .

:Thesis a owl:Class , skos:Concept ;
    rdfs:label "Thesis"@en ;
    rdfs:subClassOf schema:Thesis ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Thesis"@en ;
    skos:altLabel "Dissertation"@en ;
    skos:exactMatch schema:Thesis .

:ConferencePaper a owl:Class , skos:Concept ;
    rdfs:label "Conference Paper"@en ;
    rdfs:subClassOf schema:ScholarlyArticle ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Conference Paper"@en ;
    skos:exactMatch coar:c_5794 .

:Report a owl:Class , skos:Concept ;
    rdfs:label "Report"@en ;
    rdfs:subClassOf schema:Report ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Report"@en ;
    skos:exactMatch schema:Report .

:BlogPost a owl:Class , skos:Concept ;
    rdfs:label "Blog Post"@en ;
    rdfs:subClassOf schema:BlogPosting ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Blog Post"@en ;
    skos:exactMatch schema:BlogPosting .

:Image a owl:Class , skos:Concept ;
    rdfs:label "Image"@en ;
    rdfs:subClassOf schema:ImageObject ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Image"@en ;
    skos:exactMatch schema:ImageObject .

:Software a owl:Class , skos:Concept ;
    rdfs:label "Software"@en ;
    rdfs:subClassOf schema:SoftwareSourceCode ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Software"@en ;
    skos:exactMatch schema:SoftwareSourceCode .

:Map a owl:Class , skos:Concept ;
    rdfs:label "Map"@en ;
    rdfs:subClassOf schema:Map ;
    skos:inScheme :DocumentTypes ;
    skos:prefLabel "Map"@en ;
    skos:exactMatch schema:Map .

# Add remaining types: Bibliography, Periodical, Preprint, Review,
# Text, Manuscript, LearningObject, Conference
```

#### 2. Update Core Ontology

**Modify:** `releases/2025-10-14/serializations/triple.ttl`

```turtle
# Import vocabulary
<https://gotriple.eu/ontology/triple> a owl:Ontology ;
    owl:imports <https://gotriple.eu/vocabulary/document-types> ;
    owl:versionInfo "2.0.0" .

# Remove dc:type restriction, documents now use rdf:type directly
foaf:Document a owl:Class ;
    rdfs:subClassOf schema:CreativeWork .
    # No dc:type restriction needed!
```

#### 3. Data Migration

**Before:**
```turtle
:document_1 a foaf:Document ;
    dc:type triple:typ_article .
```

**After:**
```turtle
:document_1 a :Document ,
              doctypes:Article .  # Multi-typing with punning
```

---

### Query Comparison

#### Query: All documents of type Article

**Current:**
```sparql
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?doc WHERE {
  ?doc a foaf:Document ;
       dc:type triple:typ_article .
}
# 2 triple patterns
```

**Proposed:**
```sparql
PREFIX doctypes: <https://gotriple.eu/vocabulary/document-types#>

SELECT ?doc WHERE {
  ?doc a doctypes:Article .
}
# 1 triple pattern (50% reduction)
```

#### Query: Documents with type + COAR alignment

**Current:**
```sparql
SELECT ?doc ?coar WHERE {
  ?doc dc:type ?type .
  ?type skos:exactMatch ?coar .
  FILTER(STRSTARTS(STR(?coar), "https://vocabularies.coar"))
}
# 3 patterns
```

**Proposed:**
```sparql
SELECT ?doc ?coar WHERE {
  ?doc a ?type .
  ?type skos:exactMatch ?coar .
  FILTER(STRSTARTS(STR(?coar), "https://vocabularies.coar"))
}
# 2 patterns (33% reduction)
```

---

### Files to Create/Modify

#### New Files
1. **`vocabularies/document-types.ttl`** - Complete vocabulary with punning

#### Files to Modify
2. **`releases/2025-10-14/serializations/triple.ttl`**
   - Add `owl:imports` for vocabulary
   - Remove `dc:type` restriction from `foaf:Document`
   - Line 217: Remove or deprecate `dc:type` property

3. **Iteration files**
   - `development/08/TBOX.ttl` - Update to punning pattern
   - `development/08/ABOX.ttl` - Migrate data examples

---

### Benefits

| Benefit | Impact |
|---------|--------|
| **Zero-hop queries** | 50% reduction for type queries |
| **Modular vocabulary** | Separate file, easier maintenance |
| **OWL reasoning** | Type hierarchy inference |
| **SKOS preserved** | All alignments maintained |
| **Schema.org alignment** | Better LOD integration |

---

## Implementation Strategy

### Phase 1: Preparation (Week 1)

1. ✅ **Analysis Complete**
   - Current roles identified
   - Schema.org mappings confirmed
   - Query patterns documented

2. **Create test environment**
   - Copy current ontology to `/development/refactoring/`
   - Set up SPARQL endpoint for testing
   - Prepare test data samples

3. **Create vocabulary files**
   - `vocabularies/document-types.ttl`
   - `vocabularies/licenses.ttl` (if needed)
   - `vocabularies/access-conditions.ttl` (if needed)

### Phase 2: Implementation (Week 2)

4. **Implement Task 2 (Document Types)**
   - Create modular vocabulary with punning
   - Update core ontology imports
   - Remove `dc:type` restrictions
   - Test queries

5. **Implement Task 1 (Roles)**
   - Add Schema.org property definitions
   - Remove PRO pattern classes
   - Update `foaf:Document` restrictions
   - Migrate test data

6. **Update iteration files**
   - Refactor iterations 03, 05, 06, 08
   - Update formal competency questions
   - Update ABOX examples

### Phase 3: Testing (Week 3)

7. **Query testing**
   - Run all formal competency questions
   - Compare query performance
   - Validate SPARQL results

8. **Reasoning testing**
   - Test OWL reasoning with punning
   - Validate type hierarchy inference
   - Check SKOS alignment queries

9. **Documentation**
   - Update CLAUDE.md with new patterns
   - Create migration guide
   - Update README with changes

### Phase 4: Release (Week 4)

10. **Create new release**
    - Version 2.0.0
    - Update CHANGELOG.md
    - Tag Git repository

11. **Migration support**
    - Provide SPARQL UPDATE scripts
    - Create backward compatibility layer (optional)
    - Document breaking changes

---

## Migration Path

### Automated Migration Scripts

#### Script 1: Migrate Document Types

```sparql
# SPARQL UPDATE: Convert dc:type to rdf:type with punning
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX triple: <https://gotriple.eu/ontology/triple#>
PREFIX doctypes: <https://gotriple.eu/vocabulary/document-types#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

DELETE {
  ?doc dc:type ?oldType .
}
INSERT {
  ?doc a ?newType .
}
WHERE {
  ?doc a foaf:Document ;
       dc:type ?oldType .

  # Type mapping
  VALUES (?oldType ?newType) {
    (triple:typ_article doctypes:Article)
    (triple:typ_book-part doctypes:BookPart)
    (triple:typ_dataset doctypes:Dataset)
    (triple:typ_book doctypes:Book)
    (triple:typ_thesis doctypes:Thesis)
    # ... add all mappings
  }
}
```

#### Script 2: Migrate PRO Roles to Schema.org

```sparql
# SPARQL UPDATE: Convert PRO author pattern to schema:author
PREFIX pro: <http://purl.org/spar/pro/>
PREFIX schema: <http://schema.org/>

DELETE {
  ?doc pro:isDocumentContextFor ?role .
  ?role pro:withRole pro:author .
  ?role pro:isHeldBy ?person .
}
INSERT {
  ?doc schema:author ?person .
}
WHERE {
  ?doc pro:isDocumentContextFor ?role .
  ?role pro:withRole pro:author ;
        pro:isHeldBy ?person .
}
```

### Backward Compatibility Option

For transition period, support both patterns:

```turtle
# Document with BOTH patterns
:document_1 a :Document ,
              doctypes:Article ;      # New pattern
    dc:type doctypes:Article ;        # Old pattern (deprecated)
    schema:author :person_1 ;         # New pattern
    pro:isDocumentContextFor :role_1 . # Old pattern (deprecated)
```

---

## Testing Plan

### Test Cases

#### 1. Document Type Queries

| Test ID | Query | Expected Result | Status |
|---------|-------|----------------|--------|
| DT-01 | All Article documents | List of documents | ☐ |
| DT-02 | Document type with COAR alignment | Type + COAR URI | ☐ |
| DT-03 | Type hierarchy reasoning | Inferred ScholarlyArticle | ☐ |
| DT-04 | Type vocabulary listing | All types in scheme | ☐ |

#### 2. Role Queries

| Test ID | Query | Expected Result | Status |
|---------|-------|----------------|--------|
| R-01 | Authors of document | List of authors | ☐ |
| R-02 | Documents by author | List of documents | ☐ |
| R-03 | Multiple roles (author + funder) | Combined results | ☐ |
| R-04 | Organization as publisher | Organization entity | ☐ |

#### 3. Performance Tests

| Test ID | Metric | Current | Target | Status |
|---------|--------|---------|--------|--------|
| P-01 | Author query time | Baseline | -50% | ☐ |
| P-02 | Type query time | Baseline | -50% | ☐ |
| P-03 | Complex query (roles + types) | Baseline | -40% | ☐ |

---

## Risks and Mitigations

### High Risk

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Breaking existing applications** | HIGH | HIGH | Provide migration period with dual support |
| **Data loss during migration** | CRITICAL | LOW | Comprehensive backup + rollback plan |
| **OWL reasoner incompatibility** | MEDIUM | LOW | Test with multiple reasoners (Pellet, HermiT) |

### Medium Risk

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Query performance degradation** | MEDIUM | LOW | Benchmark before/after, optimize if needed |
| **Loss of temporal role information** | MEDIUM | MEDIUM | Provide reification option for edge cases |
| **SKOS tool incompatibility** | LOW | LOW | Document punning pattern, test with SKOS tools |

---

## Success Criteria

### Functional Requirements

- ✅ All formal competency questions pass
- ✅ All SKOS alignments preserved
- ✅ Schema.org validation successful
- ✅ OWL reasoning functional

### Performance Requirements

- ✅ Query complexity reduced by 50%+
- ✅ SPARQL execution time reduced by 30%+
- ✅ Ontology file size maintained or reduced

### Quality Requirements

- ✅ No data loss during migration
- ✅ Backward compatibility for 6 months
- ✅ Complete documentation
- ✅ Migration scripts validated

---

## Timeline

```
Week 1 (Preparation)
├── Day 1-2: Set up test environment
├── Day 3-4: Create vocabulary files
└── Day 5: Preparation review

Week 2 (Implementation)
├── Day 1-2: Implement Task 2 (Document Types)
├── Day 3-4: Implement Task 1 (Roles)
└── Day 5: Code review

Week 3 (Testing)
├── Day 1-2: Query testing
├── Day 3: Reasoning testing
└── Day 4-5: Documentation

Week 4 (Release)
├── Day 1-2: Final testing
├── Day 3: Create release
└── Day 4-5: Migration support
```

---

## Appendix

### A. Schema.org Properties Reference

Complete list of CreativeWork properties (v29.3):

- `schema:author` - Author of the work
- `schema:contributor` - Secondary contributor
- `schema:publisher` - Publisher
- `schema:producer` - Producer
- `schema:creator` - Creator (synonym for author)
- `schema:funder` - Funding organization
- `schema:provider` - Data/service provider
- `schema:editor` - Editor
- `schema:translator` - Translator
- `schema:copyrightHolder` - Copyright holder

### B. Current vs Proposed Architecture Diagrams

#### Current Architecture
```
Document → pro:isDocumentContextFor → RoleInTime → pro:withRole → Role (author)
                                    ↓
                                pro:isHeldBy → Person/Organization
                                    ↓
                                tvc:atTime → TimeInterval
```

#### Proposed Architecture
```
Document → schema:author → Person/Organization
        ↓
    schema:datePublished → xsd:date
```

### C. Contact

**Questions or Issues:**
- Create GitHub issue: `https://github.com/atrium-research/triple-ontology/issues`
- Email: [project contact]

---

**Document End**
