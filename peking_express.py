from character import Character
from graph import Graph


class PekingExpress:
    budget = 0
    occupiedLocations = []
    currentTurn = 1
    path = []

    character = None

    # Read the input map, which is provided in Json format.
    # Initialize the given start_location as the initial position of your character.
    def __init__(self, jsonMap, s, b, o):
        self.pekingMap = init_map(jsonMap)
        self.character = Character(s)
        self.budget = b
        self.occupiedLocations = o

        self.solve()

    # After every move of your own, this function should update the currently. Occupied locations on your locally
    # maintained map. This is necessary for the availability checks of the critical locations.
    def updated_occupied_locations(self):
        self.occupiedLocations = self.occupiedLocations[self.currentTurn]

    # When it is your turn to move, compute and return the new location of your character.
    def next_move(self):
        print("Not finished.")
        # TODO: Finish next_move function.

    def solve(self):
        # TODO: Finish solve
        print(self.occupiedLocations)
        print(self.character.path)
        print(self.pekingMap)


def init_map(jsonMap):
    source = jsonMap['connections']['source']
    target = jsonMap['connections']['target']
    price = jsonMap['connections']['price']
    critical = jsonMap['locations']['critical']
    n = len(source)

    peking_map = Graph()

    # Populate graph.
    for i in range(n):
        peking_map.add_edge(source[i], target[i], price[i])

    for i in critical:
        peking_map.update_critical(i)

    return peking_map
