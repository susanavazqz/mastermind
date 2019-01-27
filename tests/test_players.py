from unittest import TestCase

from models.player import Player
from models.player import CodeMaker


class TestPlayers(TestCase):
    def setUp(self):
        self.player = Player()
        self.codemaker = CodeMaker()

    def test_player(self):
        self.assertEqual(self.player.points, 0)

    def test_add_points(self):
        self.player.add_point()
        self.assertEqual(self.player.points, 1)

    def test_new_codemaker(self):
        self.assertTrue(self.codemaker.code)
