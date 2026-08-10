## Informal Competency Questions (Iteration 7)

## Question 1

### Identifier
CQ_7.1

### Question
What are all the metadata properties and values associated with a specific project?

### Expected Outcome
A complete list of all metadata for the project including identifiers, temporal information, names, descriptions, topics, keywords, and funding.

### Result
* `triple:project_1` → "TRIPLE_PROJ_001" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "discovery platform" → `triple:grant_1`
* `triple:project_1` → "TRIPLE_PROJ_001" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "semantic web" → `triple:grant_1`
* `triple:project_1` → "TRIPLE_PROJ_001" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "SSH research" → `triple:grant_1`
* `triple:project_1` → "ark:/12345/project-triple-ssh" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "discovery platform" → `triple:grant_1`
* `triple:project_1` → "ark:/12345/project-triple-ssh" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "semantic web" → `triple:grant_1`
* `triple:project_1` → "ark:/12345/project-triple-ssh" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "SSH research" → `triple:grant_1`
* `triple:project_1` → "H2020-863420" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "discovery platform" → `triple:grant_1`
* `triple:project_1` → "H2020-863420" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "semantic web" → `triple:grant_1`
* `triple:project_1` → "H2020-863420" → "2019-01-01" → "2022-12-31" → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE" → "The TRIPLE project aims at creating a discovery platform that connects SSH researchers with relevant resources across Europe." → "Methods and Statistics" → "SSH research" → `triple:grant_1`

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
What projects are classified under a given discipline (e.g. Methods and Statistics)?

### Expected Outcome
A list of projects whose subject matter includes the specified discipline.

### Result
For the discipline "Methods and Statistics":
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
* `triple:project_1` → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "Original Identifier" → "H2020-863420"
* `triple:project_1` → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "TRIPLE Internal ID" → "TRIPLE_PROJ_001"
* `triple:project_1` → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "datacite:ark" → "ark:/12345/project-triple-ssh"
* `triple:project_2` → "Socio-Economic Integration of Migrants in Italian Urban Contexts" → "Original Identifier" → "PRIN-2018ABCD123"
* `triple:project_2` → "Socio-Economic Integration of Migrants in Italian Urban Contexts" → "TRIPLE Internal ID" → "TRIPLE_PROJ_002"
* `triple:project_2` → "Socio-Economic Integration of Migrants in Italian Urban Contexts" → "datacite:ark" → "ark:/12345/project-miguris"
* `triple:project_3` → "Digital Documentation of Endangered Cultural Heritage in the Balkans" → "Original Identifier" → "FWF-P-34567"
* `triple:project_3` → "Digital Documentation of Endangered Cultural Heritage in the Balkans" → "Original Identifier" → "GETTY-KIM-2021-15"
* `triple:project_3` → "Digital Documentation of Endangered Cultural Heritage in the Balkans" → "TRIPLE Internal ID" → "TRIPLE_PROJ_003"
* `triple:project_3` → "Digital Documentation of Endangered Cultural Heritage in the Balkans" → "datacite:ark" → "ark:/12345/project-balkan-heritage"
* `triple:project_4` → "Conceptions of Justice in Hellenistic Philosophy" → "Original Identifier" → "ERC-ADG-101052789"
* `triple:project_4` → "Conceptions of Justice in Hellenistic Philosophy" → "TRIPLE Internal ID" → "TRIPLE_PROJ_004"
* `triple:project_4` → "Conceptions of Justice in Hellenistic Philosophy" → "datacite:ark" → "ark:/12345/project-hellenistic-justice"

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


## Question 15

### Identifier
CQ_7.15

### Question
What is the contact point email for a specific project?

### Expected Outcome
The email address associated with the project's contact point.

### Result
For `project_1`: "project-team@triple.eu"

### Based on
Example 1


## Question 16

### Identifier
CQ_7.16

### Question
What is the type of a specific project (e.g., Research, Training, Network)?

### Expected Outcome
The project classification from the controlled vocabulary.

### Result
* `triple:project_1` → "Transforming Research through Innovative Practices for Linked Interdisciplinary Exploration" → "Funded"
* `triple:project_2` → "Socio-Economic Integration of Migrants in Italian Urban Contexts" → "Funded"
* `triple:project_3` → "Digital Documentation of Endangered Cultural Heritage in the Balkans" → "Funded"
* `triple:project_4` → "Conceptions of Justice in Hellenistic Philosophy" → "Funded"

### Based on
Examples 1 and 2
