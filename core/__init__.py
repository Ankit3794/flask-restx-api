from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def create_app():
    from core.models.todo import ToDoModel
    from core.apis import api

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
    app.config['SECRET_KEY'] = "1234532"

    db.init_app(app)
    api.init_app(app)

    return app
