import vertex


class Edge:
    def __init__(self, source: vertex, destination: vertex, cost: int):
        self.source_vertex = source
        self.destination_vertex = destination
        self.cost = cost
