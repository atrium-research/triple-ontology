#!/usr/bin/env python3
"""Invariants of the consolidated model. See "One home per term" in the samod skill.

Usage: python scripts/check_model.py [path/to/triple.ttl]
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

from rdflib import BNode, Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

TRIPLE = "https://gotriple.eu/ontology/triple/"
TERM_KINDS = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty,
              OWL.NamedIndividual, OWL.AnnotationProperty)
FOREIGN_FORBIDDEN = (RDFS.domain, RDFS.range, RDFS.subPropertyOf)
BASELINE = "check_model_baseline.txt"


def terms(g: Graph) -> set[URIRef]:
    """Every declared term."""
    return {s for kind in TERM_KINDS for s in g.subjects(RDF.type, kind)
            if isinstance(s, URIRef)}


def short(iri) -> str:
    s = str(iri)
    return "triple:" + s[len(TRIPLE):] if s.startswith(TRIPLE) else s


def check_one_comment_per_language(g: Graph) -> list[str]:
    """Two iterations annotating the same term produce two comments after the merge."""
    problems = []
    by_term = defaultdict(lambda: defaultdict(list))
    for s, _, o in g.triples((None, RDFS.comment, None)):
        by_term[s][o.language].append(str(o))
    for term, by_lang in sorted(by_term.items(), key=lambda x: str(x[0])):
        for lang, values in sorted(by_lang.items(), key=lambda x: str(x[0])):
            if len(values) > 1:
                problems.append(
                    f"{short(term)} has {len(values)} comments in "
                    f"{lang or '(no language tag)'}:\n"
                    + "\n".join(f"        - {v}" for v in sorted(values))
                )
    return problems


def check_own_terms_documented(g: Graph) -> list[str]:
    """Every triple: term carries a label and a comment."""
    problems = []
    for term in sorted(terms(g), key=str):
        if not str(term).startswith(TRIPLE):
            continue
        missing = [name for name, prop in (("label", RDFS.label), ("comment", RDFS.comment))
                   if not list(g.objects(term, prop))]
        if missing:
            problems.append(f"{short(term)} has no {' and no '.join(missing)}")
    return problems


def foreign_axioms(g: Graph) -> list[str]:
    """Global axioms on terms outside triple:, as stable signatures."""
    out = []
    for prop in FOREIGN_FORBIDDEN:
        for s, _, o in g.triples((None, prop, None)):
            if isinstance(s, URIRef) and not str(s).startswith(TRIPLE):
                target = "_:anon" if isinstance(o, BNode) else short(o)
                out.append(f"{short(s)} {g.qname(prop)} {target}")
    return sorted(set(out))


def check_no_new_axioms_on_foreign_terms(g: Graph) -> list[str]:
    """Never narrow a property we do not own. The baseline lists the axioms that
    only restate what the source vocabulary declares, verified against it."""
    path = Path(__file__).resolve().parent / BASELINE
    known = set()
    if path.exists():
        known = {line.strip() for line in path.read_text().splitlines()
                 if line.strip() and not line.startswith("#")}
    return [
        f"{axiom} — constrain the value per class with owl:allValuesFrom, or in shapes/"
        for axiom in foreign_axioms(g) if axiom not in known
    ]


def check_referenced_terms_declared(g: Graph) -> list[str]:
    """A term used as superclass, range or inside a restriction must be declared."""
    declared = terms(g) | set(g.subjects(RDF.type, RDFS.Datatype))
    referenced: set[URIRef] = set()
    for prop in (RDFS.subClassOf, RDFS.subPropertyOf, RDFS.range, RDFS.domain,
                 OWL.equivalentClass):
        referenced |= {o for o in g.objects(None, prop) if isinstance(o, URIRef)}
    for prop in (OWL.onProperty, OWL.allValuesFrom, OWL.someValuesFrom,
                 OWL.onClass, OWL.onDataRange):
        referenced |= {o for s, _, o in g.triples((None, prop, None))
                       if isinstance(s, BNode) and isinstance(o, URIRef)}
    builtin = (str(XSD), str(RDF), str(RDFS), str(OWL))
    return [
        f"{short(t)} is referenced but never declared — give it a type, a label and "
        f"a comment in the iteration that uses it"
        for t in sorted(referenced - declared, key=str)
        if not str(t).startswith(builtin)
    ]


CHECKS = (
    ("one comment per term and language", check_one_comment_per_language),
    ("every triple: term documented", check_own_terms_documented),
    ("no new global axioms on foreign terms", check_no_new_axioms_on_foreign_terms),
    ("every referenced term is declared", check_referenced_terms_declared),
)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "docs" / "triple" / "triple.ttl"
    if not path.exists():
        print(f"file non trovato: {path}")
        return 1

    g = Graph()
    g.parse(path, format="turtle")
    print(f"modello: {path.name} ({len(g)} triple, {len(terms(g))} termini)\n")

    failed = 0
    for name, check in CHECKS:
        problems = check(g)
        if problems:
            failed += len(problems)
            print(f"  FALLITO  {name} — {len(problems)} problemi")
            for p in problems:
                print(f"      {p}")
        else:
            print(f"  OK       {name}")

    print()
    if failed:
        print(f"{failed} problemi da correggere")
        return 1
    print("modello conforme agli invarianti")
    return 0


if __name__ == "__main__":
    sys.exit(main())
