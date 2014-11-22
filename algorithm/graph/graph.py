from collections import defaultdict


class Vertex:
    def __init__(self, vid, value):
        self.vid = vid
        self.value = value
        self.meta = {}

    def visit(self):
        self.meta["visited"] = True

    def visited(self):
        if self.meta.has_key("visited"):
            return self.meta["visited"]
        return False


class Graph:
    def __init__(self, es, vs=[]):
        self.vertices = {}
        self.alist = defaultdict(list)

        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        self.vertices[v.vid] = v

    def add_edge(self, e):
        v1, v2 = e
        if not self.has_vertex(v1): self.add_vertex(v1)
        if not self.has_vertex(v2): self.add_vertex(v2)
        self.alist[v1.vid].append(v2.vid)
        self.alist[v2.vid].append(v1.vid)

    def has_vertex(self, v):
        return self.vertices.has_key(v.vid)

    def neighbors(self, v):
        return [self.vertices[vid] for vid in self.alist[v.vid]]

    def adjacent(self, v1, v2):
        return v2.vid in self.alist[v1.vid]


def reset_node_status(g):
    for v in g.vertices.values():
        v.meta = {}


def shortest(g, v1, v2):
    """
    BFS find shortest path from v1 to v2

    g  - graph
    v1 - vertex
    v2 - vertex

    Return Int|None  number of steps from v1 to v2.
                     Or none if no such path.
    """

    def next_level_vertices(vs):
        nvs = []
        for v in vs:
            nvs.extend(g.neighbors(v))
        nvs = set(nvs)

        return [v for v in nvs if not v.visited()]

    found = False
    level = 0
    froms = [v1]

    while froms and (not found):
        level += 1

        # check this layer
        for v in froms:
            v.visit()
            if g.adjacent(v, v2):
                found = True
                break

        # goto next layer
        froms = next_level_vertices(froms)

    reset_node_status(g)
    if found:
        return level

    return None


if __name__ == "__main__":

    # A-----B------C
    # |     |      |
    # +-----D------E

    a = Vertex(1, "a")
    b = Vertex(2, "b")
    c = Vertex(3, "c")
    d = Vertex(4, "d")
    e = Vertex(5, "e")
    edges = [
        [a, b],
        [a, d],
        [b, c],
        [b, d],
        [d, e],
        [c, e]
    ]
    g = Graph(edges)

    print shortest(g, a, c) == 2
    print shortest(g, a, e) == 2
    print shortest(g, b, e) == 2
    print shortest(g, c, e) == 1
