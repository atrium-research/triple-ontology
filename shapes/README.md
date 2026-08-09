# TRIPLE Shapes

Conformance constraints for TRIPLE data, as a SHACL shapes graph.

## Why they exist

The OWL ontology says what the terms *mean*. It cannot say what data is *acceptable*:
OWL restrictions describe inferences, not constraints. Under open-world semantics a
missing mandatory value is inferred to exist rather than reported, and
`owl:qualifiedCardinality 1` on two distinct nodes concludes they are the same node
instead of flagging an error. Mandatoriness therefore lives here, where it is checked.

## Files

- `triple-shapes.ttl` — the `sh:ShapesGraph` root; imports the ontology, lists the members.
- `identifier.shapes.ttl` — the identifier node: exactly one scheme, exactly one value,
  plus value patterns per scheme (ARK, DOI) that OWL cannot express at all.
- `entity.shapes.ttl` — which identifiers each entity must carry.

## Running the validation

```bash
source scripts/venv/bin/activate
python scripts/validate.py                    # every iteration ABOX + the examples
python scripts/validate.py development/01/ABOX.ttl
```

## Severity

| Severity | Meaning |
|---|---|
| `sh:Violation` | mandatory — the data is not conformant |
| `sh:Warning` | recommended — expected in well-formed data |
| `sh:Info` | expected but optional; usually signals a mapping error |
