from flask import Flask
from flask_restful import Api
from resources.game import GameResource

from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(GameResource, '/game', '/game/<int:game_id>')

if __name__ == '__main__':
    app.run(debug=True)
