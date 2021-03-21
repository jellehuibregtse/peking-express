from priority_queue import PriorityQueue
import sys


class Graph:
    def __init__(self, n):
        # We store the graph in an adjacency list: u -> (v, w).
        self.adjList = {}
        self.num_vertices = n
        # To store the distance from the source vertex
        self.dist = [0] * n
        # To store the path
        self.path = [-1] * n

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

    def dijkstra(self, source):
        """
        Implementation of Dijkstra's shortest path algorithm using a priority queue.
        :param source: source vertex.
        """

        # Reset the path list.
        self.path = [-1] * self.num_vertices
        # Source is the source node.
        self.dist[source] = 0

        Q = PriorityQueue()
        Q.insert((0, source))

        for u in self.adjList.keys():
            if u != source:
                # Infinity.
                self.dist[u] = sys.maxsize
                self.path[u] = -1

        while not Q.empty():
            # Get node with the minimum distance from source.
            u = Q.extract_min()

            # Update the distance of all neighbours of u and if their distance was infinity before push them to the
            # queue.
            for v, w in self.adjList[u]:
                distance = self.dist[u] + w
                if self.dist[v] > distance:
                    if self.dist[v] == sys.maxsize:
                        Q.insert((distance, v))
                    else:
                        Q.decrease_key((self.dist[v], v), distance)

                    self.dist[v] = distance
                    self.path[v] = u

        self.print_distance(source)

    def print_distance(self, source):
        """
        Print the distance from each node to the vertex.
        :param source: source vertex.
        """
        print(f"Distance from node: {source}")
        for u in range(self.num_vertices):
            print(f"Node {u} has distance {self.dist[u]}")

    def print_path(self, source, destination):
        """
        Print shortest path from source to destination.
        :param source: source vertex.
        :param destination: destination vertex.
        """
        # This only works after calling dijkstra.
        path = []
        cost = 0
        temp = destination

        while self.path[temp] != -1:
            path.append(temp)
            if temp != source:
                for v, w in self.adjList[temp]:
                    if v == self.path[temp]:
                        cost += w
                        break
            temp = self.path[temp]
        path.append(source)
        path.reverse()

        print(f"Path from {source} to {destination}")
        for u in path:
            print(f"{u}", end=" ")
            if u != destination:
                print("-> ", end="")

        print("\nTotal cost of path: ", cost)
