# Motivating Scenario - Iteration 13

## Name
CIDOC-CRM and SSHOCRo Alignment for TRIPLE Resource Classes

## General Description
To enhance interoperability with cultural heritage and Social Sciences and Humanities (SSH) research infrastructures, the TRIPLE ontology needs to align its core resource classes with CIDOC-CRM (Conceptual Reference Model) and SSHOCRo (Social Sciences and Humanities Open Cloud Reference Ontology).

CIDOC-CRM is the ISO standard (ISO 21127) for cultural heritage documentation and provides well-established conceptual modeling patterns. SSHOCRo extends and specializes CIDOC-CRM for SSH research contexts, offering more precise classifications for scholarly resources and activities.

## Alignments

### Document Resources

**triple:Document → cidoc:E31_Document**
- CIDOC-CRM E31_Document represents identifiable immaterial items that make propositions about reality
- Traditional documents (publications, reports, articles) align with this class

**triple:Document (Publications) → sshocro:SHE8_Publication**
- SSHOCRo provides SSH-specific refinement for publications
- More precise classification for scholarly publications

### Non-Traditional Resources

**triple:Multimedia → cidoc:E90_Symbolic_Object**
- E90_Symbolic_Object represents symbols and informational objects
- Suitable for audio-visual content (audio, video, interactive media)

**triple:Software → cidoc:E90_Symbolic_Object**
- E90_Symbolic_Object encompasses executable code and software applications
- Broader than E31_Document for non-textual symbolic content

**triple:SemanticArtefact → cidoc:E90_Symbolic_Object**
- E90_Symbolic_Object includes formal symbolic representations
- Appropriate for ontologies, vocabularies, taxonomies

### Project Resources

**triple:Project → sshocro:SHE3_SSH_Project**
- SSHOCRo offers SSH-specific project classification
- More precise than generic E7_Activity for SSH research projects
