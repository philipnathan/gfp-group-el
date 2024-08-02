import os
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flasgger import Swagger

from .db import db
from .controllers.users import users_blueprint
from .controllers.sellers import sellers_blueprint
from .controllers.locations import locations_blueprint

load_dotenv()
migrate = Migrate()
jwt = JWTManager()

username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    app.register_blueprint(users_blueprint)
    app.register_blueprint(sellers_blueprint)
    app.register_blueprint(locations_blueprint)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    Swagger(app)

    with app.app_context():
        db.create_all()

    return app
