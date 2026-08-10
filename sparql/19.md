## Formal Competency Questions (Iteration 19)

## CQ_19.1

Retrieve the given name and the family name of the persons behind GoTriple profiles.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?profile ?givenName ?familyName WHERE {
  ?profile a triple:Profile ;
           foaf:givenName ?givenName ;
           foaf:familyName ?familyName .
}
```

**Expected result:**
- `triple:profile_it19_1` → "Sofia" → "Rossi"

## CQ_19.2

Retrieve the disciplines a profile is interested in (chosen by the user or automatically detected).

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?profile ?discipline WHERE {
  ?profile a triple:Profile ;
           foaf:topic_interest ?discipline .
  ?discipline a triple:Discipline .
}
ORDER BY ?discipline
```

**Expected result:**
- `triple:profile_it19_1` → `disc:cultural_heritage_and_museology`
- `triple:profile_it19_1` → `disc:methods_and_statistics`

## CQ_19.3

Retrieve the TRIPLE thesaurus concepts a profile declares to know about, with their labels.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?profile ?concept ?label WHERE {
  ?profile a triple:Profile ;
           schema:knowsAbout ?concept .
  ?concept a skos:Concept ;
           skos:prefLabel ?label .
}
```

**Expected result:**
- `triple:profile_it19_1` → <http://semantics.gr/authorities/SSH-LCSH/sh2008122106> → "Digital humanities"
- `triple:profile_it19_1` → <http://semantics.gr/authorities/SSH-LCSH/sh2008122106> → "Informatica umanistica"
- `triple:profile_it19_1` → <http://semantics.gr/authorities/SSH-LCSH/sh2008122106> → "Humanités numériques"

## CQ_19.4

Retrieve the languages a profile knows.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?profile ?language ?languageName WHERE {
  ?profile a triple:Profile ;
           schema:knowsLanguage ?language .
  ?language a schema:Language ;
            schema:name ?languageName .
}
ORDER BY ?languageName
```

**Expected result:**
- `triple:profile_it19_1` → `triple:language_en_it19` → "English"
- `triple:profile_it19_1` → `triple:language_it_it19` → "Italian"

## CQ_19.5

Retrieve the organization a profile is affiliated with.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?profile ?organization ?organizationName WHERE {
  ?profile a triple:Profile ;
           schema:affiliation ?organization .
  ?organization a foaf:Organization ;
                schema:name ?organizationName .
}
```

**Expected result:**
- `triple:profile_it19_1` → `triple:organization_it19_1` → "University of Bologna"

## CQ_19.6

Retrieve the persistent identifiers of the persons behind GoTriple profiles, with their scheme and value, excluding the internal Elasticsearch id.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://www.essepuntato.it/2010/06/literalreification/>

SELECT ?profile ?scheme ?value WHERE {
  ?profile a triple:Profile ;
           datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme ?scheme ;
              litre:hasLiteralValue ?value .
  FILTER (?scheme != triple:internal_id_schema)
}
ORDER BY ?profile ?scheme
```

**Expected result:**
- `triple:profile_it19_1` → `datacite:ark` → "ark:/12345/profile-sofia-rossi"
- `triple:profile_it19_1` → `datacite:orcid` → "0000-0002-1825-0097"
- `triple:profile_it19_1` → `triple:gotriple_id_schema` → "sofia_rossi_operas_0001"
- `triple:profile_it19_1` → `triple:idref_schema` → "123456789"
- `triple:profile_it19_2` → `datacite:ark` → "ark:/12345/profile-joao-almeida"
- `triple:profile_it19_2` → `datacite:isni` → "0000000121032683"

## CQ_19.7

Retrieve the profiles of registered GoTriple users who are open to collaboration.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>

SELECT ?profile WHERE {
  ?profile a triple:Profile ;
           triple:registeredUser true ;
           triple:openToCollaboration true .
}
```

**Expected result:**
- `triple:profile_it19_1`

## CQ_19.8

Retrieve the profile-card attributes of a registered user: self-description, pronouns, photo, personal web page and date of the last GoTriple update.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?profile ?description ?pronouns ?photo ?url ?lastUpdate WHERE {
  ?profile a triple:Profile ;
           triple:registeredUser true .
  OPTIONAL { ?profile schema:description ?description . }
  OPTIONAL { ?profile triple:pronouns ?pronouns . }
  OPTIONAL { ?profile schema:image ?photo . }
  OPTIONAL { ?profile schema:url ?url . }
  OPTIONAL { ?profile schema:dateModified ?lastUpdate . }
}
```

**Expected result:**
- `triple:profile_it19_1` → "Digital historian working on computational analysis of cultural heritage collections." → "she/her" → <https://gotriple.eu/media/profile/sofia-rossi.jpg> → <https://sofia-rossi.example.org> → "2026-06-15"

## CQ_19.9

Retrieve the documents a profile is the author of (the author_of field, obtained as the inverse of schema:author).

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?profile ?document WHERE {
  ?document a triple:Document ;
            schema:author ?profile .
  ?profile a triple:Profile .
}
ORDER BY ?profile
```

**Expected result:**
- `triple:profile_it19_1` → `triple:document_it19_1`
- `triple:profile_it19_2` → `triple:document_it19_1`

## CQ_19.10

Retrieve the internal id and the GoTriple persistent identifier (the `id` and `pid` fields) of a profile.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://www.essepuntato.it/2010/06/literalreification/>

SELECT ?profile ?internalId ?pid WHERE {
  ?profile a triple:Profile ;
           datacite:hasIdentifier ?internalIdentifier .
  ?internalIdentifier datacite:usesIdentifierScheme triple:internal_id_schema ;
                      litre:hasLiteralValue ?internalId .
  OPTIONAL {
    ?profile datacite:hasIdentifier ?pidIdentifier .
    ?pidIdentifier datacite:usesIdentifierScheme datacite:ark ;
                   litre:hasLiteralValue ?pid .
  }
}
ORDER BY ?profile
```

**Expected result:**
- `triple:profile_it19_1` → "sofia_rossi_x8KfvrDgWBlxpw8Ve9U5I" → "ark:/12345/profile-sofia-rossi"
- `triple:profile_it19_2` → "joao_almeida_p2QhtsFjYDnzrw7Xg1W7K" → "ark:/12345/profile-joao-almeida"