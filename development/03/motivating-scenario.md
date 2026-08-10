# Motivating Scenario (Iteration 3)

## Name
Documents Roles

## Description

### General description

The life cycle and creation of a document in GoTriple involve various roles, each playing a significant part in its development, dissemination, and maintenance. These roles, which can be assumed by either organizations or individuals, are fluid and may change over time. They include:

1. **Author**: The individual or group primarily responsible for creating the content of the document. Authors are the intellectual source of the research and ideas presented in the document.

2. **Contributor**: These are individuals or entities that have played a significant, but not primary, role in the creation of the document. Their contributions can be in various forms, such as providing data, writing assistance, or other forms of support.

3. **Publisher**: The publisher is responsible for the distribution and dissemination of the document. This role often involves tasks such as editing, design, marketing, and ensuring the document reaches its intended audience.

4. **Provider**: This refers to the entity that makes the document available within the GoTriple platform. Providers may be different from the original publishers, especially in cases where documents are sourced from third-party databases or repositories.

5. **Producer**: The producer is typically responsible for the technical aspects of creating the document, which might include formatting, typesetting, or the production of physical copies in the case of printed materials.

6. **Aggregator**: An aggregator in the context of GoTriple collates various documents from different sources. This role is crucial for enhancing the platform's database by bringing together diverse SSH resources from multiple origins.

7. **Primary Producer**: This is the original source or creator of the document, often before it undergoes processing or publishing. The primary producer is usually responsible for the initial creation and compilation of the content.

8. **Funder**: Funders are individuals or organizations that provide financial support for the creation, research, or publication of the document. Their role is vital in enabling the research and dissemination process, especially in academic and scholarly contexts.

9. **Contact Point**: A specific contact point (person or organization) designated for the document, providing a way to reach out for inquiries or feedback related to the resource.

Each of these roles contributes to the lifecycle of a document in GoTriple, from its initial creation to its eventual dissemination and use. This dynamic ecosystem ensures that documents are not only rich in content but also supported by a network of contributors and facilitators, enhancing the overall value and accessibility of SSH resources on the GoTriple platform.

### Technical specification

The roles are modelled as **direct properties of the document**, not as reified role objects: `schema:author`, `schema:contributor`, `schema:publisher`, `schema:provider` and the TRIPLE-minted `triple:aggregator` link a `triple:Document` to a `foaf:Person` or a `foaf:Organization`, and `schema:contactPoint` links it to a `schema:ContactPoint`.

Two consequences follow, and they are deliberate:

- **No temporal collocation.** A reified `RoleInTime` proxy — role, agent and time as three sides of one object — would be needed to say *when* an agent held a role. GoTriple's source metadata does not carry that information, so the model does not ask for it: the year a provider made a document available is not represented. Should it become necessary, the PROV or PRO patterns are the place to look.
- **Roles are only those the platform actually receives.** Producer, primary producer and funder are described above because they are part of the publishing lifecycle, but no source in GoTriple provides them for a document, and no property is minted for them here. Funding is modelled at project level in iteration 07 (`schema:funding`, `schema:funder`), not on the document.

`triple:aggregator` is the only new property of this iteration: no standard vocabulary names the agent that collates documents from several sources into a discovery platform.

## Example 1

`document_1` has the following metadata:

- **Author**: `author_34`, a `foaf:Person` named "name_45"
- **Providers**: `provider_9`, a `foaf:Organization` named "name_3", and `provider_45`, a `foaf:Organization` named "name_1"
- **Contact point**: `contact_point_1`, with e-mail `contact@example.org`
