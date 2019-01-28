import random

from db import db
from models.board import Board


class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer)

    def __init__(self):
        self.points = 0

    def add_point(self):
        self.points += 1

    def save_to_db(self):
        db.session.add(self)
        db.session.flush()

    @classmethod
    def find_game(cls, player_id):
        return db.session.query(Player).get(player_id)


class CodeMaker(Player):
    __tablename__ = 'codemaker'
    id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    code = db.Column(db.String)

    def __init__(self):
        super().__init__()
        self.code = ''.join(random.sample(list(Board.CODE_PEGS.values()),
                                          Board.DEFAULT_CODE_LENGTH))


class CodeBreaker(Player):
    __tablename__ = 'codebreaker'
    id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    guess_code = db.Column(db.String)

    def __init__(self):
        super().__init__()
        self.guess_code = None
