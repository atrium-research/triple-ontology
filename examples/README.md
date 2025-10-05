# TRIPLE Ontology Examples

This directory contains practical examples of data exported using the TRIPLE ontology model.

## Directory Structure

```
examples/
├── jsonld/          # JSON-LD serialization examples
│   └── ...
└── README.md        # This file
```

## JSON-LD Examples

The `jsonld/` directory contains example documents, profiles, projects, and other entities serialized in JSON-LD format following the TRIPLE ontology structure.

Each example demonstrates:
- Proper use of TRIPLE ontology classes and properties
- Correct namespace declarations and context
- Real-world data patterns from the GoTriple platform
- Best practices for RDF serialization in JSON-LD

## Purpose

These examples serve as:
- **Reference implementations** for data producers integrating with GoTriple
- **Test cases** for validating ontology coverage
- **Documentation** showing practical application of ontology patterns
- **Templates** for creating new data exports

## Usage

Examples can be:
1. Used as templates for creating new data exports
2. Validated against the ontology using RDF tools
3. Converted to other RDF formats (Turtle, RDF/XML, etc.)
4. Loaded into triple stores for querying

## Validation

To validate JSON-LD examples against the ontology:

```bash
# Convert JSON-LD to Turtle and validate
rdfpipe -i json-ld -o turtle example.jsonld > example.ttl

# Load into RDF store and run SPARQL validation queries
```

## Contributing

When adding new examples:
1. Use meaningful filenames (e.g., `document-with-authors.jsonld`)
2. Include inline comments explaining key patterns
3. Follow JSON-LD best practices
4. Validate against the ontology before committing
