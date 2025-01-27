from flask import Flask
from flask_smorest import Api
from app.resources import auth
from app.infra.db import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    from app.model import models
    db.create_all()

api = Api(app)
api.register_blueprint(auth.blueprint)
# api.register_blueprint(main_routes.bp_v1)

if __name__ == '__main__':
    app.run(debug=True)
