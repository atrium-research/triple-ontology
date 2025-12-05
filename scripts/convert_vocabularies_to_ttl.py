#!/usr/bin/env python3
"""
Script to convert RDF/XML vocabulary files to Turtle (TTL) format.

This script converts all vocabulary files from the vocabularies/ directory
(in RDF/XML format) to Turtle format, maintaining the original structure
and metadata while providing a more readable serialization.

Usage:
    python convert_vocabularies_to_ttl.py [--output-dir OUTPUT_DIR]

Requirements:
    - rdflib
"""

import os
import sys
import argparse
from pathlib import Path
from rdflib import Graph
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def convert_rdf_to_ttl(input_file: Path, output_file: Path) -> bool:
    """
    Convert a single RDF/XML file to Turtle format.
    
    Args:
        input_file: Path to the input RDF/XML file
        output_file: Path to the output TTL file
        
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Create RDF graph
        g = Graph()
        
        # Parse the input RDF/XML file
        logger.info(f"Reading RDF/XML file: {input_file}")
        g.parse(input_file, format="xml")
        
        # Add header comment
        vocabulary_name = input_file.stem
        header_comment = f"""# TRIPLE Ontology - {vocabulary_name.title()} Vocabulary
# Converted from RDF/XML to Turtle format
# Original file: {input_file.name}
# License: CC BY 4.0
# Website: https://gotriple.eu/ontology/triple

"""
        
        # Serialize to Turtle format
        logger.info(f"Writing Turtle file: {output_file}")
        ttl_content = g.serialize(format="turtle")
        
        # Write with header comment
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(header_comment)
            f.write(ttl_content)
            
        logger.info(f"Successfully converted {input_file.name} to {output_file.name}")
        return True
        
    except Exception as e:
        logger.error(f"Error converting {input_file}: {e}")
        return False

def main():
    """Main function to convert all vocabulary files."""
    parser = argparse.ArgumentParser(description='Convert RDF/XML vocabulary files to Turtle format')
    parser.add_argument('--output-dir', '-o', 
                       default='vocabularies_ttl',
                       help='Output directory for TTL files (default: vocabularies_ttl)')
    parser.add_argument('--input-dir', '-i',
                       default='vocabularies', 
                       help='Input directory with RDF files (default: vocabularies)')
    
    args = parser.parse_args()
    
    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Set up paths
    input_dir = project_root / args.input_dir
    output_dir = project_root / args.output_dir
    
    # Validate input directory
    if not input_dir.exists():
        logger.error(f"Input directory does not exist: {input_dir}")
        sys.exit(1)
        
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    logger.info(f"Output directory: {output_dir}")
    
    # Find all RDF files
    rdf_files = list(input_dir.glob("*.rdf"))
    if not rdf_files:
        logger.warning(f"No .rdf files found in {input_dir}")
        return
        
    logger.info(f"Found {len(rdf_files)} RDF files to convert")
    
    # Convert each file
    successful_conversions = 0
    failed_conversions = 0
    
    for rdf_file in rdf_files:
        # Create output filename
        ttl_filename = rdf_file.stem + '.ttl'
        ttl_file = output_dir / ttl_filename
        
        # Convert file
        if convert_rdf_to_ttl(rdf_file, ttl_file):
            successful_conversions += 1
        else:
            failed_conversions += 1
    
    # Print summary
    logger.info(f"Conversion complete:")
    logger.info(f"  Successfully converted: {successful_conversions} files")
    if failed_conversions > 0:
        logger.error(f"  Failed conversions: {failed_conversions} files")
    
    if failed_conversions > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()