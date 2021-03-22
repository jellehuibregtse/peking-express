class Character:
    path = []
    spent = 0

    def __init__(self, start_location):
        self.path = [start_location]
