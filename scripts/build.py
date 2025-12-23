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
        RDFS.comment, # Base comment
        DCTERMS.abstract
    ]
    
    for p in properties_to_copy:
        objs = list(g.objects(ontology_node, p))
        if objs:
            metadata[p] = objs
            
    return metadata

def get_or_create_local_metadata(vocab_path, vocab_name):
    """Gets local metadata from sidecar file, creating it if missing."""
    metadata_path = vocab_path.replace(".ttl", ".metadata.ttl")
    
    if not os.path.exists(metadata_path):
        print(f"   ✨ Creating default metadata sidecar: {os.path.basename(metadata_path)}")
        
        default_uri = f"{BASE_URI}/{vocab_name}"
        default_title = f"TRIPLE Ontology - {vocab_name} Vocabulary"
        default_desc = f"Vocabulary defining {vocab_name} concepts for the TRIPLE platform."
        default_prefix = vocab_name.lower()
        
        # Create default TTL
        ttl_content = f"""@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix vann: <http://purl.org/vocab/vann/> .

<{default_uri}> a owl:Ontology ;
    dcterms:title "{default_title}"@en ;
    rdfs:label "{default_title}"@en ;
    dcterms:description "{default_desc}"@en ;
    dcterms:abstract "Abstract for {vocab_name} vocabulary."@en ;
    vann:preferredNamespacePrefix "{default_prefix}" ;
    vann:preferredNamespaceUri "{default_uri}#" .
"""
        with open(metadata_path, 'w') as f:
            f.write(ttl_content)
            
    # Load it
    g = Graph()
    g.parse(metadata_path, format="ttl")
    
    metadata = {}
    
    ontology_node = None
    for s, p, o in g.triples((None, RDF.type, OWL.Ontology)):
        ontology_node = s
        break
        
    if not ontology_node:
        print(f"⚠️  Warning: No owl:Ontology in {os.path.basename(metadata_path)}")
        return {}

    # Read everything on the ontology node
    for s, p, o in g.triples((ontology_node, None, None)):
        if p == RDF.type: continue
        if p not in metadata: metadata[p] = []
        metadata[p].append(o)
        
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

def generate_header_string(vocab_name, shared_metadata, local_metadata):
    """Generates the Turtle string for the owl:Ontology header."""
    
    uri = f"{BASE_URI}/{vocab_name}"
    
    # Start building string
    header = f"<{uri}> a owl:Ontology ;\n"
    
    # Merge metadata: Local overrides Shared
    # We want to use all keys from both
    all_keys = set(shared_metadata.keys()) | set(local_metadata.keys())
    
    # Helper to mapping predicate to QName string
    pred_map = {
        DCTERMS.publisher: "dcterms:publisher",
        DCTERMS.license: "dcterms:license",
        DCTERMS.creator: "dcterms:creator",
        DCTERMS.contributor: "dcterms:contributor",
        OWL.versionInfo: "owl:versionInfo",
        RDFS.comment: "rdfs:comment",
        DCTERMS.title: "dcterms:title",
        RDFS.label: "rdfs:label",
        DCTERMS.description: "dcterms:description",
        DCTERMS.abstract: "dcterms:abstract",
        VANN.preferredNamespacePrefix: "vann:preferredNamespacePrefix",
        VANN.preferredNamespaceUri: "vann:preferredNamespaceUri"
    }
    
    # Process known predicates in a specific order for better readability
    ordered_preds = [
        DCTERMS.title, RDFS.label, DCTERMS.description, DCTERMS.abstract,
        DCTERMS.publisher, DCTERMS.license, 
        DCTERMS.creator, DCTERMS.contributor, 
        OWL.versionInfo, RDFS.comment,
        VANN.preferredNamespacePrefix, VANN.preferredNamespaceUri
    ]
    
    # Add any others at the end
    for k in all_keys:
        if k not in ordered_preds:
            ordered_preds.append(k)
            
    for p in ordered_preds:
        # Get values: Local first, then Shared
        if p in local_metadata:
            objs = local_metadata[p]
        elif p in shared_metadata:
            objs = shared_metadata[p]
        else:
            continue
            
        # Get QName
        if p in pred_map:
            predicate_qname = pred_map[p]
        else:
            # Fallback for unknown predicates: use full URI or try to qname it if simple
            predicate_qname = f"<{str(p)}>"

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
                     # Check if it's xsd
                     if str(obj.datatype).startswith("http://www.w3.org/2001/XMLSchema#"):
                         dtype = str(obj.datatype).replace("http://www.w3.org/2001/XMLSchema#", "xsd:")
                         obj_strs.append(f'"{obj}"^^{dtype}')
                     else:
                         obj_strs.append(f'"{obj}"^^{obj.datatype.n3()}')
                else:
                    obj_strs.append(f'"{obj}"')
        
        if obj_strs:
            header += f"    {predicate_qname} {', '.join(obj_strs)} ;\n"

    # Add dynamic dates
    today = date.today().isoformat()
    # Check if dates are already in metadata? Ideally yes, but let's enforce modification date
    header += f'    dcterms:created "2021-12-01"^^xsd:date ;\n' 
    header += f'    dcterms:modified "{today}"^^xsd:date .\n'
    
    return header

def process_file(filepath, shared_metadata):
    """Reads source, updates header, and writes to build directory."""
    with open(filepath, 'r') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    vocab_name = os.path.splitext(filename)[0]
    dest_path = os.path.join(BUILD_DIR, filename)

    # Load local metadata
    local_metadata = get_or_create_local_metadata(filepath, vocab_name)

    new_header = generate_header_string(vocab_name, shared_metadata, local_metadata)
    
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
    
    # 0. Create/Clean Build Dir
    if os.path.exists(BUILD_DIR):
        # Clean existing files
        for f in glob.glob(os.path.join(BUILD_DIR, "*")):
            os.remove(f)
        print(f"🧹 Cleaned build directory: {BUILD_DIR}")
    else:
        os.makedirs(BUILD_DIR)
        print(f"📂 Created build directory: {BUILD_DIR}")
    
    # 1. Load Metadata
    print("📂 Loading Metadata...")
    shared_metadata = load_shared_metadata()
    
    # 2. Process Files
    print(f"📂 Processing vocabularies from {VOCAB_DIR} to {BUILD_DIR}...")
    all_files = glob.glob(os.path.join(VOCAB_DIR, "*.ttl"))
    # Exclude metadata files
    files = [f for f in all_files if not f.endswith(".metadata.ttl") and not f.endswith(".metadata.metadata.ttl")]
    
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
