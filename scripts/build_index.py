#!/usr/bin/env python3
"""Generate the landing page of https://gotriple.eu/ontology/ — one card per
published artefact (the consolidated model plus the six controlled vocabularies).

Everything on the page (titles, descriptions, versions, term counts) is read from
the same inputs the documentation pages are rendered from — ontology/triple.ttl
and the compiled vocabularies in build/ — so the index can never go stale.

Driven by scripts/build_docs.sh (after build.py has refreshed build/); can also
be run alone:

    python scripts/build_index.py -o build/docs-preview/index.html
"""
import argparse
import html
import os
import re
import sys

from rdflib import Graph, RDF, OWL, URIRef
from rdflib.namespace import DCTERMS, SKOS, Namespace

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VANN = Namespace("http://purl.org/vocab/vann/")

# Card links are absolute on the canonical domain (the same form as the IRIs);
# only the stylesheets stay relative, so the preview renders offline too.
BASE = "https://gotriple.eu/ontology/"

MODEL_TTL = os.path.join(REPO, "ontology", "triple.ttl")
BUILD_DIR = os.path.join(REPO, "build")

# Display order of the vocabulary cards (compiled file base names).
VOCABULARIES = ["Discipline", "ContentType", "ConditionOfAccess",
                "License", "ProjectType", "ddc"]


def kebab(name):
    """CamelCase file name -> kebab-case directory (same rule as build.py)."""
    return re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()


def ontology_node(g):
    for s in g.subjects(RDF.type, OWL.Ontology):
        return s
    sys.exit("No owl:Ontology node found")


def first(g, s, p):
    for o in g.objects(s, p):
        return str(o)
    return ""


def model_card():
    g = Graph()
    g.parse(MODEL_TTL, format="turtle")
    node = ontology_node(g)
    ns = "https://gotriple.eu/ontology/triple/"

    def count(t):
        return sum(1 for x in g.subjects(RDF.type, t)
                   if isinstance(x, URIRef) and str(x).startswith(ns))

    n_classes = count(OWL.Class)
    n_props = (count(OWL.ObjectProperty) + count(OWL.DatatypeProperty)
               + count(OWL.AnnotationProperty))
    n_ind = count(OWL.NamedIndividual)
    return {
        "kind": "Model",
        "title": first(g, node, DCTERMS.title) or "TRIPLE Ontology",
        "iri": ns,
        "href": "triple",
        "desc": first(g, node, DCTERMS.abstract) or first(g, node, DCTERMS.description),
        "version": first(g, node, OWL.versionInfo),
        "chips": [f"{n_classes} classes", f"{n_props} properties",
                  f"{n_ind} identifier schemes"],
    }


def vocabulary_card(name):
    path = os.path.join(BUILD_DIR, name + ".ttl")
    g = Graph()
    g.parse(path, format="turtle")
    node = ontology_node(g)
    ns = first(g, node, VANN.preferredNamespaceUri)
    schemes = set(g.subjects(RDF.type, SKOS.ConceptScheme))
    n_concepts = sum(1 for x in set(g.subjects(RDF.type, OWL.NamedIndividual))
                     if isinstance(x, URIRef) and str(x).startswith(ns)
                     and x not in schemes)
    return {
        "kind": "Controlled vocabulary",
        "title": first(g, node, DCTERMS.title) or name,
        "iri": ns,
        "href": kebab(name),
        "desc": first(g, node, DCTERMS.abstract) or first(g, node, DCTERMS.description),
        "version": first(g, node, OWL.versionInfo),
        "chips": [f"{n_concepts} concepts"],
    }


