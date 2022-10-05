"""
Part of the iSamples project.
"""
import dataclasses
import typing
import rdflib
import rdflib.plugins.sparql
import sqlalchemy

STORE_IDENTIFIER = "https://w3id.org/isample/vocabulary"
NS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "obo": "http://purl.obolibrary.org/obo/",
    "geosciml": "http://resource.geosciml.org/classifier/cgi/lithology",
}


def skosT(term):
    return rdflib.URIRef(f"{NS['skos']}{term}")


def rdfT(term):
    return rdflib.URIRef(f"{NS['rdf']}{term}")


def rdfsT(term):
    return rdflib.URIRef(f"{NS['rdfs']}{term}")


@dataclasses.dataclass
class VocabularyConcept:
    uri: str
    name: str
    label: list[str]
    definition: str
    broader: list[str]
    narrower: list[str]


class Vocabulary:
    _PFX = f"""
PREFIX skos: <{NS['skos']}>
PREFIX owl: <{NS['owl']}>
PREFIX rdf: <{NS['rdf']}>
PREFIX rdfs: <{NS['rdfs']}>
"""
    DEFAULT_FORMAT = "text/turtle"
    DEFAULT_STORE = "sqlite://"

    def __init__(
        self,
        storage_uri=DEFAULT_STORE,
        store_identifier=STORE_IDENTIFIER,
        purge_existing=False,
    ):
        self.origin = None
        self.storage_uri = storage_uri
        self.store_identifier = store_identifier
        self._g = None
        self._terms = {}
        self._litfts = ""
        self._literals = ""
        self._initialize_store(purge=purge_existing)

    def __len__(self):
        return len(self._g)

    def _initialize_store(self, purge=False):
        graph = rdflib.ConjunctiveGraph("SQLAlchemy", identifier=self.store_identifier)
        if purge:
            graph.destroy(self.storage_uri)
        graph.open(self.storage_uri, create=True)
        ident = graph.store._interned_id
        # sqlite specific:
        # Generate a full text search index of the literal statements
        # Triggers are used to keep the FTS up to date with changes to the literal table.
        self._literals = f"{ident}_literal_statements"
        self._litfts = f"{ident}_fts"
        sql = f"""CREATE VIRTUAL TABLE IF NOT EXISTS {self._litfts} 
        USING fts5 (object, content={self._literals}, tokenize='porter unicode61');"""
        graph.store.engine.execute(sql)
        sql = f"""CREATE TRIGGER IF NOT EXISTS fts_insert AFTER INSERT ON {self._literals}
        BEGIN
            INSERT INTO {self._litfts} (rowid,object) VALUES (new.rowid, new.object);
        END;"""
        graph.store.engine.execute(sql)

        sql = f"""CREATE TRIGGER IF NOT EXISTS fts_delete AFTER DELETE ON {self._literals}
        BEGIN
            INSERT INTO {self._litfts} ({self._litfts}, rowid, object) VALUES ('delete', old.rowid, old.object);
        END;"""
        graph.store.engine.execute(sql)

        sql = f"""CREATE TRIGGER IF NOT EXISTS fts_update AFTER UPDATE ON {self._literals}
        BEGIN
            INSERT INTO {self._litfts} ({self._litfts}, rowid, object) VALUES ('delete', old.rowid, old.object);
            INSERT INTO {self._litfts} (rowid, object) VALUES (new.rowid, new.object);
        END;
        """
        graph.store.engine.execute(sql)
        self._g = graph

    def load(
        self,
        source: str,
        format: str = DEFAULT_FORMAT,
        bindings: typing.Optional[dict] = None,
    ):
        self._g.parse(source, format=format)
        if bindings is not None:
            for k, v in bindings.items():
                self._g.bind(k, v)

    def vocabularies(self) -> list[rdflib.term.URIRef]:
        """List the vocabularies in the provided graph"""
        q = (
            Vocabulary._PFX
            + """SELECT ?s
        WHERE {
            ?s rdf:type skos:ConceptScheme .
        }"""
        )
        qres = self._g.query(q)
        res = []
        for r in qres:
            res.append(r[0])
        return res

    def getVocabRoot(self, v: str) -> list[str]:
        """Get top concept of the specific vocabulary.

        v is the URI of the vocabulary
        """
        q = rdflib.plugins.sparql.prepareQuery(
            Vocabulary._PFX
            + """SELECT ?s
        WHERE {
            ?s skos:topConceptOf ?vocabulary .
        }"""
        )
        qres = self._g.query(q, initBindings={"vocabulary": v})
        res = []
        for row in qres:
            res.append(row[0])
        return res

    def concepts(self, v: typing.Optional[str] = None) -> list[rdflib.term.URIRef]:
        """List the concept URIs in the specific vocabulary.

        Returns a list of the skos:Concept instances in the specified vocabulary
        as it exists in the current graph store.
        """
        if v is None:
            q = (
                Vocabulary._PFX
                + """SELECT ?s
            WHERE {
                ?s rdf:type skos:Concept .
            }"""
            )
            qres = self._g.query(q)
        else:
            q = (
                Vocabulary._PFX
                + """SELECT ?s
                WHERE {
                    ?s skos:inScheme ?vocabulary .
                    ?s rdf:type skos:Concept .
                }"""
            )
            qres = self._g.query(q, initBindings={"vocabulary": v})
        res = []
        for row in qres:
            res.append(row[0])
        return res

    def objects(self, subject: str, predicate: str) -> list[str]:
        q = rdflib.plugins.sparql.prepareQuery(
            Vocabulary._PFX
            + """SELECT ?o
        WHERE {
            ?subject ?predicate ?o .
        }"""
        )
        qres = self._g.query(
            q, initBindings={"subject": subject, "predicate": predicate}
        )
        res = []
        for row in qres:
            v = row[0]
            v = str(v).strip()
            if len(v) > 0:
                res.append(v)
        return res

    def broader(self, concept: str, v: typing.Optional[str] = None) -> list[str]:
        if v is None:
            q = rdflib.plugins.sparql.prepareQuery(
                Vocabulary._PFX
                + """SELECT ?s
            WHERE {
                ?child skos:broader ?s .
            }"""
            )
            qres = self._g.query(q, initBindings={"child": concept})
        else:
            q = rdflib.plugins.sparql.prepareQuery(
                Vocabulary._PFX
                + """SELECT ?s
            WHERE {
                ?s skos:inScheme ?vocabulary .
                ?child skos:broader ?s .
            }"""
            )
            qres = self._g.query(q, initBindings={"vocabulary": v, "child": concept})
        res = []
        # Should only ever be a single broader term in a well constructed taxonomy,
        # but who knows how well these things are constructed?
        for row in qres:
            res.append(row[0])
        return res

    def narrower(self, concept: str, v: typing.Optional[str] = None) -> list[str]:
        if v is None:
            q = rdflib.plugins.sparql.prepareQuery(
                Vocabulary._PFX
                + """SELECT ?s
            WHERE {
                ?s skos:broader ?parent .
            }"""
            )
            qres = self._g.query(q, initBindings={"parent": concept})
        else:
            q = rdflib.plugins.sparql.prepareQuery(
                Vocabulary._PFX
                + """SELECT ?s
            WHERE {
                ?s skos:inScheme ?vocabulary .
                ?s skos:broader ?parent .
            }"""
            )
            qres = self._g.query(q, initBindings={"vocabulary": v, "parent": concept})
        res = []
        for row in qres:
            res.append(row[0])
        return res

    def concept(self, term: str):
        if "#" in term:
            ab = term.split("#")
        else:
            ab = term.split("/")
        name = ab[-1]
        # _v = self.objects(term, skosT("inScheme"))[0]
        _v = None
        labels = self.objects(term, skosT("prefLabel"))
        labels += self.objects(term, skosT("label"))
        tmp = self.objects(term, skosT("definition"))
        definition = "\n".join(tmp)
        broader = self.objects(term, skosT("broader"))
        narrower = self.narrower(term, _v)
        return VocabularyConcept(
            uri=str(term),
            name=name,
            label=labels,
            definition=definition.strip(),
            broader=broader,
            narrower=narrower,
        )

    def match(self, q) -> list[tuple[rdflib.URIRef, rdflib.URIRef, str, float]]:
        """
        Return a list of subject,predicate,object,rank that match the provided FTS query.

        Rank is the sqlite FTS rank property, https://www.sqlite.org/fts5.html#the_bm25_function
        and indicates the relevance of the result to the query. Lower values (i.e. more negative)
        indicate higher relevance.
        """
        sql = sqlalchemy.text(
            f"""SELECT a.subject, a.predicate, a.object, b.rank FROM {self._literals} AS a
            INNER JOIN {self._litfts} AS b on a.rowid=b.rowid 
            WHERE {self._litfts} MATCH :query ORDER BY rank;"""
        )
        rows = self._g.store.engine.execute(sql, {"query": q})
        result = []
        for row in rows:
            result.append(
                (rdflib.URIRef(row[0]), rdflib.URIRef(row[1]), str(row[2]), row[3])
            )
        return result

    def resolve(self, uri: str):
        """
        WIP
        Lookup the specified uri.
        If not present in the graph try and retrieve from uri as URL.
        """
        # look for the object with iri in the current graph first
        res = []
        for t in self._g.predicate_objects(rdflib.URIRef(uri)):
            res.append(t)
        if len(res) > 0:
            return res
        g = rdflib.ConjunctiveGraph()
        self._g += g.parse(uri)
        for t in self._g.predicate_objects(rdflib.URIRef(uri)):
            res.append(t)
        return res
