from character import Character
from graph import Graph


class PekingExpress:
    budget = 0
    occupiedLocations = []
    currentTurn = 1
    character = None

    # Read the input map, which is provided in Json format.
    def __init__(self, json_map, s, b, o):
        """
        Read the input JSON map and call init_map which converts to a graph.
        :param json_map: input map (graph).
        :param s: start location.
        :param b: budget
        :param o: occupied locations.
        """
        self.solutions = []
        self.pekingMap = init_map(json_map)
        self.character = Character(s)
        self.budget = b
        self.occupiedLocations = o

        self.solve()

        print(self.character.path)

    def updated_occupied_locations(self):
        """
        After every move of your own, update the currently occupied locations, by adding your move.
        """
        if len(self.occupiedLocations) > self.currentTurn:
            self.occupiedLocations[self.currentTurn] += [self.character.path[-1]]
        else:
            self.occupiedLocations += [[self.character.path[-1]]]

    def next_move(self):
        """
        Compute the next move of your character.
        :return: the new location.
        """

        # Calculate all paths to destination from current location and time.
        self.calculate_solutions(self.currentTurn, [self.character.path[-1]], self.character.spent)

        # Get the shortest path to the destination from all the paths.
        shortest = None
        shortest_budget = 0
        shortest_path = self.character.path[-1]
        for s in self.solutions:
            # If the distance is from solution is shorter than current solution, set shortest solution to solution.
            if shortest is None or len(s[1]) < shortest:
                shortest = len(s[1])
                shortest_path = s[1]
            # If the distance is from solution is equal to current solution and price is lower, set shortest solution
            # to solution.
            elif len(s[1]) == shortest_budget > s[0]:
                shortest_path = s[1]

        # Add travel weight to spent.
        if shortest_path[0] != shortest_path[1]:
            self.character.spent += self.pekingMap.get_vertex(shortest_path[0]).weight(shortest_path[1])

        # Return next point in shortest path to location.
        return shortest_path[1]

    def calculate_solutions(self, turn, path, spent):
        """
        Calculate solutions.
        :param turn: current turn
        :param path: current path
        :param spent: what part of the budget has already been used.
        :return:
        """

        # If destination reached, add path and amount spent to solutions.
        if path[-1] == 88 and spent < self.budget:
            self.solutions.append((spent, path))
        # Else spent is under budget.
        elif spent < self.budget:
            # Get adjacent vertices.
            options = list(self.pekingMap.get_vertex(path[-1]).get_neighbours())
            # Can stay on same location if any of the next options are occupied and vital.
            if turn <= len(self.occupiedLocations):
                for o in options:
                    if o in self.occupiedLocations[turn - 1] and self.pekingMap.get_vertex(o).critical:
                        options = options + [path[-1]]
                        break
            # If it's not occupied and vital continue path.
            for o in options:
                if turn > len(self.occupiedLocations) or (
                        not (self.pekingMap.get_vertex(o).critical and o in self.occupiedLocations[turn - 1])):
                    price = self.pekingMap.get_vertex(path[-1]).weight(o) if o != path[-1] else 0
                    self.calculate_solutions(turn + 1, path + [o], spent + price)

    def solve(self):
        """
        Until we research the final node 88, we calculate a next move.
        """
        while self.character.path[-1] != 88:
            self.character.path += [self.next_move()]
            self.updated_occupied_locations()
            self.currentTurn += 1


def init_map(json_map):
    """
    Initialize graph from JSON map.
    :param json_map: JSON map.
    :return: a graph.
    """
    source = json_map['connections']['source']
    target = json_map['connections']['target']
    price = json_map['connections']['price']
    critical = json_map['locations']['critical']
    n = len(source)

    peking_map = Graph()

    # Populate graph.
    for i in range(n):
        peking_map.add_edge(source[i], target[i], price[i])

    for i in critical:
        peking_map.update_critical(i)

    return peking_map


if __name__ == "__main__":
    test = PekingExpress({"locations": {"number": 4, "critical": [3]},
                          "connections": {"source": [1, 1, 1, 2, 3], "target": [2, 3, 88, 3, 88],
                                          "price": [1, 3, 7, 1, 1]}}, 1, 5, [[2, 3], [3], [88], [88]])