def render_card(c, model=False):
    e = html.escape
    url = BASE + c["href"]
    chips = "".join(f'<span class="chip">{e(t)}</span>' for t in c["chips"])
    return f"""    <div class="card{' model' if model else ''}">
      <p class="card-head"><span class="kind">{e(c['kind'])}</span><span class="version">v{e(c['version'])}</span></p>
      <h2><a href="{e(url)}">{e(c['title'])}</a></h2>
      <p class="iri">{e(c['iri'])}</p>
      <p class="desc">{e(c['desc'])}</p>
      <p class="stats">{chips}</p>
      <p class="links"><a class="btn btn-doc" href="{e(url)}">Documentation</a><a
         class="btn" href="{e(url)}/ontology.ttl">Turtle</a><a
         class="btn" href="{e(url)}/ontology.rdf">RDF/XML</a><a
         class="btn" href="{e(url)}/ontology.jsonld">JSON-LD</a></p>
    </div>"""


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TRIPLE Ontology</title>
<!-- Same stylesheets as the documentation pages, in the same order (the landing
     has its own static/ beside it): the page belongs to the same family. These
     relative links require the trailing-slash URL /ontology/ (see docs/README.md,
     resolution rules); every other link on the page is absolute on the canonical
     domain. -->
<link href="static/owl.css" rel="stylesheet" type="text/css" />
<link href="static/yeti.css" rel="stylesheet" type="text/css" />
<link href="static/rec.css" rel="stylesheet" type="text/css" />
<link href="static/extra.css" rel="stylesheet" type="text/css" />
<style>
  /* Landing-only layout; every color is a documentation-page ingredient
     (navy borders like .entity, #F4FFFF like .hlist, headings from rec.css). */
  .subtitle {{ margin-top: 0; }}
  .intro {{ max-width: 60em; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
           gap: 16px; margin-top: 1.5em; }}
  .card {{ display: flex; flex-direction: column; border: 1px solid navy;
           background: #fff; padding: 14px 18px 16px; }}
  .card.model {{ grid-column: 1 / -1; }}
  .card-head {{ display: flex; justify-content: space-between; margin: 0; }}
  .kind {{ font-size: .72em; letter-spacing: .08em; text-transform: uppercase;
           color: #777; }}
  .version {{ font-size: .78em; color: #777; }}
  .card h2 {{ font-size: 1.3em; margin: .1em 0 .4em; padding-bottom: .25em;
              border-bottom: 1px solid navy; }}
  .iri {{ font-family: monospace, monospace; font-size: .85em; color: #666;
          word-break: break-all; margin: 0 0 .6em; }}
  .desc {{ margin: 0 0 .9em; flex: 1; }}
  .stats {{ margin: 0 0 .9em; }}
  .chip {{ display: inline-block; border: 1px solid navy; background: #F4FFFF;
           border-radius: 10px; padding: 0 .6em; font-size: .78em;
           margin: 0 .35em .35em 0; }}
  .links {{ margin: 0; display: flex; flex-wrap: wrap; gap: 6px; }}
  .links .btn {{ border: 1px solid navy; border-radius: 3px; padding: 2px 10px;
                 font-size: .85em; background: #F4FFFF; }}
  .links .btn:hover {{ background: #fff; }}
  .links .btn-doc {{ background: navy; color: #fff; }}
  .links .btn-doc:hover {{ background: #005A9C; color: #fff; }}
</style>
</head>
<body>
<div class="container">
  <h1>The TRIPLE Ontology</h1>
  <p class="subtitle">Version {version} &middot; the data model of the
     <a href="https://www.gotriple.eu/">GoTriple</a> discovery platform</p>
  <p class="intro">{abstract}
     The model and its six controlled vocabularies are published here as separate
     artefacts: each resolves at its IRI with content negotiation &mdash; HTML
     documentation for browsers, Turtle / RDF-XML / JSON-LD for semantic clients.
     Development happens on
     <a href="https://github.com/atrium-research/triple-ontology">GitHub</a>,
     where every release is archived.</p>
  <div class="grid">
{cards}
  </div>
</div>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--output", required=True, help="Output HTML file path.")
    args = ap.parse_args()

    model = model_card()
    cards = [render_card(model, model=True)]
    cards += [render_card(vocabulary_card(v)) for v in VOCABULARIES]

    page = PAGE.format(version=html.escape(model["version"]),
                       abstract=html.escape(model["desc"]),
                       cards="\n".join(cards))
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        f.write(page)
    print(f"Landing index generated at {args.output} "
          f"({1 + len(VOCABULARIES)} cards)")


if __name__ == "__main__":
    main()
