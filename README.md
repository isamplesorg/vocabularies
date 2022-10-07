# navocab

`navocab` implements tooling for navigating SKOS vocabulary definitions used in the iSamples project.

## Install

Checkout this repository:

```
git clone https://github.com/isamplesorg/navocab.git
```

Then run poetry install:

```
cd navocab
poetry install
```

## Operation

```
$ navocab --help
Usage: navocab [OPTIONS] COMMAND [ARGS]...

Options:
  -s, --store TEXT  SQLite db for vocabularies
  --verbosity TEXT  Logging level
  --help            Show this message and exit.

Commands:
  broader     Perform a depth first traversal of the vocabulary starting...
  concept     Print out a concept in JSON format.
  concepts    List the skos:Concept entities in the selected vocabulary.
  load        Load RDF from the provided local or remote URI.
  match       Perform a full text search against literal values in the...
  namespaces  List available namespaces and their prefixes.
  narrower    Perform a depth first traversal of the vocabulary starting...
  roots       Retrieve the vocabulary root term(s).
  vocabs      List the vocabulary URIs in the store.
```

### `load` 

`navocab` keeps loaded vocabularies in an sqlite cache. To load a vocabulary, provide the local or remote address of the vocabulary turtle file. The default database name is `vocabularies.db` in the current directory.

```
navocab load https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/sampledFeature.ttl
...
2022-10-07 10:58:30,435 navocab:INFO: Graph now has 180 statements.
```

Note: load currently issues a bunch of `SQLAlchemy.bind()` warnings. This is due to a pending update in one of the rdflib libraries.

To load all the current (2022-10-07) vocabularies and extensions:

```

```