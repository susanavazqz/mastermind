from flask_restful import Resource, reqparse

from models.game import Game


class GameResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('code',
                        type=str,
                        required=True,
                        help="This field is mandatory. "
                             "Ex: 'code': 'B,P,W,R'")

    def post(self):
        game = Game()
        try:
            game.save_to_db()
            return {'id': game.id, 'message': 'Game has been created'}, 201
        except:
            return {'message': 'An error occurred creating game'}, 500

    def put(self, game_id):
        game = Game.find_game(game_id)
        if not game:
            return {'message': 'Game not found'}, 404
        if game.close:
            return {'message': 'Game close'}, 400

        data = GameResource.parser.parse_args()
        game.codebreaker.guess_code = data.get('code')
        if len(game.codebreaker.guess_code.split(',')) != game.board.code_length:
            return {'message': 'Code must be {} length'.format(
                game.board.code_length)}, 400

        result = game.play_game()
        return {
            'id': game_id,
            'code': data.get('code'),
            'result': result,
        }, 200

