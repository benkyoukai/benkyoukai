import sys
import os
sys.path.append(os.path.abspath("graph"))
sys.path.append(os.path.abspath("directed_graph"))
from directed_graph import DirectedGraph
from directed_graph import Vertex
from directed_graph import getid

def topological_sort(graph):
    vertices = graph.vertices.values()

    # A dirty work around.
    #
    # If curval is not mutable,
    # its value cannot be reassigned(changed) in the nested function.
    #
    # For more info: http://stackoverflow.com/questions/6198709/how-do-i-change-nesting-functions-variable-in-the-nested-function
    curval = [len(vertices)]
    visited = set([])

    def DFS(v):
        visited.add(v.vid)
        vids = graph.neighbors(v)
        for vid in vids:
            if vid not in visited:
                DFS(graph.vertex(vid))

        v.value = curval[0]
        curval[0] -= 1

    for v in vertices:
        if v.vid not in visited:
            DFS(v)


if __name__ == "__main__":

    # A----->B----->C
    # |             ^
    # |             |
    # +----->D------+
    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    edges = [
        (A, B),
        (A, D),
        (B, C),
        (D, C),
    ]
    graph = DirectedGraph(edges=edges)
    topological_sort(graph)

    # ('A', 1) -> ('B', 3) -> ('C', 4)
    # ('A', 1) -> ('D', 2) -> ('C', 4)
    def dfspp(graph, start):
        def DFS(v):
            ns = graph.neighbors(v)
            lists = []
            for vid in ns:
                lists += DFS(graph.vertex(vid))

            if not lists:
                return [[(v.vid, v.value)]]
            return [[(v.vid, v.value)] + l for l in lists]

        lists = DFS(start)
        for l in lists:
            print " -> ".join(map(lambda t: str(t), l))

    dfspp(graph, A)
