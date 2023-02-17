from flask_restx import Namespace, Resource

api = Namespace("user", description="User related operation")

users = {
    1: {
        "username": "ankit",
        "email": "ankit@gmail.com"
    },
    2: {
        "username": "riddhi",
        "email": "riddhi@gmail.com"
    }
}


@api.route('/')
class User(Resource):
    def get(self):
        return users


@api.route('/<string:user_id>')
class SingleUser(Resource):
    def get(self, user_id):
        if int(user_id) in users:
            return users.get(int(user_id))
        else:
            return {"message": "user not found"}, 201
