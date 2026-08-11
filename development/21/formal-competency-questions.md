# Formal Competency Questions - Iteration 21

## CQ_21.1

What resource is this document based on (derivation)?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?source WHERE {
  triple:document_it21_a schema:isBasedOn ?source .
}
```

**Expected result:**
- `https://zenodo.org/records/1234567`

## CQ_21.2

Which platform products does the document refer the reader to?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?product WHERE {
  triple:document_it21_a dcterms:references ?product .
}
```

**Expected result:**
- `triple:dataset_it21_b`

## CQ_21.3

Which documents reference this dataset (passive side, asserted independently)?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?document WHERE {
  triple:dataset_it21_b dcterms:isReferencedBy ?document .
}
```

**Expected result:**
- `triple:document_it21_a`

## CQ_21.4

Return access page and direct download file of each distribution of the dataset.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

SELECT ?distribution ?access ?download WHERE {
  triple:dataset_it21_b dcat:distribution ?distribution .
  ?distribution dcat:accessURL ?access ;
                dcat:downloadURL ?download .
}
```

**Expected result:**
- `triple:distribution_it21_b` → `https://data.example-provider.eu/datasets/wm-settlements` → `https://data.example-provider.eu/datasets/wm-settlements/sites.csv`

## CQ_21.5

What is the occupation of the profile, as supplied by the provider?

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?occupation WHERE {
  triple:profile_it21_c schema:jobTitle ?occupation .
}
```

**Expected result:**
- "Research Software Engineer"
