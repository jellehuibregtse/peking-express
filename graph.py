from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_edge(self, u, v, w):
        """
        An edge going from vertex u -> v and v -> u with weight w.
        Note that we assume this is an undirected graph.
        :param u: vertex
        :param v: vertex
        :param w: weight
        """

        # We add vertex u.
        if u not in self.vertices:
            self.vertices[u] = Vertex(u)

        # We add vertex v.
        if v not in self.vertices:
            self.vertices[v] = Vertex(v)

        self.vertices[u].add_neighbour(v, w)
        self.vertices[v].add_neighbour(u, w)

        self.num_vertices += 2

    def get_vertex(self, u):
        return self.vertices[u] if u in self.vertices else None

    def update_critical(self, u, critical=True):
        vertex = self.get_vertex(u)
        vertex.set_critical(critical)

    def print_graph(self):
        for u in self.vertices:
            print(u, "->",
                  " -> ".join(str(f"{v}({self.vertices[u].neighbours[v]})") for v in self.vertices[u].neighbours))


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(3, 2, 3)
    graph.add_edge(2, 1, 7)
    graph.add_edge(1, 88, 9)
    graph.add_edge(2, 88, 2)
    graph.add_edge(3, 88, 1)
    graph.print_graph()
