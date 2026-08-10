#!/usr/bin/env python3
"""Generate ontology/modules/serializations/*.ttl from the consolidated model.

A module is the class, its neighbours at one hop, the terms its SHACL shapes
mention, and the extras listed in the sidecar <M>.metadata.ttl — which is the
only hand-written part, together with the module's own descriptive metadata.

Usage: python scripts/build_modules.py [--check]
"""
from __future__ import annotations

import sys
from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.compare import graph_diff, to_isomorphic
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS

ROOT = Path(__file__).resolve().parent.parent
MODEL = ROOT / "ontology" / "triple.ttl"
METADATA = ROOT / "ontology" / "metadata.ttl"
SHAPES_DIR = ROOT / "shapes"
MODULES_DIR = ROOT / "ontology" / "modules" / "serializations"

TRIPLE = Namespace("https://gotriple.eu/ontology/triple/")
SH = Namespace("http://www.w3.org/ns/shacl#")
TBUILD = Namespace("https://gotriple.eu/ontology/triple/build#")

MODULES = ["Document", "Dataset", "MediaObject", "SemanticArtefact", "Project", "Profile"]

FOLLOW = {RDFS.subClassOf, RDFS.subPropertyOf, RDFS.range, RDFS.domain,
          OWL.equivalentClass, SKOS.exactMatch, SKOS.closeMatch,
          SKOS.broadMatch, SKOS.relatedMatch}
IN_RESTRICTION = {OWL.onProperty, OWL.allValuesFrom, OWL.someValuesFrom,
                  OWL.onClass, OWL.onDataRange, OWL.hasValue}
HEADER = (DCTERMS.title, DCTERMS.abstract, DCTERMS.description, DCTERMS.creator,
          DCTERMS.contributor, DCTERMS.created, DCTERMS.modified, OWL.versionInfo,
          URIRef("https://schema.org/creativeWorkStatus"))


def reachable(model: Graph, root: URIRef, depth: int = 1) -> set[URIRef]:
    """Terms reachable from the class. One hop: two would double the module."""
    seen: set[URIRef] = {root}
    frontier: set[URIRef] = {root}
    for _ in range(depth):
        found: set[URIRef] = set()
        for subject in frontier:
            for p, o in model.predicate_objects(subject):
                targets: list[URIRef] = []
                if isinstance(o, BNode):
                    targets += _terms_in_node(model, o)
                elif isinstance(o, URIRef) and p in FOLLOW:
                    targets.append(o)
                found |= {t for t in targets
                          if t not in seen and not str(t).startswith(str(OWL))}
        seen |= found
        frontier = found
    return seen


def _terms_in_node(model: Graph, node: BNode, depth: int = 3) -> list[URIRef]:
    """Named terms inside a restriction, a union or a list."""
    out: list[URIRef] = []
    if depth == 0:
        return out
    for p, o in model.predicate_objects(node):
        if isinstance(o, URIRef) and (p in IN_RESTRICTION or p == RDF.first or p in FOLLOW):
            out.append(o)
        elif isinstance(o, BNode):
            out += _terms_in_node(model, o, depth - 1)
    return out


def shape_terms(shapes: Graph, root: URIRef) -> set[URIRef]:
    """Terms the shapes targeting this class mention — the identifier model lives there."""
    out: set[URIRef] = set()
    for shape in shapes.subjects(SH.targetClass, root):
        for prop_shape in shapes.objects(shape, SH.property):
            out |= _terms_in_shape(shapes, prop_shape)
    return {t for t in out if not str(t).startswith(str(SH))}


def _terms_in_shape(shapes: Graph, node, depth: int = 3) -> set[URIRef]:
    out: set[URIRef] = set()
    if depth == 0:
        return out
    for p, o in shapes.predicate_objects(node):
        if isinstance(o, URIRef) and p in (SH.path, SH["class"], SH.hasValue, SH.datatype):
            out.add(o)
        elif p == SH["in"]:
            item = o
            while item and item != RDF.nil:
                value = shapes.value(item, RDF.first)
                if isinstance(value, URIRef):
                    out.add(value)
                item = shapes.value(item, RDF.rest)
        elif isinstance(o, (BNode, URIRef)) and p in (SH.property, SH.qualifiedValueShape, SH.node):
            out |= _terms_in_shape(shapes, o, depth - 1)
    return out


def describe(model: Graph, term: URIRef, into: Graph, *, axioms: bool = True) -> None:
    """Copy a term's description. Without `axioms`, its restrictions are left out:
    they would link to properties the module does not document."""
    for p, o in model.predicate_objects(term):
        if not axioms and isinstance(o, BNode) and p == RDFS.subClassOf:
            continue
        into.add((term, p, o))
        if isinstance(o, BNode):
            _copy_node(model, o, into)


def _copy_node(model: Graph, node: BNode, into: Graph) -> None:
    for p, o in model.predicate_objects(node):
        into.add((node, p, o))
        if isinstance(o, BNode):
            _copy_node(model, o, into)


def sidecar_path(module: str) -> Path:
    return MODULES_DIR / f"{module}.metadata.ttl"


def build(module: str, model: Graph, shapes: Graph, meta: Graph) -> Graph:
    root = TRIPLE[module]
    side = Graph()
    if sidecar_path(module).exists():
        side.parse(sidecar_path(module), format="turtle")

    members = reachable(model, root) | shape_terms(shapes, root)
    members |= {t for t in side.objects(root, TBUILD.includes) if isinstance(t, URIRef)}

    out = Graph()
    for prefix, ns in model.namespaces():
        out.bind(prefix, ns)
    out.bind("skos", SKOS)

    # pyLODE expects the module to declare itself an ontology on the class IRI
    out.add((root, RDF.type, OWL.Ontology))
    for prop in HEADER:
        for value in side.objects(root, prop):
            out.add((root, prop, value))
    subject = URIRef("https://gotriple.eu/ontology/triple")
    for prop in (OWL.versionInfo, DCTERMS.modified):
        for value in meta.objects(subject, prop):
            out.set((root, prop, Literal(str(value))))

    for term in sorted(members, key=str):
        if isinstance(term, URIRef):
            describe(model, term, out, axioms=(term == root))
    return out


def main() -> int:
    check_only = "--check" in sys.argv
    model = Graph()
    model.parse(MODEL, format="turtle")
    meta = Graph()
    meta.parse(METADATA, format="turtle")
    shapes = Graph()
    for f in sorted(SHAPES_DIR.glob("*.ttl")):
        shapes.parse(f, format="turtle")

    differing = 0
    for module in MODULES:
        built = build(module, model, shapes, meta)
        target = MODULES_DIR / f"{module}.ttl"
        if check_only:
            current = Graph()
            if target.exists():
                current.parse(target, format="turtle")
            _, only_built, only_file = graph_diff(to_isomorphic(built), to_isomorphic(current))
            status = "OK" if not (len(only_built) or len(only_file)) else "DIVERSO"
            print(f"  {status:8} {module:18} mancanti nel file: {len(only_built):3}  "
                  f"in più: {len(only_file):3}")
            differing += bool(len(only_built) or len(only_file))
        else:
            target.write_text(built.serialize(format="turtle"))
            print(f"  scritto  {module:18} {len(built)} triple")

    if check_only and differing:
        print(f"\n{differing} moduli non corrispondono — esegui python scripts/build_modules.py")
        return 1
    print("\nfatto")
    return 0


if __name__ == "__main__":
    sys.exit(main())
