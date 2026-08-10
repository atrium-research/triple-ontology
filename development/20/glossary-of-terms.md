# Glossary of Terms - Iteration 20

| Term | Definition |
|------|------------|
| `triple:Document` | A document in the GoTriple platform (defined in iteration 01; used here as the record kind being deduplicated). |
| `triple:isDuplicateOf` | Links a record to the representative record of the same scholarly work, elected by the GoTriple deduplication pipeline. The direction carries the role: the representative is the target and asserts nothing. Specialises `prov:alternateOf`. |
| `prov:alternateOf` | PROV-O property relating two entities that present aspects of the same thing. Reflexive, symmetric and transitive by specification; the specialisation adds the direction towards the representative. |
| `schema:headline` | Title of the record (schema.org). |
| `schema:provider` | The service or organization that provided the record (schema.org). |
