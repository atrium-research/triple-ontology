# Motivating Scenario (Iteration 15)

## Name
Graphia - Modeling AI-Extracted Entity Mentions

## Description

### Context
The Graphia project utilizes AI systems (NER/Entity Linking) to automatically extract entity mentions from documents. These mentions need to be represented in the ontology in a way that preserves the link between the document and the entity while accommodating different levels of entity resolution.

### Objective
Represent entity mentions detected in documents using the **Web Annotation Ontology (OA)**. The system must link these mentions to the most appropriate URI available: a direct external URI (e.g., Wikidata), an existing internal URI, or a newly minted local URI.

### Modeling Strategy
The core principle is to avoid redefining individuals if a URI already exists.
-   **External URIs**: Used directly (e.g., Wikidata).
-   **Internal URIs**: Used directly if the entity is already known.
-   **New Local URIs**: Minted only when no match is found. Using dual typing (`schema:Type` + `skos:Concept`) for compatibility.

### Implementation Scenarios

#### Scenario A: External Match Found
The NER service identifies an external resource (e.g., Ada Lovelace on Wikidata).
*   **Action**: `oa:hasBody` points to `<http://www.wikidata.org/entity/Q7259>`.
*   **Enrichment**: The external URI is typed as `schema:Person` in the local graph.

#### Scenario B: Internal Match Found
The entity matches an existing project partner or researcher.
*   **Action**: `oa:hasBody` points to existing URI `triple:JaneDoe`.

#### Scenario C: No Match / Ambiguous
The entity is new and not found externally.
*   **Action**: Mint new URI `triple:person_1`.
*   **Typing**: Entity is defined as `a schema:Person, skos:Concept`.

### Example
A document "Graphia Report 2025" mentions:
1.  **Ada Lovelace** (Linked to Wikidata Q7259).
2.  **Jane Doe** (Known researcher, internal URI).
3.  **John Smith** (New entity, local URI).
