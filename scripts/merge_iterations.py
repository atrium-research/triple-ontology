#!/usr/bin/env python3
"""
TRIPLE Ontology Merger

This script merges all TBOX.ttl files from the development iterations
into a single consolidated ontology file (structure only, no instance data).

Usage:
    python merge_iterations.py [--output OUTPUT_FILE]

Arguments:
    --output    Output file path (default: ../ontology/triple-ontology.ttl)
"""

import argparse
import sys
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal
from rdflib.namespace import SKOS, DCTERMS, FOAF
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_development_dir():
    """Get the development directory path."""
    script_dir = Path(__file__).parent
    dev_dir = script_dir.parent / 'development'

    if not dev_dir.exists():
        logger.error(f"Development directory not found: {dev_dir}")
        sys.exit(1)

    return dev_dir


def find_ttl_files(dev_dir):
    """Find all TBOX.ttl files in iteration directories (structure only)."""
    ttl_files = []

    # Get all iteration directories (sorted numerically)
    iteration_dirs = sorted([d for d in dev_dir.iterdir() if d.is_dir()],
                          key=lambda x: int(x.name) if x.name.isdigit() else 0)

    for iteration_dir in iteration_dirs:
        # Check for TBOX.ttl only
        tbox = iteration_dir / 'TBOX.ttl'
        if tbox.exists():
            ttl_files.append(('TBOX', iteration_dir.name, tbox))
            logger.info(f"Found: {iteration_dir.name}/TBOX.ttl")

    return ttl_files


def merge_graphs(ttl_files):
    """Merge all TTL files into a single RDF graph."""
    logger.info("Creating merged graph...")
    merged_graph = Graph()

    # Define common namespaces
    TRIPLE = Namespace("https://gotriple.eu/ontology/triple#")
    SCHEMA = Namespace("http://schema.org/")
    DATACITE = Namespace("http://purl.org/spar/datacite/")
    LITRE = Namespace("http://purl.org/spar/literal/")
    DC = Namespace("http://purl.org/dc/elements/1.1/")

    # Bind namespaces
    merged_graph.bind("triple", TRIPLE)
    merged_graph.bind("schema", SCHEMA)
    merged_graph.bind("skos", SKOS)
    merged_graph.bind("foaf", FOAF)
    merged_graph.bind("dc", DC)
    merged_graph.bind("dcterms", DCTERMS)
    merged_graph.bind("datacite", DATACITE)
    merged_graph.bind("litre", LITRE)
    merged_graph.bind("owl", OWL)
    merged_graph.bind("rdf", RDF)
    merged_graph.bind("rdfs", RDFS)

    # Load and merge each file
    for file_type, iteration, file_path in ttl_files:
        try:
            logger.info(f"Loading {iteration}/{file_type}.ttl...")
            temp_graph = Graph()
            temp_graph.parse(file_path, format='turtle')

            # Add all triples to merged graph
            for triple in temp_graph:
                merged_graph.add(triple)

            logger.info(f"  Added {len(temp_graph)} triples from {iteration}/{file_type}.ttl")

        except Exception as e:
            logger.error(f"Error loading {file_path}: {e}")

    logger.info(f"Total triples in merged graph: {len(merged_graph)}")
    return merged_graph


def add_metadata(graph):
    """Add ontology metadata to the merged graph."""
    logger.info("Adding ontology metadata...")

    TRIPLE_ONT = Namespace("https://gotriple.eu/ontology/triple")

    # Add ontology declaration
    graph.add((TRIPLE_ONT[""], RDF.type, OWL.Ontology))
    graph.add((TRIPLE_ONT[""], OWL.versionIRI,
              Literal("https://gotriple.eu/ontology/triple/1.0.0")))
    graph.add((TRIPLE_ONT[""], RDFS.label,
              Literal("TRIPLE Ontology", lang="en")))
    graph.add((TRIPLE_ONT[""], RDFS.comment,
              Literal("Comprehensive semantic representation of the GoTriple discovery platform's data model for Social Sciences and Humanities (SSH) research artifacts.", lang="en")))
    graph.add((TRIPLE_ONT[""], DCTERMS.created,
              Literal("2025-10-06")))
    graph.add((TRIPLE_ONT[""], DCTERMS.modified,
              Literal("2025-10-06")))

    return graph


def save_ontology(graph, output_path):
    """Save the merged graph to a Turtle file."""
    logger.info(f"Saving merged ontology to: {output_path}")

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        graph.serialize(destination=str(output_path), format='turtle')
        logger.info(f"Successfully saved ontology with {len(graph)} triples")
        return True

    except Exception as e:
        logger.error(f"Error saving ontology: {e}")
        return False


def print_statistics(graph):
    """Print statistics about the merged ontology."""
    logger.info("\n=== Ontology Statistics (TBOX Only) ===")

    # Count classes
    classes = set(graph.subjects(RDF.type, OWL.Class)) | \
              set(graph.subjects(RDF.type, RDFS.Class))
    logger.info(f"Classes: {len(classes)}")

    # Count object properties
    obj_props = set(graph.subjects(RDF.type, OWL.ObjectProperty))
    logger.info(f"Object Properties: {len(obj_props)}")

    # Count data properties
    data_props = set(graph.subjects(RDF.type, OWL.DatatypeProperty))
    logger.info(f"Data Properties: {len(data_props)}")

    logger.info(f"Total Triples: {len(graph)}")
    logger.info("=======================================\n")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Merge TRIPLE ontology iterations into a single file.'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path(__file__).parent.parent / 'ontology' / 'triple-ontology.ttl',
        help='Output file path (default: ../ontology/triple-ontology.ttl)'
    )

    args = parser.parse_args()

    logger.info("=== TRIPLE Ontology Merger ===\n")

    # Get development directory
    dev_dir = get_development_dir()
    logger.info(f"Development directory: {dev_dir}\n")

    # Find all TTL files
    ttl_files = find_ttl_files(dev_dir)

    if not ttl_files:
        logger.error("No TTL files found!")
        sys.exit(1)

    logger.info(f"\nFound {len(ttl_files)} TTL files\n")

    # Merge graphs
    merged_graph = merge_graphs(ttl_files)

    # Add metadata
    merged_graph = add_metadata(merged_graph)

    # Print statistics
    print_statistics(merged_graph)

    # Save ontology
    if save_ontology(merged_graph, args.output):
        logger.info(f"\n✓ Ontology successfully saved to: {args.output}")
        return 0
    else:
        logger.error("\n✗ Failed to save ontology")
        return 1


if __name__ == '__main__':
    sys.exit(main())
