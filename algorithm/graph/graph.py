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
        self.alist = defaultdict(set)

        for v in vertices:
            self.add_vertex(v)

        for e in edges:
            self.add_edge(e)

    def vertex(self, vid):
        """ Get vertex by vid """
        return self.vertices[vid]

    def add_vertex(self, v):
        """
        Add vertex to graph

        v - Vertex. Raise exception if v is not a Vertex object

        Return self
        """
        if not isinstance(v, Vertex):
            raise "Cannot add non-Vertex object to Graph"
        self.vertices[v.vid] = v
        return self

    def add_edge(self, e):
        """
        Add edge to graph

        e - [Vertex|Vertex#id, Vertex|Vertex#id]
            If vertex dose not exists, add vertex object to graph.
            Raise Exception when Vertex#id is passed and there is no such vertex.

        Return self
        """
        v1, v2 = e
        vid1, vid2 = getid(v1), getid(v2)

        if not self.has_vertex(vid1):
            self.add_vertex(v1)

        if not self.has_vertex(vid2):
            self.add_vertex(v2)

        self.alist[vid1].add(vid2)
        self.alist[vid2].add(vid1)
        return self

    def has_vertex(self, v):
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
        return vid2 in self.alist[vid1]

    def neighbors(self, v):
        """
        Get adjacent vertex ids

        v - Vertex|Vertex#id

        Return A set of Vertex#id
        """
        vid = getid(v)
        return self.alist[vid]


def getid(v):
    if isinstance(v, Vertex):
        v = v.vid
    return v


def shortest(g, v1, v2):
    """
    BFS find shortest path from v1 to v2

    g  - Graph
    v1 - Vertex|Vertex#id
    v2 - Vertex|Vertex#id

    Return Int|None  number of steps from v1 to v2.
                     Or none if no such path.
    """

    vid1, vid2 = getid(v1), getid(v2)
    visited = set()
    found = False
    level = 0
    layer = [vid1]

    while layer and (not found):
        level += 1

        # check this layer
        for vid in layer:
            visited.add(vid)
            if g.adjacent(vid, vid2):
                found = True
                break

        # goto next layer
        vids = []
        for v in layer:
            vids.extend(g.neighbors(v))
        vids = set(vids)
        layer = [vid for vid in vids if vid not in visited]

    if found:
        return level

    return None


if __name__ == "__main__":

    # A-----B------C
    # |     |      |
    # +-----D------E
    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)
    e = Vertex(5)
    edges = [
        [a, b],
        [a, d],
        [b, c],
        [b, d],
        [d, e],
        [c, e],
    ]
    g = Graph(edges=edges)

    print shortest(g, a, c) == 2
    print shortest(g, a, e) == 2
    print shortest(g, b, e) == 2
    print shortest(g, c, e) == 1
