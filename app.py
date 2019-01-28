from flask import Flask
from flask_restful import Api
from resources.game import GameResource


app = Flask(__name__)
api = Api(app)


api.add_resource(GameResource, '/game', '/game/<int:game_id>')

if __name__ == '__main__':
    app.run(debug=True)
