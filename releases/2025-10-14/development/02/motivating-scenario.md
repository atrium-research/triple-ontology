# Motivating Scenario (Iteration 2)

## Name
GoTriple Controlled Vocabulary

## Description

### General description

Every document can be associated with one or more of the following entities: license, access conditions, type of document, and field of discipline. The data sources from which individual documents are retrieved contain an extremely variable number of these entities. To reduce the complexity and variability of this information, the approach adopted was to extract the most frequent terms and create controlled vocabularies. Therefore, for each of the entities listed above, a controlled vocabulary has been defined.

This controlled vocabulary serves as a standardized set of terms for each entity, ensuring consistency across the dataset. By doing so, it simplifies the categorization and retrieval of documents based on their respective entities. This method aids in streamlining the search and analysis process, making it easier to identify and access documents that meet specific criteria. Additionally, the use of controlled vocabularies can enhance the accuracy and efficiency of data processing and analysis within the system.

1. **License**: This refers to the legal permissions and restrictions associated with a document. A license dictates how the document can be used, shared, modified, and distributed. For instance, some documents might be under open licenses allowing free use and distribution, while others could have more restrictive licenses that limit their use to certain conditions or require payment or attribution.

2. **Access Conditions**: These are the terms that govern how and by whom a document can be accessed. Access conditions might include restrictions based on user credentials, subscription status, geographical location, or other criteria. For example, some documents might be publicly accessible, while others could be available only to certain academic institutions or paid subscribers.

3. **Type of Document**: This refers to the category or format of the document. It includes distinctions such as research papers, articles, technical reports, books, or datasets. Each type of document has its own structure, purpose, and audience. For instance, a research paper might present new findings in a specific field, whereas a technical report might provide detailed technical information about a project or study.

4. **Field of Discipline**: This entity relates to the academic or professional field to which a document belongs. It denotes the subject area or the specialized domain of knowledge covered by the document. Examples of disciplines include medicine, engineering, economics, history, and many others. This categorization is crucial for researchers and professionals seeking information specific to their field of study or interest.

### Technical specification

For defining the common base structure of each controlled vocabulary, the following structure has been adopted within the scope of this project. Every term listed in the vocabulary should have the following capabilities:

1. **Connection to a Vocabulary**: Each term must be associated with a specific controlled vocabulary. This ensures that it is categorized correctly and is part of a structured collection of standardized terms. This association helps in maintaining the integrity and organization of the vocabularies across different entities.

2. **Unique Identifier**: Every term in the vocabulary should have a unique identifier. This is crucial for distinguishing between terms, especially when different terms might have similar names or descriptions. A unique identifier could be a numerical code, an alphanumeric string, or any other system that ensures each term is distinctly recognized.

3. **Ability to Connect to One or More External Entities**: Each term should have the capacity to link to external entities in two specific ways:
   - **Close Match**: This implies that the term in the vocabulary is nearly equivalent to, but not exactly the same as, a term in an external system or entity. A close match suggests a high degree of similarity or relevance, though the terms might not be identical.
   - **Exact Match**: This indicates that the term in the controlled vocabulary is precisely the same as a term in an external entity. An exact match is used when the terms are interchangeable, with no variation in meaning or context.


## Example 1

`document_1` is connected with the term `term_45`. It belongs to `schema_45`. This term is closely connect with `close_external_term_4` and `close_external_term_6`


