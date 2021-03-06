from unittest import TestCase

from models.game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_create_game(self):
        self.assertTrue(self.game)

    def test_create_open_game(self):
        self.assertEqual(self.game.close, False)

    def test_finish_game(self):
        self.game.codebreaker.guess_code = 'B,P,W,R'
        self.game.codemaker.code = 'B,P,W,R'
        self.assertEqual(self.game._is_finished_game(), True)

    def test_get_black_pegs(self):
        self.game.codebreaker.guess_code = 'B,P,W,R'
        self.game.codemaker.code = 'B,Y,W,R'

        self.assertEqual(self.game.get_black_pegs(), 3)

    def test_get_white_pegs(self):
        self.game.codebreaker.guess_code = 'B,P,W,R'
        self.game.codemaker.code = 'P,B,W,R'

        self.assertEqual(self.game.get_white_pegs(), 2)

    def test_is_finished_game(self):
        self.game.codebreaker.guess_code = 'B,P,W,R'
        self.game.codemaker.code = 'B,P,W,R'

        self.assertTrue(self.game._is_finished_game())
