# Glossary of Terms (Iteration 15)

| Term | Definition |
| :--- | :--- |
| `oa:Annotation` | The class for Web Annotations. Represents a connection between a target resource (the document) and a body resource (the entity mentioned). |
| `oa:hasTarget` | Property linking the Annotation to the resource being annotated (the document). |
| `oa:hasBody` | Property linking the Annotation to the body of the annotation (the entity being mentioned). |
| `oa:motivatedBy` | Property indicating the motivation for the annotation. In this case, `oa:identifying`. |
| `oa:identifying` | The motivation for the annotation, indicating that the purpose is to identify the entity mentioned in the target. |
| `skos:Concept` | Used for dual typing of new local entities to maintain compatibility with SKOS-based tools. |
| `schema:Person` | Schema.org class used to type the entities (both external and internal). |
