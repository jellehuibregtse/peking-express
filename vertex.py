class Vertex:
    """
    A vertex v in V. All neighbours are connected by edges.
    """

    def __init__(self, index, critical=False):
        self.index = index
        self.critical = critical
        # A dict of node and weight.
        self.neighbours = {}

    def add_neighbour(self, vertex, weight=0):
        self.neighbours[vertex] = weight

    def remove_neighbour(self, vertex):
        del self.neighbours[vertex]

    def get_neighbours(self):
        return list(self.neighbours.keys())

    def weight(self, vertex):
        return self.neighbours[vertex]

    def set_critical(self, critical):
        self.critical = critical
