from unittest import TestCase

from models.player import CodeBreaker
from models.player import CodeMaker
from models.game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()
        self.codeMaker = CodeMaker()
        self.codeBreaker = CodeBreaker()

    def test_create_game(self):
        self.assertTrue(self.game.id)

    def test_create_open_game(self):
        self.assertEqual(self.game.close, False)

    def test_finish_game(self):
        self.game.finish_game()

        self.assertEqual(self.game.close, True)
