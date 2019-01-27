

class Player:
    def __init__(self):
        self.points = 0

    def add_point(self):
        self.points += 1


class CodeMaker(Player):
    def __init__(self):
        super().__init__()


class CodeBreaker(Player):
    def __init__(self):
        super().__init__()