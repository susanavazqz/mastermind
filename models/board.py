

class Board:
    CODE_PEGS = {
        'black': 'B',
        'white': 'W',
        'red': 'R',
        'yellow': 'Y',
        'purple': 'P'
    }

    DEFAULT_CODE_LENGTH = 4

    def __init__(self, code_pegs=CODE_PEGS, code_length=DEFAULT_CODE_LENGTH):
        self.code_pegs = code_pegs
        self.code_length = code_length
