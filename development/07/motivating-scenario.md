# Motivating Scenario (Iteration 7)

## Name
Project

## Description

### General description
In addition to documents, GoTriple facilitates the integration of projects within the Social Sciences and Humanities (SSH) domain from external sources. Although integration is limited to a select number of external data sources, each project is accompanied by the following metadata:
- **Identification**: Analogous to documents, it is feasible to associate one or more identifiers with a project.
- **Temporal Placement**: Metadata are available to denote the project's duration or period of execution.
- **Roles**: The roles involved in the organization and funding of the project are specified.
- **Subject**: Similar to documents, a project can be linked to one or more disciplinary categories or to one or more keywords.
- **Name, Acronyms, and Description**: Basic textual metadata are provided to offer human-readable information about the project.

### Technical specification

Projects in GoTriple are modeled as instances of `schema:Project` to align with Schema.org standards. Each project includes:

**Identification:**
- Projects have unique identifiers using the DataCite pattern (`datacite:Identifier` and `datacite:IdentifierScheme`)
- Common identifier schemes include project IDs from funding agencies (e.g., Horizon 2020, national research councils)

**Temporal Information:**
- `schema:startDate`: Project start date (xsd:date or xsd:dateTime)
- `schema:endDate`: Project end date (xsd:date or xsd:dateTime)

**Funding and Sponsorship:**
- `schema:funding`: Connects project to `schema:Grant` instances
- `schema:Grant` includes:
  - `schema:funder`: Links to funding organization(s)
  - `schema:sponsor`: Links to sponsoring organization(s)

**Roles:**
- Projects use the PRO (Publishing Roles Ontology) pattern with `pro:RoleInTime`
- Key roles include:
  - `triple:Sponsor`: Organization providing financial support
  - `triple:Funder`: Organization funding the project
  - `triple:CoordinatingEntity`: Organization coordinating project activities
- Roles are held by agents (`foaf:Agent`, `foaf:Person`, or `foaf:Organization`)

**Subject Coverage:**
- `schema:about`: Links to disciplinary topics (SKOS concepts)
- `schema:keywords`: Links to keyword terms (`schema:DefinedTerm`)

**Descriptive Metadata:**
- `schema:name`: Official project name (multilingual using @lang tags)
- `schema:alternateName`: Project acronym or alternative names
- `schema:description`: Project abstract/description (multilingual)

## Example 1

**TRIPLE-SSH Project funded by Horizon 2020**

The TRIPLE project ("Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration") is a 3-year SSH research initiative (2019-2022) funded by the European Commission under Horizon 2020 program (Grant Agreement No. 863420). The project is coordinated by the Austrian Centre for Digital Humanities and Cultural Heritage (ACDH-CH) with participation from 15 partner institutions across Europe. The project focuses on developing a discovery platform for SSH research resources and has a budget of €3.5 million sponsored by the European Research Executive Agency (REA).

**Key metadata:**
- Identifier: H2020-863420
- Start date: 2019-01-01
- End date: 2022-12-31
- Coordinating entity: Austrian Centre for Digital Humanities and Cultural Heritage (ACDH-CH)
- Funder: European Commission
- Sponsor: European Research Executive Agency (REA)
- Topic: Digital Humanities (discipline)
- Keywords: discovery platform, semantic web, SSH research
- Name: Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration
- Alternate name: TRIPLE
- Description: The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe.

## Example 2

**National Research Project on Migration Studies**

A 2-year research project (2020-2022) on contemporary migration patterns in Southern Europe, funded by the Italian Ministry of University and Research (MUR) under the PRIN 2018 program (project code: 2018ABCD123). The project is coordinated by the University of Bologna, Department of Sociology and Business Law. The project examines socio-economic integration of migrants in Italian urban contexts with a grant of €250,000.

**Key metadata:**
- Identifier: PRIN-2018ABCD123
- Start date: 2020-03-01
- End date: 2022-02-28
- Coordinating entity: University of Bologna - Department of Sociology and Business Law
- Funder: Italian Ministry of University and Research (MUR)
- Sponsor: Italian Ministry of University and Research (MUR)
- Topic: Sociology, Migration Studies (disciplines)
- Keywords: migration, integration, urban studies, Southern Europe
- Name: Socio-Economic Integration of Migrants in Italian Urban Contexts
- Alternate name: MIGURIS
- Description: This research project investigates the mechanisms of socio-economic integration of migrant populations in three Italian metropolitan areas.

## Example 3

**Collaborative Heritage Documentation Project**

A digital humanities project (2021-2024) focused on documenting endangered cultural heritage sites in the Balkans. The 3-year initiative is coordinated by the University of Vienna and co-funded by two sources: the Austrian Science Fund (FWF) with grant number P-34567 and the Getty Foundation's Keeping It Modern program. The project involves partnerships with local museums and heritage institutions in Croatia, Serbia, and Bosnia-Herzegovina.

**Key metadata:**
- Identifiers: FWF-P-34567, GETTY-KIM-2021-15
- Start date: 2021-06-01
- End date: 2024-05-31
- Coordinating entity: University of Vienna - Institute for Cultural Heritage
- Funders: Austrian Science Fund (FWF), The Getty Foundation
- Sponsors: Austrian Science Fund (FWF), The Getty Foundation
- Topics: Cultural Heritage, Digital Humanities, History (disciplines)
- Keywords: heritage documentation, Balkans, digital preservation, cultural memory
- Name: Digital Documentation of Endangered Cultural Heritage in the Balkans
- Alternate name: BALKAN-HERITAGE
- Description: This collaborative project employs advanced digital technologies to document and preserve endangered cultural heritage sites across the Balkan region.

## Example 4

**ERC Advanced Grant on Ancient Philosophy**

A 5-year individual research project (2022-2027) examining the concept of justice in Hellenistic philosophy, funded by the European Research Council through an ERC Advanced Grant (project number: ADG-101052789). The principal investigator is based at Humboldt University Berlin, Faculty of Philosophy. The project receives €2.5 million in funding.

**Key metadata:**
- Identifier: ERC-ADG-101052789
- Start date: 2022-09-01
- End date: 2027-08-31
- Coordinating entity: Humboldt University Berlin - Faculty of Philosophy
- Funder: European Research Council (ERC)
- Sponsor: European Research Council (ERC)
- Topics: Philosophy, Ancient History (disciplines)
- Keywords: Hellenistic philosophy, justice, ancient ethics, Stoicism
- Name: Conceptions of Justice in Hellenistic Philosophy
- Alternate name: HELLENISTIC-JUSTICE
- Description: This project provides a comprehensive analysis of how Hellenistic philosophical schools conceptualized justice and its role in ethical and political thought.
