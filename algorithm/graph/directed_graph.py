import sys
import os
sys.path.append(os.path.abspath("graph"))
from graph import Graph
from graph import Vertex
from graph import getid

class DirectedGraph(Graph):
    def addedge(self, e):
        v1, v2 = e
        vid1, vid2 = getid(v1), getid(v2)

        if not self.hasvertex(vid1):
            self.addvertex(v1)

        if not self.hasvertex(vid2):
            self.addvertex(v2)

        self.edges[vid1][vid2] = True
