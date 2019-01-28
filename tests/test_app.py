import json

from app import app
from unittest import TestCase


class TestApp(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.game_id = self.app.post('/game').json.get('id')

    def make_put_data(self, game_id, data):
        return self.app.put('game/{}'.format(game_id),
                            data=json.dumps(dict(code=data)),
                            content_type='application/json')

    def test_new_game(self):
        resp = self.app.post('/game')
        self.assertEqual(resp.status, '201 CREATED')

    def test_play_game(self):
        resp = self.make_put_data(self.game_id, 'B,R,W,P')
        self.assertEqual(resp.status, '200 OK')

    def test_play_is_not_close(self):
        resp = self.make_put_data(self.game_id, 'B,R,W,P')

        self.assertEqual(resp.status, '200 OK')

    def test_play_game_wrong_data_length(self):
        resp = self.make_put_data(self.game_id, 'B,R,W')
        self.assertEqual(resp.status, '400 BAD REQUEST')

    def test_play_without_data(self):
        resp = self.make_put_data(self.game_id, dict())
        self.assertEqual(resp.status, '400 BAD REQUEST')

    def test_play_game_not_found(self):
        resp = self.make_put_data(-1, 'B,R,W,P')
        self.assertEqual(resp.status, '404 NOT FOUND')


