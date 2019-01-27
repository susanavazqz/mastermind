import json

from unittest import TestCase
from app import app
from models.game import Game


class TestApp(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.game = Game()

    def test_new_game(self):
        resp = self.app.post('/game')
        self.assertEqual(resp.status, '201 CREATED')

    def test_play_game(self):
        resp = self.app.post('game/{}/play'.format(self.game.id),
                             data=json.dumps(
                                 dict(code='["B", "R", "W", "P"]')),
                             content_type='application/json')

        self.assertEqual(resp.status, '200 OK')

    def test_play_is_not_close(self):
        resp = self.app.post('game/{}/play'.format(self.game.id),
                             data=json.dumps(
                                 dict(code='["B", "R", "W", "P"]')),
                             content_type='application/json')

        self.assertEqual(resp.status, '200 OK')

    def test_play_game_wrong_data_length(self):
        resp = self.app.post('game/{}/play'.format(self.game.id),
                             data=json.dumps(
                                 dict(code='["B", "R", "W"]')),
                             content_type='application/json')
        self.assertEqual(resp.status, '400 BAD REQUEST')

    def test_play_without_data(self):
        resp = self.app.post('game/{}/play'.format(self.game.id),
                             data=json.dumps(dict()),
                             content_type='application/json')
        self.assertEqual(resp.status, '400 BAD REQUEST')

    def test_play_game_not_found(self):
        game = self.app.post('game/-1/play',
                             data=json.dumps(
                                 dict(code='["B", "R", "W", "P"]')),
                             content_type='application/json')
        self.assertEqual(game.status, '404 NOT FOUND')
