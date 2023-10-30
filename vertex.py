INFINITY = 9999999
UNDEFINED = -1


class Vertex:
    def __init__(self, name):
        self.name = name
        self.path_length = INFINITY
        self.processed = False
        self.predecessor = UNDEFINED
