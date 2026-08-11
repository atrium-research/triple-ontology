# Glossary of Terms - Iteration 21

| Term | Definition |
|------|------------|
| `schema:isBasedOn` | A resource from which this work is derived or from which it is a modification or adaptation (schema.org; supersedes the deprecated `isBasedOnUrl`). Role-B link: the value is an IRI. |
| `dcterms:references` | A related resource that is referenced, cited, or otherwise pointed to by the described resource (DCMI). Declared inverse of `dcterms:isReferencedBy`, already in the model on the passive side. |
| `dcterms:isReferencedBy` | A related resource that references, cites, or otherwise points to the described resource (DCMI; defined in iteration 10). |
| `dcat:accessURL` | A URL of a resource that gives access to a distribution of the dataset, e.g. a landing page or portal (DCAT). IRI-valued. |
| `dcat:downloadURL` | The URL of the downloadable file of a distribution in a given format (DCAT). IRI-valued. |
| `dcat:Distribution` | A specific representation of a dataset (DCAT; used since iteration 10). |
| `schema:jobTitle` | The job title of the person, as a plain string (schema.org). Chosen over `schema:hasOccupation`, whose range demands a structured `Occupation` node the platform data cannot fill yet. |
| `triple:Document`, `triple:Dataset`, `triple:Profile` | Platform entities (iterations 01, 10, 06) carrying the new links. |
