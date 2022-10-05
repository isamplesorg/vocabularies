import os
import navocab


def test_load():
    NS = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "obo": "http://purl.obolibrary.org/obo/",
        "geosciml": "http://resource.geosciml.org/classifier/cgi/lithology",
    }

    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source, bindings=NS)
    assert len(v) == 33
    os.unlink(dest)


def test_vocabularies():
    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source)
    vocabs = v.vocabularies()
    assert len(vocabs) == 1
    assert str(vocabs[0]) == "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    os.unlink(dest)


def test_root():
    vocab = "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source)
    roots = v.getVocabRoot(vocab)
    assert len(roots) == 1
    assert str(roots[0]) == "https://w3id.org/isample/vocabulary/test/1/rootterm"
    os.unlink(dest)


def test_concepts():
    vocab = "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source)
    concepts = v.concepts(vocab)
    assert len(concepts) == 5
    concepts = v.concepts()
    assert len(concepts) == 6
    os.unlink(dest)


def test_narrower():
    vocab = "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    root = "https://w3id.org/isample/vocabulary/test/1/rootterm"
    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source)
    ns = v.narrower(root)
    assert len(ns) == 3
    ns = v.narrower(root, vocab)
    assert len(ns) == 2
    os.unlink(dest)


def test_broader():
    root = "https://w3id.org/isample/vocabulary/test/1/rootterm"
    term = "https://w3id.org/isample/vocabulary/test/1/level1b"
    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source)
    ns = v.broader(term)
    assert len(ns) == 1
    assert str(ns[0]) == root
    ns = v.broader(root)
    assert len(ns) == 0
    os.unlink(dest)


def test_match():
    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source)
    res = v.match("foobar")
    assert len(res) == 0
    res = v.match("once removed")
    assert len(res) == 2
    res = v.match("once OR twice")
    assert len(res) == 4
    os.unlink(dest)
