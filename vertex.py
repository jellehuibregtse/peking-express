class Vertex:
    def __init__(self, index, critical=False):
        self.index = index
        self.critical = critical
        self.occupied = False
        # A dict of node and weight.
        self.neighbours = {}

    def add_neighbour(self, vertex, weight=0):
        self.neighbours[vertex] = weight

    def remove_neighbour(self, vertex):
        del self.neighbours[vertex]

    def get_neighbours(self):
        return self.neighbours.keys()

    def available(self):
        return self.occupied and self.critical

    def weight(self, vertex):
        return self.neighbours[vertex]

    def set_critical(self, critical):
        self.critical = critical
