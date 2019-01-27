from models.player import CodeBreaker, CodeMaker
from models.board import Board


class Game:
    def __init__(self):
        self.id = 1
        self.codemaker = CodeMaker()
        self.codebreaker = CodeBreaker()
        self.board = Board()
        self.close = False

    def finish_game(self):
        self.close = True

    @staticmethod
    def find_game(id):
        if id == 1:
            return Game()
        else:
            return False
