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
        self.pekingMap = init_map(json_map)
        self.character = Character(s)
        self.startLocation = s
        self.budget = b
        self.occupiedLocations = o

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
        solution = self.calculate_best_solution((None, None), self.currentTurn, [self.character.path[-1]],
                                                self.character.spent)

        # Add travel weight to spent.
        if solution[1] is not None and solution[1][0] != solution[1][1]:
            self.character.spent += self.pekingMap.get_vertex(solution[1][0]).weight(solution[1][1])

        # Return next point in shortest path to location.
        if solution[1] is not None:
            return solution[1][1]

        return None

    def calculate_best_solution(self, solution, turn, path, spent) -> tuple:
        """
        Calculate solutions.
        :param solution: the solution
        :param turn: current turn
        :param path: current path
        :param spent: what part of the budget has already been used.
        :return: list of all solutions
        """

        # If destination reached, add path and amount spent to solutions.
        if path[-1] == 88 and spent < self.budget:
            if solution[1] is None or len(path) < len(solution[1]) or (
                    len(solution[1]) == len(path) and solution[0] > spent):
                solution = (spent, path)
        # Else spent is under budget.
        elif spent < self.budget and (solution[1] is None or len(path) < len(solution[1])):
            # Get adjacent vertices.
            options = self.pekingMap.get_vertex(path[-1]).get_neighbours()
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
                    solution = self.calculate_best_solution(solution, turn + 1, path + [o], spent + price)
        return solution

    def solve(self):
        """
        Until we research the final node 88, we calculate a next move.
        """
        while self.character.path[-1] != 88:
            n = self.next_move()
            if n is None:
                print('Error: no solution found.')
                break
            self.character.path += [n]
            self.updated_occupied_locations()
            self.currentTurn += 1

    def get_path(self):
        return self.character.path

    def get_path_weight(self):
        return sum([self.pekingMap.get_vertex(i).weight(i + 1) for i in range(len(self.get_path()))])

    def get_path_length(self):
        return len(self.get_path())


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
