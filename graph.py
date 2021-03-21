class Graph:
    def __init__(self, n):
        # We store the graph in an adjacency list: u -> (v, w).
        self.adjList = {}
        self.num_vertices = n

    def add_edge(self, u, v, w):
        """
        An edge going from vertex u -> v and v -> u with weight w.
        Note that we assume this is an undirected graph.

        :param u: vertex
        :param v: vertex
        :param w: weight
        """

        # We add vertex u.
        if u in self.adjList.keys():
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

        # We add vertex v.
        if v in self.adjList.keys():
            self.adjList[v].append((u, w))
        else:
            self.adjList[v] = [(u, w)]

    def print_graph(self):
        """
        We print the graph: u -> v(w)
        """
        for u in self.adjList:
            print(u, "->", " -> ".join(str(f"{v}({w})") for v, w in self.adjList[u]))
