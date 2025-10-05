# Motivating Scenario (Iteration 11)

## Name
Document Mentions and References

## Description

### General description

Scholarly documents in the Social Sciences and Humanities do not exist in isolation. They form complex networks of references, citations, and mentions that connect research artifacts, people, projects, and institutions. Understanding these connections is crucial for discovering related research, tracing the evolution of ideas, and identifying collaboration patterns.

In the GoTriple platform, documents can mention various types of entities:

1. **Other Documents**: Citations and bibliographic references to other publications, datasets, or research outputs. These mentions create citation networks and help users discover related work.

2. **People**: Mentions of researchers, authors, or scholars discussed in the text but who are not necessarily authors or contributors to the document itself. For example, a paper about digital humanities might mention prominent figures in the field.

3. **Projects**: References to research projects, initiatives, or programs that are discussed, evaluated, or related to the document's content. This helps connect documents to the broader research ecosystem.

4. **Organizations**: Mentions of institutions, research centers, universities, or funding bodies that are relevant to the document's context but may not have a formal role (like publisher or funder).

By capturing these mentions explicitly in the ontology, GoTriple enables:
- **Discovery of related resources**: Users can navigate from one document to mentioned entities
- **Network analysis**: Understanding citation patterns and research connections
- **Context enrichment**: Providing richer context about a document's intellectual environment
- **Cross-referencing**: Linking documents across different types of relationships

### Technical specification

The mentions functionality will be implemented using the `schema:mentions` property from Schema.org vocabulary. This property is designed to indicate that a CreativeWork (in our case, a Document) contains a reference to a subject.

**Property specification:**

- **Property**: `schema:mentions`
- **Domain**: `schema:CreativeWork` (compatible with `foaf:Document`)
- **Range**: `schema:Thing` (allows mentioning any type of entity)
- **Usage**: Connects documents to mentioned entities of various types

**Compatibility declaration:**

To ensure semantic consistency, we explicitly declare that `foaf:Document` is a subclass of `schema:CreativeWork`:

```turtle
foaf:Document rdfs:subClassOf schema:CreativeWork .
```

This ensures that all documents in GoTriple are recognized as creative works, making the use of `schema:mentions` semantically valid.

**Entities that can be mentioned:**

1. **Documents** (`foaf:Document`): Other publications in the GoTriple platform or external resources
2. **People** (`foaf:Person`): Researchers, scholars, authors mentioned in the text
3. **Projects** (`schema:Project`): Research projects discussed or referenced
4. **Organizations** (`foaf:Organization`): Institutions, research centers, funding bodies

The flexible range of `schema:mentions` allows for mentioning any type of entity, making the model extensible for future needs while maintaining simplicity.

**Querying mentions:**

To query specific types of mentions, SPARQL queries can filter by the type of the mentioned entity:

```sparql
# Find all documents mentioned by document_1
SELECT ?mentioned WHERE {
  triple:document_1 schema:mentions ?mentioned .
  ?mentioned a foaf:Document .
}
```

## Example 1

`document_1` mentions `document_45` (a bibliographic reference to another paper in GoTriple). It also mentions `person_23` (a researcher discussed in the text).

## Example 2

`document_67` mentions `project_12` (a research project that the paper evaluates) and `organization_5` (a research institute mentioned in the methodology section).

## Example 3

`document_89` mentions three other documents: `document_100`, `document_101`, and `document_102` (forming a citation network).

## Example 4

`document_34` mentions `person_78` (a prominent scholar in the field whose work is discussed) and `organization_23` (a university that conducted related research).
