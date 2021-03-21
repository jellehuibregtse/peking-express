from character import Character


class PekingExpress:
    pekingMap = {}
    budget = 0
    occupiedLocations = []
    currentTurn = 1
    path = []

    character = None

    # Read the input map, which is provided in Json format.
    # Initialize the given start_location as the initial position of your character.
    def __init__(self, m, s, b, o):
        self.pekingMap = m
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
        while self.character.location != self.pekingMap['connections']['target'][-1]:
            self.path = self.path + self.next_move()
            self.updated_occupied_locations()
        print(self.occupiedLocations)
        print(self.character.path)
        print(self.pekingMap)
