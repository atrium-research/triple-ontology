# Motivating Scenario (Iteration 9)

## Name
Access Conditions Vocabulary Extension and COAR Alignment

## Description

### General description

The GoTriple platform provides access to a diverse range of scholarly resources from multiple providers, each with different access policies and restrictions. To facilitate discovery and ensure users understand how they can access documents, GoTriple maintains a controlled vocabulary for access conditions.

Access conditions define the level of accessibility for a document, ranging from fully open access to restricted or embargoed content. Aligning this vocabulary with internationally recognized standards ensures interoperability with other scholarly infrastructures and repositories.

The COAR (Confederation of Open Access Repositories) Access Rights vocabulary is a widely adopted standard that defines four primary access levels for scholarly resources. By mapping and extending the GoTriple `conditions_of_access` vocabulary to align with COAR, the platform enhances its compatibility with global repository networks and provides clearer access information to users.

The four access levels being integrated are:

1. **Embargoed Access**: The resource is currently under embargo but will become openly accessible after a specified date. During the embargo period, access is restricted.

2. **Metadata Only Access**: Only the metadata (title, authors, abstract, etc.) is publicly accessible, but the full content of the resource is not available through the repository.

3. **Open Access**: The resource is freely accessible to anyone without restrictions. This is the most permissive access level.

4. **Restricted Access**: Access to the resource is limited to specific users or groups, such as institutional members, subscribers, or authorized individuals.

### Technical specification

The access conditions vocabulary extension involves adding four new terms to the `triple:conditions_of_access` controlled vocabulary:

1. **Term**: `acc_embargoed-access`
   - **Label**: "Embargoed access"
   - **Vocabulary**: `triple:conditions_of_access` (skos:ConceptScheme)
   - **External Alignment**: `skos:exactMatch` to `https://vocabularies.coar-repositories.org/access_rights/c_f1cf/` (COAR Embargoed Access)
   - **Usage**: Assigned to documents via `schema:conditionsOfAccess` property

2. **Term**: `acc_metadata-only-access`
   - **Label**: "Metadata only access"
   - **Vocabulary**: `triple:conditions_of_access`
   - **External Alignment**: `skos:exactMatch` to `https://vocabularies.coar-repositories.org/access_rights/c_14cb/` (COAR Metadata Only Access)
   - **Usage**: Assigned to documents via `schema:conditionsOfAccess` property

3. **Term**: `acc_open-access`
   - **Label**: "Open access"
   - **Vocabulary**: `triple:conditions_of_access`
   - **External Alignment**: `skos:exactMatch` to `https://vocabularies.coar-repositories.org/access_rights/c_abf2/` (COAR Open Access)
   - **Usage**: Assigned to documents via `schema:conditionsOfAccess` property

4. **Term**: `acc_restricted-access`
   - **Label**: "Restricted access"
   - **Vocabulary**: `triple:conditions_of_access`
   - **External Alignment**: `skos:exactMatch` to `https://vocabularies.coar-repositories.org/access_rights/c_16ec/` (COAR Restricted Access)
   - **Usage**: Assigned to documents via `schema:conditionsOfAccess` property

Each term is defined as a `skos:Concept` within the `triple:conditions_of_access` vocabulary (a `skos:ConceptScheme`), ensuring consistency with the controlled vocabulary pattern established in Iteration 02.

## Example 1

`document_1` has access condition `acc_open-access`. This term belongs to the `conditions_of_access` vocabulary and has an exact match to the COAR access rights term `https://vocabularies.coar-repositories.org/access_rights/c_abf2/`.

## Example 2

`document_23` has access condition `acc_embargoed-access`, indicating that the full content is currently under embargo but will become openly accessible after a specified date.

## Example 3

`document_56` has access condition `acc_metadata-only-access`. Users can view the document's metadata (title, authors, abstract) but cannot access the full text through GoTriple.

## Example 4

`acc_restricted-access` is a concept in the `conditions_of_access` vocabulary that is exactly matched to the COAR access rights term for restricted access: `https://vocabularies.coar-repositories.org/access_rights/c_16ec/`.
