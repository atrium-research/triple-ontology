# TRIPLE Ontology Scripts

This directory contains utility scripts for working with the TRIPLE ontology.

## Setup

Install required dependencies:

```bash
pip install -r requirements.txt
```

Or using a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Scripts

### merge_iterations.py

Merges all TBOX.ttl files from development iterations into a single consolidated ontology file (structure only, no instance data).

**Usage:**

```bash
# Default output to ../ontology/triple-ontology.ttl
python merge_iterations.py

# Custom output path
python merge_iterations.py --output /path/to/output.ttl
```

**What it does:**

1. Scans all iteration directories in `development/`
2. Loads all TBOX.ttl files (ontology structure only)
3. Merges them into a single RDF graph (removing duplicates automatically)
4. Adds ontology metadata (version, labels, comments, dates)
5. Saves the consolidated ontology to `ontology/triple-ontology.ttl`
6. Prints statistics about the merged ontology

**Output includes:**

- All classes, properties, and restrictions from all iterations
- Proper namespace bindings
- Ontology metadata
- Statistics summary (classes, properties)
- **No instance data** (ABOX files are excluded)

**Example output:**

```
=== TRIPLE Ontology Merger ===

Development directory: /path/to/triple-ontology/development

Found: 01/TBOX.ttl
Found: 02/TBOX.ttl
Found: 03/TBOX.ttl
...

Found 11 TTL files

Creating merged graph...
Loading 01/TBOX.ttl...
  Added 29 triples from 01/TBOX.ttl
Loading 02/TBOX.ttl...
  Added 30 triples from 02/TBOX.ttl
...

Total triples in merged graph: 350

Adding ontology metadata...

=== Ontology Statistics (TBOX Only) ===
Classes: 25
Object Properties: 18
Data Properties: 5
Total Triples: 355
=======================================

Saving merged ontology to: ../ontology/triple-ontology.ttl

✓ Ontology successfully saved to: ../ontology/triple-ontology.ttl
```

## Directory Structure

```
triple-ontology/
├── development/          # Iteration files (source)
│   ├── 01/
│   │   ├── TBOX.ttl
│   │   └── ABOX.ttl
│   ├── 02/
│   │   ├── TBOX.ttl
│   │   └── ABOX.ttl
│   └── ...
├── ontology/            # Consolidated ontology (output)
│   └── triple-ontology.ttl
└── scripts/             # Utility scripts
    ├── README.md
    ├── requirements.txt
    └── merge_iterations.py
```

## Notes

- The script automatically handles duplicate triples (RDF semantics)
- Namespace prefixes are standardized across all iterations
- The output is valid Turtle format
- Statistics are logged during execution
- Error handling for missing or malformed files
