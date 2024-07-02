# Triple Ontology: TRIPLE

The TRIPLE project, launched in October 2019 and coordinated by the French National Center for
Scientific Research (CNRS), involved 22 partners from 15 European countries. Its primary aim was
to develop the GoTriple discovery platform, a multilingual access point for discovering and reusing
research artefacts in the social sciences and humanities (SSH). This thesis presented a
comprehensive ontology designed to formalise the TRIPLE data model using semantic
technologies. The ontology addressed the challenge of managing heterogeneous data aggregated by
the Core Pipeline, which integrated research artefacts from diverse external sources with varying
structures and formats.
This newly developed ontology ensured a robust semantic representation of research artefacts,
surpassing the limitations of initial alignments with Schema.org and SIOC standards. It was aligned
with the main data aggregators, ensuring adherence to state-of-the-art practices in the field.
Developed in collaboration with domain experts, the ontology was crafted to achieve several key
objectives: formalising the data model with semantic standards, defining controlled vocabularies,
establishing connections with external entities, ensuring resource reusability, and maintaining
detailed documentation for transparency and extensibility.
The ontology development followed a structured methodology, beginning with a preliminary
analysis and employing the Simplified Agile Methodology for Ontology Development (SAMOD).
This approach ensured a flexible, iterative development process with comprehensive testing and
documentation, guaranteeing the ontology's accuracy and adaptability. Consequently, the ontology
enhanced the semantic representation of research artefacts, promoted interoperability, and facilitated
collaboration and knowledge reuse across the SSH domain.

This repository contains the full documentation produced during the development of TRIPLE ontology. In particular:

* the `development` directory contains a folder for each iteration, thus constituting a full test case with a Motivating Scenario, a list of Informal Competency Questions, a Glossary of Terms, a Graffoo diagram of the model in .png format (along with its .graphml file), a list of Formal Competency Questions, a TBox and a ABox (both written in the Turtle RDF serialization);

* the `diagrams` directory contains a set of Graffoo diagrams representing the refactored model of each iteration;

* the `sparql` directory contains a set of refactored Formal Competency Questions.

