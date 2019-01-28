from db import db


class Board(db.Model):
    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    code_pegs = db.Column(db.String)
    code_length = db.Column(db.Integer)

    CODE_PEGS = {
        'black': 'B',
        'white': 'W',
        'red': 'R',
        'yellow': 'Y',
        'purple': 'P'
    }

    DEFAULT_CODE_LENGTH = 4

    def __init__(self, code_pegs=str(CODE_PEGS), code_length=DEFAULT_CODE_LENGTH):
        self.code_pegs = code_pegs
        self.code_length = code_length

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
