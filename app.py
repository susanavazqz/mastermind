from flask import Flask, jsonify, request
from flask_restful import reqparse
from models.game import Game


app = Flask(__name__)


@app.route('/')
def home():
    return 'Mastermind'


@app.route('/game', methods=['POST'])
def create_game():
    game = Game()
    return jsonify({'id': game.id, 'message': 'Game has been created'}), 201


@app.route('/game/<int:game_id>/play', methods=['PUT'])
def play_game(game_id):
    game = Game.find_game(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404

    if game.close:
        return jsonify({'message': 'Game close'}), 400

    parser = reqparse.RequestParser()
    parser.add_argument('code',
                        type=str,
                        required=True,
                        help="This field is mandatory. "
                             "Ex: 'code': 'B, P, W, R'")

    data = parser.parse_args()
    codebraker_code = data.get('code').split(",")
    if len(codebraker_code) != game.code_length:
        return jsonify(
            {'message': 'Code must be {} length'.format(game.code_length)}
        ), 400

    return jsonify({'message': 'TODO'}), 200


@app.route('/game/<int:game_id>/history', methods=['GET'])
def game_history(game_id):
    return jsonify({}), 501


if __name__ == '__main__':
    app.run()
