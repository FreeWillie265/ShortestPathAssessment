from vertex import Vertex


class Edge:
    def __init__(self, source: Vertex, destination: Vertex, cost: int):
        self.source_vertex = source
        self.destination_vertex = destination
        self.cost = cost
