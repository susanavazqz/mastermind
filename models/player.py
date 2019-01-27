import random

from models.board import Board


class Player:
    def __init__(self):
        self.points = 0

    def add_point(self):
        self.points += 1


class CodeMaker(Player):
    def __init__(self):
        super().__init__()
        self.code = ','.join([random.choice(list(Board.CODE_PEGS.values()))
                             for _ in range(Board.DEFAULT_CODE_LENGTH)])


class CodeBreaker(Player):
    def __init__(self):
        super().__init__()
        self.guess_code = None
