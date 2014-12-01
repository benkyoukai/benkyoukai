import sys
import os
sys.path.append(os.path.abspath("graph"))
from graph import Graph
from graph import Vertex
from graph import getid

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
