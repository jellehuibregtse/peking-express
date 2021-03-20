class character:
    path = []
    location = 0

    def __init__(self, startlocation):
        self.location = startlocation

class pekingExpress:
    pekingMap = {}
    budget = 0
    occupiedLocations = []
    currentTurn = 1

    character = None

    # read the input map, which is provided in Json format
    # initialize the given startlocation as the initial position of your character
    def __init__(self, m, s, b, o):
        self.pekingMap = m
        self.character = character(s)
        self.budget = b
        self.occupiedLocations = o
        
        self.solve()

    # after every move of your own, this function should update the currently
    # occupied locations on your locally maintained map. This is necessary for the
    # availability checks of the critical locations.
    def updateOccupiedLocations(self):
        self.occupiedLocations = self.occupiedLocations[self.currentTurn]
        
    # when it is your turn to move, compute and return the new location of your character
    def nextMove(self):
        print("not finished")
        
    def solve(self):
        while self.character.location != self.pekingMap['connections']['target'][-1]:
            self.myPath = self.myPath + self.nextMove()
            self.updateOccupiedLocations()
        print(self.occupiedLocations)
        print(self.character.path)
        print(self.pekingMap)