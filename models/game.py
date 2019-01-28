from db import db

from models.board import Board
from models.player import CodeMaker, CodeBreaker


class Game(db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)
    codemaker_id = db.Column(db.Integer, db.ForeignKey('codemaker.id'))
    codemaker = db.relationship('CodeMaker', backref='codemaker_game',
                                foreign_keys=[codemaker_id])
    codebreaker_id = db.Column(db.Integer, db.ForeignKey('codebreaker.id'))
    codebreaker = db.relationship('CodeBreaker', backref='codebreaker_game',
                                  foreign_keys=[codebreaker_id])
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    board = db.relationship('Board', backref='board_game',
                            foreign_keys=[board_id])
    close = db.Column(db.Boolean)

    def __init__(self):
        self.codebreaker = CodeBreaker()
        self.codemaker = CodeMaker()
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

    @classmethod
    def find_game(cls, game_id):
        return db.session.query(Game).get(game_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
