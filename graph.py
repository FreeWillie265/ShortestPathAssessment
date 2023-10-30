import vertex as Vertex
import edge as Edge


class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = []

    def add_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)

    def add_edge(self, edge: Edge):
        self.edges.append(edge)
