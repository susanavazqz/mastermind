from unittest import TestCase

from app.player import CodeBreaker
from app.player import CodeMaker
from app.game import Game


class TestGame(TestCase):
    def setUp(self):
        self.codeMaker = CodeMaker()
        self.codeBraker = CodeBreaker()

    def test_create_game(self):
        game = Game(self.codeMaker, self.codeBraker)

        self.assertEqual(game.close, False)

    def test_finish_game(self):
        game = Game(self.codeMaker, self.codeBraker)
        game.finish_game()

        self.assertEqual(game.close, True)
