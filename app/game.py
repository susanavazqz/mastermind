

class Game:
    def __init__(self, codemaker, codebreaker):
        self.codemaker = codemaker
        self.codebreaker = codebreaker
        self.close = False

    def finish_game(self):
        self.close = True
