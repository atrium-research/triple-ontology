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
from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, URIRef, BNode
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


def normalize_restriction(graph, restriction_node):
    """
    Create a normalized representation of an OWL restriction for deduplication.
    Returns a tuple representing the restriction's structure.
    """
    restriction_type = None
    property_uri = None
    value_constraint = None
    cardinality = None
    cardinality_type = None
    
    # Get the restriction type and property
    for p, o in graph.predicate_objects(restriction_node):
        if p == OWL.onProperty:
            property_uri = str(o)
        elif p == OWL.allValuesFrom:
            restriction_type = "allValuesFrom"
            value_constraint = str(o)
        elif p == OWL.someValuesFrom:
            restriction_type = "someValuesFrom"
            value_constraint = str(o)
        elif p == OWL.hasValue:
            restriction_type = "hasValue"
            value_constraint = str(o)
        elif p == OWL.minCardinality:
            cardinality_type = "minCardinality"
            cardinality = str(o)
        elif p == OWL.maxCardinality:
            cardinality_type = "maxCardinality"
            cardinality = str(o)
        elif p == OWL.cardinality:
            cardinality_type = "cardinality"
            cardinality = str(o)
        elif p == OWL.qualifiedCardinality:
            cardinality_type = "qualifiedCardinality"
            cardinality = str(o)
        elif p == OWL.onClass:
            value_constraint = f"onClass:{str(o)}"
        elif p == OWL.onDataRange:
            value_constraint = f"onDataRange:{str(o)}"
    
    # Create a normalized tuple representation
    return (property_uri, restriction_type, value_constraint, cardinality_type, cardinality)


def deduplicate_restrictions(graph):
    """
    Remove duplicate restrictions from class definitions in the graph.
    """
    logger.info("Deduplicating identical restrictions...")
    
    # Find all classes that have rdfs:subClassOf relationships
    classes_with_restrictions = set()
    for s, p, o in graph.triples((None, RDFS.subClassOf, None)):
        if isinstance(o, URIRef) or (hasattr(o, 'concrete') and not o.concrete):
            # Skip non-restriction subclass relationships
            continue
        classes_with_restrictions.add(s)
    
    restrictions_removed = 0
    
    for class_uri in classes_with_restrictions:
        # Get all restrictions for this class
        restrictions = list(graph.objects(class_uri, RDFS.subClassOf))
        restriction_nodes = [r for r in restrictions if not isinstance(r, URIRef)]
        
        if len(restriction_nodes) < 2:
            continue  # No duplicates possible
        
        # Normalize restrictions and find duplicates
        normalized_restrictions = {}
        nodes_to_remove = []
        
        for restriction_node in restriction_nodes:
            # Check if this is actually a restriction
            if not (restriction_node, RDF.type, OWL.Restriction) in graph:
                continue
                
            normalized = normalize_restriction(graph, restriction_node)
            
            if normalized in normalized_restrictions:
                # This is a duplicate - mark the restriction node for removal
                nodes_to_remove.append(restriction_node)
                restrictions_removed += 1
                logger.info(f"  Found duplicate restriction on {class_uri}: {normalized}")
            else:
                normalized_restrictions[normalized] = restriction_node
        
        # Remove duplicate restriction triples
        for restriction_node in nodes_to_remove:
            # Remove the subClassOf relationship to this duplicate restriction
            graph.remove((class_uri, RDFS.subClassOf, restriction_node))
            
            # Remove all triples about this restriction node
            triples_to_remove = list(graph.triples((restriction_node, None, None)))
            for triple in triples_to_remove:
                graph.remove(triple)
    
    logger.info(f"Removed {restrictions_removed} duplicate restrictions")
    return graph


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
    SIOC = Namespace("http://rdfs.org/sioc/ns#")

    # Bind essential namespaces (let files define their own schema: prefix)
    merged_graph.bind("triple", TRIPLE)
    merged_graph.bind("skos", SKOS)
    merged_graph.bind("foaf", FOAF)
    merged_graph.bind("dc", DC)
    merged_graph.bind("dcterms", DCTERMS)
    merged_graph.bind("datacite", DATACITE)
    merged_graph.bind("litre", LITRE)
    merged_graph.bind("sioc", SIOC)
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

    # Add schema prefix after loading all files to avoid conflicts
    merged_graph.bind("schema", SCHEMA)
    
    logger.info(f"Total triples in merged graph before deduplication: {len(merged_graph)}")
    
    # Deduplicate identical restrictions
    merged_graph = deduplicate_restrictions(merged_graph)
    
    logger.info(f"Total triples in merged graph after deduplication: {len(merged_graph)}")
    return merged_graph


def add_metadata(graph):
    """Add ontology metadata to the merged graph."""
    logger.info("Adding ontology metadata...")

    TRIPLE_ONT = Namespace("https://gotriple.eu/ontology/triple")

    # Add ontology declaration
    graph.add((TRIPLE_ONT[""], RDF.type, OWL.Ontology))
    graph.add((TRIPLE_ONT[""], OWL.versionIRI,
              URIRef("https://gotriple.eu/ontology/triple/1.0.0")))
    graph.add((TRIPLE_ONT[""], RDFS.label,
              Literal("TRIPLE Ontology", lang="en")))
    graph.add((TRIPLE_ONT[""], RDFS.comment,
              Literal("Comprehensive semantic representation of the GoTriple discovery platform's data model for Social Sciences and Humanities (SSH) research artifacts.", lang="en")))
    graph.add((TRIPLE_ONT[""], OWL.versionInfo,
              Literal("1.0.0")))
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
        
        # Serialize to string first
        turtle_content = graph.serialize(format='turtle')
        
        # Fix schema1: prefix to schema:
        turtle_content = turtle_content.replace('@prefix schema1:', '@prefix schema:')
        turtle_content = turtle_content.replace('schema1:', 'schema:')
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(turtle_content)
            
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
