"""

"""

import dataclasses
import json
import logging
import logging.config
import sys
import click
import navocab

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(name)s:%(levelname)s: %(message)s",
            "dateformat": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
            "propogate": False,
        },
    },
}

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "WARN": logging.WARNING,
    "ERROR": logging.ERROR,
    "FATAL": logging.CRITICAL,
    "CRITICAL": logging.CRITICAL,
}


def getLogger():
    return logging.getLogger("navocab")


def getDefaultVocabulary(vs, abbreviate=False):
    L = getLogger()
    vocabs = vs.vocabularies(abbreviate=abbreviate)
    vocabulary = vocabs[0]
    if len(vocabs) > 1:
        L.warning("More than one vocabulary in store. Using: %s", vocabulary)
    return vocabulary


@click.group()
@click.pass_context
@click.option(
    "-s", "--store", default="vocabularies.db", help="SQLite db for vocabularies"
)
@click.option("--verbosity", default="INFO", help="Logging level")
def main(ctx, store, verbosity) -> int:
    verbosity = verbosity.upper()
    logging_config["loggers"][""]["level"] = verbosity
    logging.config.dictConfig(logging_config)
    L = getLogger()
    ctx.ensure_object(dict)
    store_uri = f"sqlite:///{store}"
    L.info("Using store at: %s", store_uri)
    ctx.obj["store"] = navocab.Vocabulary(storage_uri=store_uri)
    return 0


@main.command("load")
@click.pass_context
@click.argument("uri")
def load(ctx, uri):
    """Load RDF from the provided local or remote URI."""
    L = getLogger()
    _s = ctx.obj["store"]
    L.info("Loading URI: %s", uri)
    _s.load(uri)
    L.info("Graph now has %s statements.", len(_s._g))


@main.command("namespaces")
@click.pass_context
@click.option(
    "-b",
    "--bind",
    default=None,
    help="Bind new prefix to namespace, like: 'eg=https://example.com/'",
)
def namespaces(ctx, bind):
    L = getLogger()
    _s = ctx.obj["store"]
    if bind is not None:
        p_uri = bind.split("=", 1)
        if len(p_uri) < 2:
            L.error("Insufficient parameters: %s", bind)
            L.info("Format the bind request like 'prefix=namspace'")
            return
        _s.bind(p_uri[0].strip(), p_uri[1].strip())
    for prefix, uri in _s.namespaces():
        print(f"{prefix} = {str(uri)}")


@main.command("vocabs")
@click.pass_context
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
def vocabularies(ctx, full_uri):
    """List the vocabulary URIs in the store."""
    _s = ctx.obj["store"]
    vocabs = _s.vocabularies(abbreviate=(not full_uri))
    for v in vocabs:
        print(v)


@main.command("concepts")
@click.option(
    "-v",
    "--vocabulary",
    default=None,
    help="URI of vocabulary, 'default' to load first available.",
)
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
@click.pass_context
def concepts(ctx, vocabulary, full_uri):
    """List the skos:Concept entities in the selected vocabulary."""
    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=False)
        L.info("Loaded default vocabulary: %s", vocabulary)
    concepts = _s.concepts(vocabulary, abbreviate=(not full_uri))
    for c in concepts:
        print(f"{c}")


@main.command("roots")
@click.pass_context
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
def vocabulary_root(ctx, full_uri):
    """Retrieve the vocabulary root term(s)."""
    _s = ctx.obj["store"]
    vocabs = _s.vocabularies(abbreviate=(not full_uri))
    for vocab in vocabs:
        roots = _s.getVocabRoot(vocab, abbreviate=(not full_uri))
        print(f"{vocab}")
        for root in roots:
            print(f"  {str(root)}")
        if len(roots) < 1:
            print("  No root terms in this vocabulary.")
        print()


@main.command("broader")
@click.option(
    "-v",
    "--vocabulary",
    default=None,
    help="URI of vocabulary, 'default' to load first available.",
)
@click.option("-d", "--depth", default=-1, help="Depth to traverse (default=all)")
@click.argument("concept")
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
@click.pass_context
def broader(ctx, vocabulary, concept, depth, full_uri):
    """Perform a depth first traversal of the vocabulary starting from CONCEPT."""

    def _broader(s, v, c, indent=0, level=0, max=100):
        ns = s.broader(c, v, abbreviate=(not full_uri))
        for n in ns:
            print(f"{indent*' '}{n}")
            if level < max:
                _broader(s, v, n, indent=indent + 2, level=level + 1, max=max)

    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=(not full_uri))
        L.info("Loaded default vocabulary: %s", vocabulary)
    if depth < 1:
        depth = 100
    _broader(_s, vocabulary, concept, max=depth)


@main.command("narrower")
@click.option(
    "-v",
    "--vocabulary",
    default=None,
    help="URI of vocabulary, 'default' to load first available.",
)
@click.option("-d", "--depth", default=-1, help="Depth to traverse (default=all)")
@click.argument("concept")
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
@click.pass_context
def narrower(ctx, vocabulary, concept, depth, full_uri):
    """Perform a depth first traversal of the vocabulary starting from CONCEPT."""

    def _narrower(s, v, c, indent=0, level=0, max=100):
        ns = s.narrower(c, v, abbreviate=(not full_uri))
        for n in ns:
            print(f"{indent*' '}{n}")
            if level < max:
                _narrower(s, v, n, indent=indent + 2, level=level + 1, max=max)

    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=(not full_uri))
        L.info("Loaded default vocabulary: %s", vocabulary)
    if depth < 1:
        depth = 100
    _narrower(_s, vocabulary, concept, max=depth)


@main.command("concept")
@click.argument("concept")
@click.pass_context
def get_concept(ctx, concept):
    """Print out a concept in JSON format."""
    _s = ctx.obj["store"]
    c = _s.concept(concept)
    print(json.dumps(dataclasses.asdict(c), indent=2))


@main.command("match")
@click.argument("query")
@click.option("-c", "--concepts-only", is_flag=True, help="Show only the concept URIs")
@click.option(
    "-p", "--predicate", default=None, help="Match only on objects of this predicate"
)
@click.pass_context
def matchconcepts(ctx, query, concepts_only, predicate):
    """Perform a full text search against literal values in the store.

    QUERY is an sqlite fts match expression
    """
    L = getLogger()
    _s = ctx.obj["store"]
    results = _s.match(query, predicate=predicate)
    if len(results) < 1:
        L.warning("No matches")
        return
    concepts = []
    # results are ordered by relevance
    for result in results:
        concept = str(result[0])
        if concept not in concepts:
            concepts.append(concept)
    for concept in concepts:
        if concepts_only:
            print(concept)
        else:
            vt = _s.concept(concept)
            print(json.dumps(dataclasses.asdict(vt), indent=2))
            print()


if __name__ == "__main__":
    sys.exit(main())
