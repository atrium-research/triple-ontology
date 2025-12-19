## Informal Competency Questions (Iteration 7)

## Question 1

### Identifier
CQ_7.1

### Question
What are all the metadata properties and values associated with a specific project?

### Expected Outcome
A complete list of all metadata for the project including identifiers, temporal information, names, descriptions, topics, keywords, and funding.

### Result
For `project_1` (TRIPLE-SSH):
* Identifier: H2020-863420
* Start date: 2019-01-01
* End date: 2022-12-31
* Name: "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration"@en
* Alternate name: "TRIPLE"@en
* Description: "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe."@en
* Topic: Digital Humanities
* Keywords: discovery platform, semantic web, SSH research
* Funding: grant_1
* Date created: 2018-12-01
* Date modified: 2023-01-15
* Language: en
* Organizer: ACDH-CH
* Main Entity of Page: https://triple.eu/projects/1

### Based on
Example 1


## Question 2

### Identifier
CQ_7.2

### Question
What are all the funding grants associated with a project, and who are the funders and sponsors for each grant?

### Expected Outcome
A list of grants with their associated funding organizations (funders and sponsors).

### Result
For `project_1` (TRIPLE-SSH):
* Grant: `grant_1`
  * Funder: European Commission
  * Sponsor: European Research Executive Agency (REA)

### Based on
Example 1


## Question 3

### Identifier
CQ_7.3

### Question
Which projects have multiple funders or sponsors?

### Expected Outcome
A list of projects that receive funding from more than one source.

### Result
* `project_3` (BALKAN-HERITAGE)
  * Grant 1: Austrian Science Fund (FWF)
  * Grant 2: The Getty Foundation

### Based on
Example 3


## Question 4

### Identifier
CQ_7.4

### Question
What projects are associated with a specific discipline or topic (e.g., Digital Humanities)?

### Expected Outcome
A list of projects whose subject matter includes the specified discipline.

### Result
For topic "Digital Humanities":
* `project_1` (TRIPLE)
* `project_3` (BALKAN-HERITAGE)

### Based on
Examples 1 and 3


## Question 5

### Identifier
CQ_7.5

### Question
What is the duration of each project (time span between start and end dates)?

### Expected Outcome
A list of projects with their calculated duration in years or months.

### Result
* `project_1`: 4 years (2019-2022)
* `project_2`: 2 years (2020-2022)
* `project_3`: 3 years (2021-2024)
* `project_4`: 5 years (2022-2027)

### Based on
Examples 1, 2, 3, 4


## Question 6

### Identifier
CQ_7.6

### Question
Which projects were active during a specific time period (e.g., year 2022)?

### Expected Outcome
A list of projects whose temporal span overlaps with the specified period.

### Result
For year 2022:
* `project_1` (TRIPLE) - ends 2022-12-31
* `project_2` (MIGURIS) - ends 2022-02-28
* `project_3` (BALKAN-HERITAGE) - ongoing
* `project_4` (HELLENISTIC-JUSTICE) - starts 2022-09-01

### Based on
Examples 1, 2, 3, 4


## Question 7

### Identifier
CQ_7.7

### Question
What are all the identifier schemes used for projects and their corresponding identifier values?

### Expected Outcome
A list of projects with their identifier schemes and literal values.

### Result
* `project_1`: Horizon 2020 Grant Agreement Number → "H2020-863420"
* `project_2`: PRIN Project Code → "PRIN-2018ABCD123"
* `project_3`:
  * FWF Project Number → "FWF-P-34567"
  * Getty Foundation Grant Number → "GETTY-KIM-2021-15"
* `project_4`: ERC Grant Number → "ERC-ADG-101052789"

### Based on
Examples 1, 2, 3, 4


## Question 8

### Identifier
CQ_7.8

### Question
Which organizations fund or sponsor multiple projects?

### Expected Outcome
A list of organizations that appear as funders or sponsors for more than one project.

### Result
(Based on current examples, each organization funds only one project, but this query would identify organizations funding multiple projects if present in the data)

### Based on
Examples 1, 2, 3, 4


## Question 9

### Identifier
CQ_7.9

### Question
What keywords are most frequently associated with projects in the platform?

### Expected Outcome
A ranked list of keywords by frequency of use across all projects.

### Result
All keywords appear once in the current dataset. In a larger dataset, this would show the most common research themes.

### Based on
Examples 1, 2, 3, 4


## Question 10

### Identifier
CQ_7.10

### Question
Retrieve projects by searching for specific keywords in their names, descriptions, or acronyms?

### Expected Outcome
A list of projects whose textual metadata contains the search term.

### Result
For search term "heritage":
* `project_3` (BALKAN-HERITAGE) - contains "heritage" in name, alternate name, and description

For search term "philosophy":
* `project_4` (HELLENISTIC-JUSTICE) - contains "philosophy" in name and description

### Based on
Examples 3 and 4
