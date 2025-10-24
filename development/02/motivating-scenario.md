# Motivating Scenario (Iteration 2)

## Name
GoTriple Controlled Vocabularies

## Description

### General description

Every document in the GoTriple platform can be associated with one or more of the following classification entities: **license**, **access conditions**, **type of document**, and **field of discipline**. The data sources from which individual documents are retrieved contain an extremely variable number of these entities, with inconsistent terminology and representations.

To reduce the complexity and variability of this information, the approach adopted was to extract the most frequent terms and create **controlled vocabularies**. Therefore, for each of the entities listed above, a controlled vocabulary has been defined using the **SKOS (Simple Knowledge Organization System)** standard.

This controlled vocabulary serves as a standardized set of terms for each entity, ensuring consistency across the dataset. By doing so, it simplifies the categorization and retrieval of documents based on their respective entities. This method aids in streamlining the search and analysis process, making it easier to identify and access documents that meet specific criteria. Additionally, the use of controlled vocabularies can enhance the accuracy and efficiency of data processing and analysis within the system.

#### The Four Controlled Vocabularies

1. **License Vocabulary**: This refers to the legal permissions and restrictions associated with a document. A license dictates how the document can be used, shared, modified, and distributed. For instance, some documents might be under open licenses (like CC-BY-4.0) allowing free use and distribution, while others could have more restrictive licenses that limit their use to certain conditions or require payment or attribution.

2. **Access Conditions Vocabulary**: These are the terms that govern how and by whom a document can be accessed. Access conditions might include restrictions based on user credentials, subscription status, geographical location, or other criteria. For example, some documents might be "Open Access", while others could be "Restricted Access" available only to certain academic institutions or paid subscribers.

3. **Document Type Vocabulary**: This refers to the category or format of the document. It includes distinctions such as Article, Dataset, Book, Conference Proceeding, Thesis, Report, etc. Each type of document has its own structure, purpose, and audience. For instance, a research article might present new findings in a specific field, whereas a dataset provides raw data for analysis.

4. **Discipline Vocabulary**: This entity relates to the academic or professional field to which a document belongs. It denotes the subject area or the specialized domain of knowledge covered by the document. Examples of disciplines include History, Sociology, Digital Humanities, Linguistics, Political Science, and many others. This categorization is crucial for researchers and professionals seeking information specific to their field of study or interest.

### Technical specification

For defining the common base structure of each controlled vocabulary, the following structure has been adopted using **SKOS**:

#### SKOS Structure

Every controlled vocabulary is modeled as a **`skos:ConceptScheme`**, and every term within that vocabulary is modeled as a **`skos:Concept`**.

Every term in the vocabulary has the following capabilities:

1. **Connection to a Vocabulary** (`skos:inScheme`): Each term must be associated with a specific controlled vocabulary. This ensures that it is categorized correctly and is part of a structured collection of standardized terms. This association helps in maintaining the integrity and organization of the vocabularies across different entities.

2. **Unique Identifier**: Every term in the vocabulary has a unique URI identifier. This is crucial for distinguishing between terms, especially when different terms might have similar names or descriptions.

3. **Labels and Definitions** (`rdfs:label`, `skos:definition`): Each term has human-readable labels and optional definitions explaining its meaning.

4. **Ability to Connect to One or More External Entities**: Each term should have the capacity to link to external entities in two specific ways:
   - **Close Match** (`skos:closeMatch`): This implies that the term in the vocabulary is nearly equivalent to, but not exactly the same as, a term in an external system or entity (e.g., COAR, Wikidata, Getty vocabularies). A close match suggests a high degree of similarity or relevance, though the terms might not be identical.
   - **Exact Match** (`skos:exactMatch`): This indicates that the term in the controlled vocabulary is precisely the same as a term in an external entity. An exact match is used when the terms are interchangeable, with no variation in meaning or context.

#### Properties Connecting Documents to Vocabularies

- **`schema:license`**: Links a document to a license term from the License Vocabulary
- **`schema:conditionsOfAccess`**: Links a document to an access condition term from the Access Conditions Vocabulary
- **`dc:type`**: Links a document to a document type term from the Document Type Vocabulary
- **`dc:subject`**: Links a document to one or more discipline terms from the Discipline Vocabulary

## Example 1: Document with License

`document_1` is an open access article published under a Creative Commons Attribution 4.0 license. The document is linked to the term `cc_by_4_0` from the `license_vocabulary`. This term has an exact match to the official Creative Commons URI.

- Document: `document_1`
- License term: `cc_by_4_0`
- Belongs to: `license_vocabulary` (ConceptScheme)
- External match: Exact match to `https://creativecommons.org/licenses/by/4.0/`

## Example 2: Document with Access Conditions

`document_2` is a research paper that is freely available to anyone. The document is linked to the term `open_access` from the `access_conditions_vocabulary`. This term has a close match to the COAR Access Rights vocabulary.

- Document: `document_2`
- Access term: `open_access`
- Belongs to: `access_conditions_vocabulary` (ConceptScheme)
- External match: Close match to COAR's "Open Access" concept

## Example 3: Document with Type

`document_3` is a scholarly article. The document is linked to the term `article` from the `document_type_vocabulary`. This term has an exact match to the COAR Resource Type "article".

- Document: `document_3`
- Type term: `article`
- Belongs to: `document_type_vocabulary` (ConceptScheme)
- External match: Exact match to COAR Resource Type "article"

## Example 4: Document with Multiple Disciplines

`document_4` is an interdisciplinary study covering both Digital Humanities and Linguistics. The document is linked to two terms from the `discipline_vocabulary`: `digital_humanities` and `linguistics`. Both terms have close matches to external classification systems.

- Document: `document_4`
- Discipline terms: `digital_humanities`, `linguistics`
- Belong to: `discipline_vocabulary` (ConceptScheme)
- External matches: Close matches to UNESCO Thesaurus and Library of Congress Subject Headings
