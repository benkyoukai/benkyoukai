import sys
import os
sys.path.append(os.path.abspath("graph"))
from graph import Graph
from graph import Vertex
from graph import getid

class DirectedGraph(Graph):
    def add_edge(self, e):
        v1, v2 = e
        vid1, vid2 = getid(v1), getid(v2)

        if not self.has_vertex(vid1):
            self.add_vertex(v1)

        if not self.has_vertex(vid2):
            self.add_vertex(v2)

        self.alist[vid1].add(vid2)





