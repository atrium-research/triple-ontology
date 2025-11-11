# Triple Ontology: TRIPLE

The TRIPLE project, launched in October 2019 and coordinated by the French National Center for
Scientific Research (CNRS), involved 22 partners from 15 European countries. Its primary aim was
to develop the [GoTriple.eu](https://GoTriple.eu) discovery platform, a multilingual access point for discovering and reusing
research artefacts in the social sciences and humanities (SSH).

The TRIPLE Ontology has been designed to formalise the GoTriple data model using semantic
technologies. The ontology addressed the challenge of managing heterogeneous data aggregated by
GoTriple's data processing pipeline (named SCRE), which integrates research artefacts from diverse external sources with varying
structures and formats.

The ontology ensures a robust semantic representation of research artefacts,
surpassing the limitations of initial alignments with Schema.org and SIOC standards. It was aligned
with the main data aggregators, ensuring adherence to state-of-the-art practices in the field.
Developed in collaboration with domain experts, the ontology was crafted to achieve several key
objectives: formalising the data model with semantic standards, defining controlled vocabularies,
establishing connections with external entities, ensuring resource reusability, and maintaining
detailed documentation for transparency and extensibility.

The ontology development followed the [SAMOD](https://essepuntato.it/samod/) (Simplified Agile Methodology for Ontology Development) methodology.
This approach ensured a flexible, iterative development process with comprehensive testing and
documentation, guaranteeing knowledge sharing and reuse across the SSH domain.

This repository contains the full documentation produced during the development of TRIPLE ontology.

## Repository Structure

### Core Directories

* **`development/`** - Contains 16 SAMOD iterations (01-16), each representing a complete development cycle with:
  * `motivating-scenario.md` - Use case description and examples
  * `informal-competency-questions.md` - Natural language requirements
  * `glossary-of-terms.md` - Domain terminology definitions
  * `formal-competency-questions.md` - SPARQL test queries
  * `TBOX.ttl` - Terminological Box (ontology structure: classes, properties, restrictions)
  * `ABOX.ttl` - Assertional Box (test instance data)
  * `modelet.graphml` - Graffoo diagram source file (yEd format)
  * `modelet.png` - Visual diagram export

* **`ontology/`** - Consolidated final ontology
  * `triple-ontology.ttl` - Merged TBOX from all iterations (structure only, no instances)

* **`diagrams/`** - Refactored Graffoo diagrams (01.png - 07.png) showing the consolidated model after each of the first 7 iterations

* **`sparql/`** - Refactored formal competency questions (01.md - 07.md) with SPARQL queries for testing the final ontology

* **`examples/`** - Practical data examples
  * `jsonld/` - Real-world JSON-LD serialization examples from GoTriple platform

* **`scripts/`** - Utility tools
  * `merge_iterations.py` - Merges all TBOX files into the consolidated ontology
  * `requirements.txt` - Python dependencies
  * See `scripts/README.md` for usage details

## Getting Started

The final ontology is available at [https://www.gotriple.eu/ontology/triple](https://www.gotriple.eu/ontology/triple).

To work with the ontology locally:

```bash
# View the consolidated ontology
cat ontology/triple-ontology.ttl

# Regenerate the consolidated ontology from iterations
cd scripts
pip install -r requirements.txt
python merge_iterations.py
```
