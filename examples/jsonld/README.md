# JSON-LD Examples

## How to Read JSON-LD

JSON-LD (JSON for Linking Data) is a JSON-based format for representing RDF data. Here's a quick guide:

### Key Concepts

**`@context`**: Defines prefixes and namespaces
```json
"@context": {
  "foaf": "http://xmlns.com/foaf/0.1/",
  "schema": "http://schema.org/"
}
```

**`@id`**: The URI identifier of a resource
```json
"@id": "https://gotriple.eu/document/12345"
```

**`@type`**: The RDF type (class) of a resource
```json
"@type": "foaf:Document"
```

**`@value`**: Literal value (especially for typed/language-tagged literals)
```json
{
  "@language": "en",
  "@value": "Digital Humanities"
}
```

**`@graph`**: Contains an array of resources (nodes)
```json
"@graph": [ {...}, {...} ]
```

### Reading Example

```json
{
  "@id": "https://gotriple.eu/document/12345",
  "@type": "foaf:Document",
  "dcterms:title": {
    "@language": "en",
    "@value": "Digital Humanities in the Age of AI"
  }
}
```

**Translation to RDF:**
```turtle
<https://gotriple.eu/document/12345> a foaf:Document ;
    dcterms:title "Digital Humanities in the Age of AI"@en .
```

### Nested Objects

Objects can be **embedded** or **referenced by ID**:

```json
"schema:mentions": {
  "@id": "https://gotriple.eu/person/alan-turing",
  "@type": "foaf:Person",
  "foaf:name": "Alan Turing"
}
```

### Arrays

Arrays represent multiple values:

```json
"schema:keywords": [
  { "@value": "Digital Humanities" },
  { "@value": "AI" }
]
```

## Tools

**Validate and convert:**
```bash
# View as Turtle
rdfpipe -i json-ld -o turtle document-complete-example.jsonld

# Validate structure
jsonld validate document-complete-example.jsonld
```

**Online playground:**
- https://json-ld.org/playground/

## Files

- **document-complete-example.jsonld**: Comprehensive document example using all ontology features
