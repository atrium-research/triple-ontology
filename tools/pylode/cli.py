import os
import shutil
import click
from jinja2 import Environment, FileSystemLoader, select_autoescape
from .parser import OntologyParser

@click.command()
@click.argument('input_path')
@click.option('--output', '-o', default='output.html', help='Output file or directory path.')
@click.option('--css', default=None, help='Path to custom CSS.')
@click.option('--sections', 'sections_dir', default=None,
              help='Directory of numbered markdown chapter files (front-matter: title, terms).')
@click.option('--figures', 'figures_dir', default=None,
              help='Directory of per-term Graffoo diagrams, named {anchor}.png (":" becomes "-").')
def main(input_path, output, css, sections_dir, figures_dir):
    """LODE: Live OWL Documentation Environment (Python Port)."""
    
    click.echo(f"Parsing ontology from {input_path}...")
    parser = OntologyParser(input_path)
    
    metadata = parser.get_metadata()
    classes = parser.get_classes()
    object_properties = parser.get_object_properties()
    datatype_properties = parser.get_datatype_properties()
    annotation_properties = parser.get_annotation_properties()
    individuals = parser.get_named_individuals()
    namespaces = parser.get_namespaces()
    
    click.echo(f"Found {len(classes)} classes, {len(object_properties)} obj props, {len(datatype_properties)} data props, {len(individuals)} individuals, {len(namespaces)} namespaces.")

    if figures_dir:
        n_fig = 0
        for el in classes + object_properties + datatype_properties + annotation_properties + individuals:
            if not el.anchor:
                continue
            base = el.anchor.replace(":", "-")
            for ext in (".svg", ".png"):
                if os.path.exists(os.path.join(figures_dir, base + ext)):
                    el.figure = "figures/" + base + ext
                    n_fig += 1
                    break
        click.echo(f"Figures: {n_fig} terms have a diagram")

    sections = []
    if sections_dir:
        from .sections import load_sections
        sections = load_sections(sections_dir)
        lookup = {}
        for el in classes + object_properties + datatype_properties + annotation_properties + individuals:
            if el.anchor:
                lookup[el.anchor] = el
            lookup[el.uri] = el
        covered = set()
        for sec in sections:
            sec["elements"] = []
            for term in sec["terms"]:
                el = lookup.get(term)
                if el is None:
                    click.echo(f"WARNING: chapter '{sec['title']}': term '{term}' not found in the ontology")
                else:
                    sec["elements"].append(el)
                    covered.add(el.uri)
        for n, sec in enumerate(sections, 1):
            for el in sec["elements"]:
                if el.chapter is None:
                    el.chapter = {"n": n, "title": sec["title"], "slug": sec["slug"]}
        total = len(classes) + len(object_properties) + len(datatype_properties) + len(annotation_properties) + len(individuals)
        click.echo(f"Chapters: {len(sections)}; terms referenced by a chapter: {len(covered)}/{total}")

    env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
        autoescape=select_autoescape()
    )
    
    template = env.get_template("base.html")
    
    html = template.render(
        sections=sections,
        metadata=metadata,
        classes=classes,
        object_properties=object_properties,
        datatype_properties=datatype_properties,
        annotation_properties=annotation_properties,
        individuals=individuals,
        namespaces=namespaces,
        css_path="static/css/" # Simplified for now
    )
    
    # Handle Output Directory and Assets
    output_path = os.path.abspath(output)
    
    # Check if output looks like a directory or file
    # User request: "il risultato della serializzazione vorrei che fosse index.html"
    # Logic: if output path does not end in .html, treat as dir and append index.html
    if not output.lower().endswith('.html'):
        output_dir = output_path
        output_filename = "index.html"
        html_output_path = os.path.join(output_dir, output_filename)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    else:
        output_dir = os.path.dirname(output_path)
        if not output_dir:
            output_dir = os.getcwd() # local dir
        html_output_path = output_path
        output_filename = os.path.basename(html_output_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(html_output_path, 'w') as f:
        f.write(html)

    if figures_dir and os.path.isdir(figures_dir):
        shutil.copytree(figures_dir, os.path.join(output_dir, 'figures'), dirs_exist_ok=True)

    # Copy Static Assets
    click.echo("Copying static assets...")
    module_dir = os.path.dirname(__file__)
    src_static = os.path.join(module_dir, 'templates', 'static')
    dst_static = os.path.join(output_dir, 'static')
    
    if os.path.exists(src_static):
        shutil.copytree(src_static, dst_static, dirs_exist_ok=True)
    else:
        click.echo(f"Warning: Static assets not found at {src_static}")

    # Serialization logic
    # 1. ontology.ttl (Copy of source if possible, to preserve formatting/comments)
    # If input is not TTL, we might want to serialize, but assuming input is TTL for now based on context.
    dst_ttl = os.path.join(output_dir, "ontology.ttl")
    if input_path.lower().endswith('.ttl'):
        shutil.copy2(input_path, dst_ttl)
        click.echo(f"Copied source to {dst_ttl}")
    else:
        # Fallback: serialize if input wasn't TTL
        parser.graph.serialize(destination=dst_ttl, format='turtle')
        click.echo(f"Serialized to {dst_ttl}")

    # 2. ontology.jsonld
    dst_jsonld = os.path.join(output_dir, "ontology.jsonld")
    click.echo(f"Serializing to JSON-LD: {dst_jsonld}")
    parser.graph.serialize(destination=dst_jsonld, format='json-ld')

    # 3. ontology.rdf (RDF/XML)
    dst_rdf = os.path.join(output_dir, "ontology.rdf")
    click.echo(f"Serializing to RDF/XML: {dst_rdf}")
    parser.graph.serialize(destination=dst_rdf, format='xml')

    click.echo(f"Documentation generated at {html_output_path}")

if __name__ == '__main__':
    main()
