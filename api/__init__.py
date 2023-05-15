from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hej'
    app.config['SQLALCHEMY_DATABASE_URI'] = "x"#f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .app import views

    app.register_blueprint(views, url_prefix='/')

    from . import models

    with app.app_context():
        db.create_all()

    return app