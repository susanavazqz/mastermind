from unittest import TestCase

from models.board import Board


class TestBoard(TestCase):
    def test_create_board(self):
        board = Board()
        self.assertTrue(Board.DEFAULT_CODE_LENGTH, board.code_length)
        self.assertEqual(Board.CODE_PEGS, board.code_pegs)
