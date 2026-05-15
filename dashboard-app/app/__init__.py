from flask import Flask
from flask_appbuilder import Model


from .extensions import appbuilder, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    with app.app_context():
        from app import models
        appbuilder.init_app(app, db.session)
        Model.metadata.create_all(db.engine)
        from . import views
    return app
