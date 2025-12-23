import os
import re
import sys
import glob
from datetime import date
import rdflib
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, OWL

# Constants
VOCAB_DIR = "vocabularies/serializations/ttl"
BUILD_DIR = "build"
METADATA_FILE = "ontology/metadata.ttl"
BASE_URI = "https://gotriple.eu/ontology/triple"

# Namespaces
DCTERMS = Namespace("http://purl.org/dc/terms/")
VANN = Namespace("http://purl.org/vocab/vann/")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

def load_shared_metadata():
    """Loads shared metadata from the central metadata file."""
    g = Graph()
    g.parse(METADATA_FILE, format="ttl")
    
    metadata = {}
    
    # We expect the subject to be the ontology URI
    # But we can just query for the owl:Ontology
    
    ontology_node = None
    for s, p, o in g.triples((None, RDF.type, OWL.Ontology)):
        ontology_node = s
        break
    
    if not ontology_node:
        print(f"Error: No owl:Ontology found in {METADATA_FILE}")
        sys.exit(1)

    # Properties to copy
    properties_to_copy = [
        DCTERMS.publisher,
        DCTERMS.license,
        DCTERMS.creator,
        DCTERMS.contributor,
        OWL.versionInfo,
        VANN.preferredNamespaceUri, # We might want to customize this per vocab, but base is good
        RDFS.comment # Base comment
    ]
    
    for p in properties_to_copy:
        objs = list(g.objects(ontology_node, p))
        if objs:
            metadata[p] = objs
            
    return metadata

def validate_file(filepath):
    """Validates a TTL file using rdflib."""
    g = Graph()
    try:
        g.parse(filepath, format="ttl")
        print(f"✅ [VALID] {filepath}")
        return True
    except Exception as e:
        print(f"❌ [INVALID] {filepath}")
        print(e)
        return False

def generate_header_string(vocab_name, shared_metadata):
    """Generates the Turtle string for the owl:Ontology header."""
    
    uri = f"{BASE_URI}/{vocab_name}"
    title = f"TRIPLE Ontology - {vocab_name} Vocabulary"
    
    # Start building string
    header = f"<{uri}> a owl:Ontology ;\n"
    header += f'    dcterms:title "{title}"@en ;\n'
    header += f'    rdfs:label "{title}"@en ;\n'
    
    # Add shared metadata
    for p, objs in shared_metadata.items():
        predicate_qname = ""
        if p == DCTERMS.publisher: predicate_qname = "dcterms:publisher"
        elif p == DCTERMS.license: predicate_qname = "dcterms:license"
        elif p == DCTERMS.creator: predicate_qname = "dcterms:creator"
        elif p == DCTERMS.contributor: predicate_qname = "dcterms:contributor"
        elif p == OWL.versionInfo: predicate_qname = "owl:versionInfo"
        elif p == RDFS.comment: predicate_qname = "rdfs:comment"
        
        if not predicate_qname: continue 

        # Format objects
        obj_strs = []
        for obj in objs:
            if isinstance(obj, URIRef):
                obj_strs.append(f"<{str(obj)}>")
            elif isinstance(obj, Literal):
                # Simple crude formatting
                if obj.language:
                    obj_strs.append(f'"{obj}"@{obj.language}')
                elif obj.datatype:
                     obj_strs.append(f'"{obj}"^^{obj.datatype.n3()}')
                else:
                    obj_strs.append(f'"{obj}"')
        
        if obj_strs:
            header += f"    {predicate_qname} {', '.join(obj_strs)} ;\n"

    # Add dynamic dates
    today = date.today().isoformat()
    header += f'    dcterms:created "2021-12-01"^^xsd:date ;\n' # Keep original creation? Or make dynamic? Let's fix it for now or assume replacement.
    header += f'    dcterms:modified "{today}"^^xsd:date ;\n'
    
    # VANN
    header += f'    vann:preferredNamespacePrefix "{vocab_name.lower()}" ;\n' # deriving prefix from vocab name
    header += f'    vann:preferredNamespaceUri "{uri}#" .\n'
    
    return header

def process_file(filepath, shared_metadata):
    """Reads source, updates header, and writes to build directory."""
    with open(filepath, 'r') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    vocab_name = os.path.splitext(filename)[0]
    dest_path = os.path.join(BUILD_DIR, filename)

    new_header = generate_header_string(vocab_name, shared_metadata)
    
    # Ensure required prefixes exist
    required_prefixes = {
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "vann": "http://purl.org/vocab/vann/",
        "dcterms": "http://purl.org/dc/terms/",
        "owl": "http://www.w3.org/2002/07/owl#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
    }
    
    prefix_block = ""
    for prefix, uri in required_prefixes.items():
        if f"@prefix {prefix}:" not in content:
            # print(f"   Injecting missing prefix: {prefix}")
            prefix_block += f"@prefix {prefix}: <{uri}> .\n"
            
    if prefix_block:
        content = prefix_block + content
    
    # Line-based parser to find and remove existing header
    lines = content.splitlines(keepends=True)
    start_idx = -1
    end_idx = -1
    
    # 1. Find Start
    for i, line in enumerate(lines):
        if " a owl:Ontology" in line:
            start_idx = i
            break
            
    if start_idx != -1:
        # print(f"   Refactoring existing header in {filename}")
        # 2. Find End (line ending with . ignoring whitespace)
        for i in range(start_idx, len(lines)):
            stripped = lines[i].strip()
            if stripped.endswith("."):
                end_idx = i
                break
        
        if end_idx != -1:
            updated_content = "".join(lines[:start_idx]) + new_header + "\n" + "".join(lines[end_idx+1:])
        else:
             print(f"⚠️  Could not find end of header block in {filename}. Skipping replacement.")
             updated_content = content
    else:
        # print(f"   Injecting new header in {filename}")
        last_prefix_idx = -1
        for i, line in enumerate(lines):
            if line.strip().startswith("@prefix") and line.strip().endswith("."):
                last_prefix_idx = i
                
        if last_prefix_idx != -1:
            updated_content = "".join(lines[:last_prefix_idx+1]) + "\n" + new_header + "\n" + "".join(lines[last_prefix_idx+1:])
        else:
            updated_content = new_header + "\n" + content

    with open(dest_path, 'w') as f:
        f.write(updated_content)
        
    return dest_path

def main():
    print("🚀 Starting Build Script...")
    
    # 0. Create Build Dir
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
        print(f"📂 Created build directory: {BUILD_DIR}")
    
    # 1. Load Metadata
    print("📂 Loading Metadata...")
    shared_metadata = load_shared_metadata()
    
    # 2. Process Files
    print(f"📂 Processing vocabularies from {VOCAB_DIR} to {BUILD_DIR}...")
    files = glob.glob(os.path.join(VOCAB_DIR, "*.ttl"))
    
    success_count = 0
    fail_count = 0
    
    for filepath in files:
        # print(f"🔄 Processing {os.path.basename(filepath)}...")
        
        # Process and write to build/
        dest_path = process_file(filepath, shared_metadata)
        
        # Validate the *Artifact* in build/
        if validate_file(dest_path):
            success_count += 1
        else:
            print(f"⚠️  Build artifact invalid: {dest_path}")
            fail_count += 1
            
    print(f"\n🎉 Build Complete. Success: {success_count}, Failed: {fail_count}")

if __name__ == "__main__":
    main()
