from models.player import CodeMaker
from models.player import CodeBreaker


class Game:
    CODE_LENGTH = 4

    def __init__(self):
        self.id = 1
        self.codemaker = CodeMaker()
        self.codebreaker = CodeBreaker()
        self.code_length = Game.CODE_LENGTH
        self.close = False

    def finish_game(self):
        self.close = True

    @staticmethod
    def find_game(id):
        if id == 1:
            return Game()
        else:
            return False
