from flask_restx import Resource, Namespace, fields
from core.models.todo import ToDoModel

todos = [{
    "id": 1,
    "task": "flask with restx"
}, {
    "id": 2,
    "task": "flask with restx and resources"
}
]

api = Namespace('todo', description='todo related operations')

model = api.model('Model', {
    'id': fields.Integer,
    'content': fields.String,
})


@api.route('/')
class ToDO(Resource):
    @api.marshal_with(model)
    def get(self):
        return ToDoModel.find_all()


@api.route('/<string:todo_id>')
class ToDoSingle(Resource):
    @api.marshal_with(model)
    def get(self, todo_id):
        if todo := ToDoModel.find_by_id(int(todo_id)):
            return todo
        return {"message": f"No todo found with {todo_id}"}, 201
