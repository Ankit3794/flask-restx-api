from flask import Flask
from core.apis import api
from core import db
from core.models.todo import ToDoModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SECRET_KEY'] = "1234532"

api.init_app(app)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
