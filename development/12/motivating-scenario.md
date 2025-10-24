# Motivating Scenario - Iteration 12

## Name
Extension of Resource Types: Semantic Artefacts, Software, and Multimedia

## General Description
The GoTriple platform needs to extend its resource type taxonomy beyond traditional documents to include three additional major categories of scholarly resources: Semantic Artefacts (ontologies, vocabularies, taxonomies), Software (research software, tools, code repositories), and Multimedia resources (audio, video, interactive media). These resource types are increasingly important in SSH research and require proper classification and metadata support.

While the current ontology has `triple:Document` as a subclass of `schema:CreativeWork` and `foaf:Document`, these new resource types represent distinct categories that should be positioned at the same hierarchical level as `triple:Document`, all being subclasses of `schema:CreativeWork`.

## Technical Specification

The ontology must support:

1. **Semantic Artefacts** (`triple:SemanticArtefact`): Resources that formalize knowledge structures
   - Ontologies, vocabularies, controlled vocabularies
   - Taxonomies, thesauri, classification schemes
   - Knowledge graphs and semantic models
   - All metadata applicable to documents (identifiers, titles, descriptions, authors, etc.)

2. **Software** (`triple:Software`): Executable programs, code, and computational tools
   - Research software applications
   - Code repositories and libraries
   - Scripts, algorithms, computational workflows
   - All metadata applicable to documents plus software-specific properties

3. **Multimedia** (`triple:Multimedia`): Audio-visual and interactive content
   - Audio recordings (interviews, lectures, oral histories)
   - Video recordings (documentaries, presentations, performances)
   - Interactive multimedia resources
   - All metadata applicable to documents plus multimedia-specific properties

## Examples

