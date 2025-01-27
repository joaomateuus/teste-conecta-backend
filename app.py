from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from config import Config
from app.infra.db import db
from app.resources import auth

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
with app.app_context():
    from app.model import models
    db.create_all()

api = Api(app)
api.register_blueprint(auth.blueprint)
# api.register_blueprint(main_routes.bp_v1)

if __name__ == '__main__':
    app.run(debug=True)
