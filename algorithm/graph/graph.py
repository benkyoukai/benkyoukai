from collections import defaultdict


class Vertex:
    def __init__(self, vid, value=None):
        self.vid = vid
        self.value = value


class Graph:
    """
    Indirected Graph
    """

    def __init__(self, vertices=[], edges=[]):
        self.vertices = {}
        self.edges = defaultdict(dict)

        for v in vertices:
            self.addvertex(v)

        for e in edges:
            self.addedge(e)

    def getvertex(self, vid):
        """ Get vertex by vid """
        return self.vertices[vid]

    def getvertices(self):
        return self.vertices.values()

    def addvertex(self, v):
        """
        Add vertex to graph

        v - Vertex. Raise exception if v is not a Vertex object

        Return self
        """
        if not isinstance(v, Vertex):
            raise "Cannot add non-Vertex object to Graph"
        self.vertices[v.vid] = v
        return self

    def addedge(self, e):
        """
        Add edge to graph

        e - [Vertex|Vertex#id, Vertex|Vertex#id]
            If vertex dose not exists, add vertex object to graph.
            Raise Exception when Vertex#id is passed and there is no such vertex.

        Return self
        """
        v1, v2 = e
        vid1, vid2 = getid(v1), getid(v2)

        if not self.hasvertex(vid1):
            self.addvertex(v1)

        if not self.hasvertex(vid2):
            self.addvertex(v2)

        self.edges[vid1][vid2] = True
        self.edges[vid2][vid1] = True
        return self

    def hasvertex(self, v):
        """
        Check if vertex exists

        v - Vertex|Vertex#id

        Return Bool
        """
        vid = getid(v)
        return self.vertices.has_key(vid)

    def adjacent(self, v1, v2):
        """
        Check if two vertices is adjacent

        v1 - Vertex|Vertex#id
        v2 - Vertex|Vertex#id

        Return Bool
        """
        vid1, vid2 = getid(v1), getid(v2)
        return self.edges[vid1].has_key(vid2)

    def neighbors(self, v):
        """
        Get adjacent vertex ids

        v - Vertex|Vertex#id

        Return A list of Vertex#id
        """
        vid = getid(v)
        return self.edges[vid].keys()


def getid(v):
    if isinstance(v, Vertex):
        v = v.vid
    return v
