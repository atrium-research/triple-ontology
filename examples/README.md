# Examples

Worked examples of GoTriple data expressed with the TRIPLE ontology.

## Contents

- `jsonld/document-complete-example.jsonld` — one complete document record in
  JSON-LD: identifiers (reified, scheme-tagged), descriptive core, vocabulary
  links (`disc:`/`ct:`/`coa:`/`lic:`), original values, annotations. Kept in
  sync with the model: it is validated by the SHACL profile at every release.

## Validating

The examples are part of the standard validation perimeter:

```bash
source scripts/venv/bin/activate
python scripts/validate.py          # iterations + examples/ + vocabularies
```

## Reading JSON-LD, in short

`@context` binds the prefixes, `@id` is the resource IRI, `@type` its class,
`@language`/`@value` carry language-tagged literals, `@graph` holds the node
list. The full syntax is the [JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld11/).
