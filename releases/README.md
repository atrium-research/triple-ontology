# TRIPLE Ontology Releases

Official releases of the TRIPLE ontology for the GoTriple discovery platform.

## Latest Version

- **2025-10-22** (v1.0.0) - Initial public release

## Release Structure

Each release (organized by date YYYY-MM-DD) contains:

- **serializations/** - Ontology in multiple RDF formats (.ttl, .rdf, .owl, .jsonld, .nt)
- **vocabularies/** - Controlled vocabulary modules (licenses, access conditions, document types, disciplines, identifier schemes)
- **documentation/html/** - HTML documentation with CSS/JS
- **documentation/diagrams/** - Visual Graffoo diagrams
- **RELEASE-NOTES.md** - Detailed release notes

## Usage

```turtle
@prefix triple: <https://gotriple.eu/ontology/triple#> .
```

- **Base namespace**: `https://gotriple.eu/ontology/triple#`
- **Ontology IRI**: `https://gotriple.eu/ontology/triple`

## Development

See `development/` directory for complete SAMOD iteration history.
