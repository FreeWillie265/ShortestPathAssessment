from vertex import Vertex
from edge import Edge
from helpers import UNDEFINED, INFINITY


class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = []

    def add_vertex(self, vertex_name):
        self.vertices.append(Vertex(vertex_name))

    def add_edge(self, source_index, dest_index, cost):
        source_vertex = self.vertices[source_index]
        dest_vertex = self.vertices[dest_index]
        self.edges.append(Edge(source_vertex, dest_vertex, cost))

    def is_adjacent(self, vertex_1: int, vertex_2: int):
        """Check if two vertices are adjacent to each other.
        i.e. You can find an edge where the source is vertex 1
         and the destination is vertex two or vice versa"""
        for edge in self.edges:
            if (edge.source_vertex == self.vertices[vertex_1] and edge.destination_vertex == self.vertices[
                vertex_2]) or (
                    edge.source_vertex == self.vertices[vertex_2] and edge.destination_vertex == self.vertices[
                vertex_1]):
                return True
        return False

    def get_vertex_index(self, vertex_name):
        for i in range(len(self.vertices)):
            if self.vertices[i].name == vertex_name:
                return i
        return UNDEFINED

    def get_weight(self, vertex_1: int, vertex_2: int):
        """Get the cost of the path from vertex 1 to vertex 2"""
        for edge in self.edges:
            if (edge.source_vertex == self.vertices[vertex_1] and edge.destination_vertex == self.vertices[
                vertex_2]) or (
                    edge.source_vertex == self.vertices[vertex_2] and edge.destination_vertex == self.vertices[
                vertex_1]):
                return edge.cost

    def min_cost_vertex_index(self):
        min_cost = INFINITY
        index = UNDEFINED

        for i in range(len(self.vertices)):
            if not self.vertices[i].processed and self.vertices[i].path_length < min_cost:
                min_cost = self.vertices[i].path_length
                index = i
        return index

    def dijkstras_algorithm(self, source_index):
        if source_index == UNDEFINED:
            return

        self.vertices[source_index].path_length = 0

        while True:
            current = self.min_cost_vertex_index()
            if current == UNDEFINED:
                return

            self.vertices[current].processed = True

            for i in range(len(self.vertices)):
                if self.is_adjacent(current, i) and not self.vertices[i].processed:
                    if self.vertices[current].path_length + self.get_weight(current, i) < self.vertices[i].path_length:
                        self.vertices[i].path_length = self.vertices[current].path_length + self.get_weight(current, i)
                        self.vertices[i].predecessor = current

    def print_shortest_path(self, source: int, dest: int):
        path = []
        count = 0

        while source != dest:
            path.append(self.vertices[dest].name)
            predecessor = self.vertices[dest].predecessor
            dest = predecessor
            count = count + 1

        print("The shortest path is: ")
        print(self.vertices[source].name, end="")
        for i in reversed(range(count)):
            print(" --> {}".format(path[i]), end="")
        print(".")

    def execute(self, source_name, dest_name):
        source_index = self.get_vertex_index(source_name)
        dest_index = self.get_vertex_index(dest_name)

        if source_index == UNDEFINED:
            print("Source vertex not found")
            return

        if dest_index == UNDEFINED:
            print("Destination vertex not found")
            return

        self.dijkstras_algorithm(source_index)
        self.print_shortest_path(source_index, dest_index)
