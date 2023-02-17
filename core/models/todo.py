from core import db
from typing import List


class ToDoModel(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f"ToDoModel(id={self.id}, content={self.content})"

    def json(self):
        return {
            "content": self.content
        }

    @classmethod
    def find_by_id(cls, _id) -> "ToDoModel":
        return ToDoModel.query.get(_id)

    @classmethod
    def find_all(cls) -> List["ToDoModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
