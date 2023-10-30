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

    def is_adjacent(self, vertex_1: int, vertex_2: int):
        """Check if two vertices are adjacent to each other.
        i.e. You can find an edge where the source is vertex 1
         and the destination is vertex two or vice versa"""
        for edge in self.edges:
            if (edge.source_vertex == self.vertices[vertex_1] and edge.destination_vertex == self.vertices[vertex_2]) or (edge.source_vertex == self.vertices[vertex_2] and edge.destination_vertex == self.vertices[vertex_1]):
                return True
        return False
