# Motivating Scenario (Iteration 5)

## Name
Discarded entities and documents cluster

## Description

### General description
One of the most frequent problems when harvesting and ingesting data from third-party data sources is 
the duplication of documents. Indeed, the external sources taken by the GoTriple platform to aggregate 
resources may contain overlapping data. One difficulty is recognising when two documents 
from different external sources are the same document. In the event that two or more similar documents 
are found to be the same, the concept of a cluster has been defined in GoTriple. 
The cluster is trivially a set of documents, to which an identifier corresponds, 
within which it is possible to retrieve documents with different identifiers but 
which can be traced back to the same document.

Another problem in GoTriple, again attributable to the number and diversity of external sources used, 
is the unusability of certain data. In particular, we refer to two entities: keywords and author. 
Some authors or keywords were decided not to be considered as useful for research purposes within 
the platform. For this reason, it was decided not to make them useful for searching and filtering documents.
For the sake of transparency, however, it was not decided to permanently remove them from the platform. 
The solution adopted is to highlight individuals, whether keywords or authors, by means of a flag. 
In this way, the data is preserved, but not made operational on the interface with which users interact.

### Technical specification

//

## Example 1

`document_7` and `document_89` are the same document. For this reason both belong to a single cluster `cluster_45`

## Example 2

`document_56` has as authors `author_5` and `author_567`. This last author was discarded.

## Example 3

`document_67` has as keywords `keyword_90` and `keyword_67`. Both keywords were discarded.