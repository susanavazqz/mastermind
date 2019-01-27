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

    def get_black_pegs(self):
        return sum([1 for x, y in zip(self.codebreaker.guess_code.split(','),
                                      self.codemaker.code.split(','))
                    if x == y])

    def get_white_pegs(self):
        return len(set(self.codebreaker.guess_code.split(',')).intersection(
            set(self.codemaker.code.split(',')))) - self.get_black_pegs()

    def get_coincidence_result(self):
        return dict(black_pegs=self.get_black_pegs(),
                    white_pegs=self.get_white_pegs())

    def _is_finished_game(self):
        return self.get_black_pegs() == self.board.code_length

    def play_game(self):
        result = self.get_coincidence_result()
        if self._is_finished_game():
            self.finish_game()

        return result

    @staticmethod
    def find_game(id):
        if id == 1:
            return Game()
        else:
            return False
