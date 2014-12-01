import sys
import os
sys.path.append(os.path.abspath("weighted_graph"))
sys.path.append(os.path.abspath("../heap"))

from weighted_graph import WeightedGraph
from weighted_graph import Vertex
from weighted_graph import getid
from collections import defaultdict
from heap import Heap

def dijkstra(graph, source, target):
    source, target = getid(source), getid(target)
    visited = dict()
    heap = Heap([], lambda t1, t2: cmp(t1[0], t2[0]))
    heap.insert((0, source))

    while heap.size() > 0:
        val = s = None
        while not s:
            val, s = heap.popmin()
            if visited.has_key(s):
                val = s = None

        if s == target:
            return val
        visited[s] = val

        vs = graph.neighbors(s)
        for v in vs:
            if not visited.has_key(v):
                tmp = val + graph.getweight(s,v)
                heap.insert((tmp, v))

    return None

if __name__ == "__main__":

    #    2     4
    # A----->B----->C
    # |             ^
    # |  3          | 1
    # +----->D------+
    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    edges = [
        (A, B, 2),
        (A, D, 3),
        (B, C, 4),
        (D, C, 1),
    ]
    graph = WeightedGraph(edges=edges)
    print dijkstra(graph, A, D)

