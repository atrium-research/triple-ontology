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
- `triple:profile_it19_1` → "Sofia", "Rossi"

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

Retrieve the thesaurus keywords a profile declares to know about, with their names.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX schema: <https://schema.org/>

SELECT ?profile ?keyword ?name WHERE {
  ?profile a triple:Profile ;
           schema:knowsAbout ?keyword .
  ?keyword a schema:DefinedTerm ;
           schema:name ?name .
}
```

**Expected result:**
- `triple:profile_it19_1` → `triple:kw_distant-reading_it19` → "Distant reading"@en
- `triple:profile_it19_1` → `triple:kw_distant-reading_it19` → "Lettura distante"@it

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

Retrieve the persistent identifiers of the persons behind GoTriple profiles, with their scheme and value, excluding the internal Elasticsearch id (whose scheme is the local resource one).

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?profile ?scheme ?value WHERE {
  ?profile a triple:Profile ;
           datacite:hasIdentifier ?identifier .
  ?identifier datacite:usesIdentifierScheme ?scheme ;
              litre:hasLiteralValue ?value .
  FILTER (?scheme != datacite:local-resource-identifier-scheme)
}
ORDER BY ?profile ?scheme
```

**Expected result:**
- `triple:profile_it19_1` → `datacite:orcid` → "0000-0002-1825-0097"
- `triple:profile_it19_1` → `triple:gotriple_id_schema` → "sofia_rossi_operas_0001"
- `triple:profile_it19_1` → `triple:idref_schema` → "123456789"
- `triple:profile_it19_2` → `datacite:isni` → "0000000121032683"

## CQ_19.10

Retrieve the internal id and the GoTriple persistent identifier (the `id` and `pid` fields) of a profile.

```sparql
PREFIX triple: <https://gotriple.eu/ontology/triple/>
PREFIX datacite: <http://purl.org/spar/datacite/>
PREFIX litre: <http://purl.org/spar/literal/>

SELECT ?profile ?internalId ?pid WHERE {
  ?profile a triple:Profile ;
           datacite:hasIdentifier ?internalIdentifier .
  ?internalIdentifier a triple:ID ;
                      litre:hasLiteralValue ?internalId .
  OPTIONAL {
    ?profile datacite:hasIdentifier ?pidIdentifier .
    ?pidIdentifier a triple:PID ;
                   litre:hasLiteralValue ?pid .
  }
}
ORDER BY ?profile
```

**Expected result:**
- `triple:profile_it19_1` → "sofia_rossi_x8KfvrDgWBlxpw8Ve9U5I", "ark:/12345/profile-sofia-rossi"
- `triple:profile_it19_2` → "joao_almeida_p2QhtsFjYDnzrw7Xg1W7K", (no pid in this example)

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
- `triple:profile_it19_1` → "Digital historian working on computational analysis of cultural heritage collections."@en, "she/her", `https://gotriple.eu/media/profile/sofia-rossi.jpg`, `https://sofia-rossi.example.org`, "2026-06-15"^^xsd:date

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
