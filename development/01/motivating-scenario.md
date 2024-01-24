# Motivating Scenario (Iteration 1)

## Name
GoTriple Document
## Description

### General description

[add abstract and title]

GoTriple is an advanced multilingual discovery platform specifically tailored for the social sciences and humanities (SSH) sector. It is designed to aggregate, process, and semantically enrich a vast array of SSH resources. These resources include scholarly publications, research datasets, detailed project descriptions, and extensive profiles of researchers, sourced from a wide range of origins. GoTriple’s primary objective is to facilitate the discovery and subsequent reuse of SSH resources, which are often dispersed across various European language repositories. The platform enables users to forge connections across different research disciplines and linguistic boundaries. It is equipped with sophisticated tools and features for research support, including data visualization, web annotation, personalized recommendation systems, social networking capabilities, and innovative approaches to research funding, such as crowdfunding.

In the GoTriple environment, the term "document" refers to a broad spectrum of records obtained from data providers. These records encompass a wide variety of scholarly and research-oriented materials. Each document within GoTriple is characterized by several distinct features:

1. **Content Variety**: Documents in GoTriple cover an extensive range of formats, including academic papers, datasets, project reports, and more, catering to the diverse needs of the SSH community.

2. **Multilingual Support**: GoTriple places significant emphasis on the linguistic aspect of documents. It accurately identifies and represents the language of a publication and its textual components, such as titles, abstracts, and keywords. The platform employs a controlled vocabulary that includes TRIPLE’s primary languages and other common languages, enhanced with special labels like "other" and "undefined" for cases that fall outside standard categorizations.

3. **Language Identification**: Employing advanced pattern matching rules, GoTriple categorizes the language of a document’s metadata. If the language is not in the controlled vocabulary, it is labeled as "other," and if missing, it is marked as "undefined." This ensures comprehensive and precise language representation.

4. **ISO-639-1 Standardization**: Each language element in GoTriple adheres to the ISO-639-1 notation, a two-character code format. This standardization facilitates language recognition and aligns with the platform’s automatic translation services.

5. **Multiple Identifiers**: Every document in GoTriple is associated with multiple identifiers, enhancing the platform's ability to accurately reference, locate, and cite documents. This multi-identifier system is crucial in differentiating documents within GoTriple’s diverse collection, ensuring a robust and efficient document management and retrieval system.

### Technical specification

The technical description of a document within GoTriple encompasses several key aspects:

1. **Types**: A document in GoTriple can be classified into various types to accurately represent its nature and content. These types include, but are not limited to, Article, Bibliography, Blog Post, Book, Conference, Dataset, Image, Learning Object, Manuscript, Report, Periodical, Preprint, Review, Software, Text, Thesis, Map, and more. Each type serves to categorize the document in a way that reflects its primary purpose or format.

2. **Languages**: The language attribute of a document is critical for its categorization and accessibility. GoTriple incorporates a controlled vocabulary that covers a wide range of languages, ensuring accurate representation and identification. This includes primary languages like Croatian, English, French, German, Greek, Italian, Polish, Portuguese, Slovenian, Spanish, and Ukrainian, along with other common languages such as Arabic, Dutch, Swedish, and more. Special labels like "other" and "undefined" are also used to categorize languages not specifically listed or when language data is missing. Languages are formatted in ISO-639-1 two-character codes, aligning with the platform’s language recognition and translation services.

3. **Identifiers**: Each document in GoTriple is associated with several identifiers, enhancing its traceability and accessibility. These identifiers include:

   - **Local Identifier**: A unique identifier assigned within the GoTriple system, serving as a primary reference point for the document within the platform.
   - **DOI (Digital Object Identifier)**: A widely recognized identifier that provides a persistent link to the document's location on the internet. DOIs are crucial for ensuring long-term accessibility and are commonly used in academic and research settings.
   - **Full Document URL**: The direct URL to the document itself, providing immediate access to the document for viewing or download.
   - **Source URL**: This URL points to the original source of the document, offering a link to where the document was initially published or hosted.
   - **Landing Page URL**: The URL of the landing page that provides descriptive information about the document, often including metadata, abstracts, and links to the full document or related resources.


## Example 1

`document_1` has these identifiers: `identifier_2` and `identifier_4`. Its type is `type_5`. The language of the document is `language_10`


## Example 2

`document_45` has these identifiers: `identifier_67` and `identifier_678`. Its type is `type_7`. The language of the document is `language_2`


## Example 3

`document_31` has these identifiers: `identifier_78` and `identifier_645`. Its type is `type_5`. The language of the document is `language_10`
