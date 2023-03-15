from flask import request
from flask_restx import Resource
from ..util.dto import UserDto
from ..service.user_service import UserService
from flask_jwt_extended import jwt_required

api = UserDto.api
_user = UserDto.user
_user_update_pwd = UserDto.user_update_pwd


@api.route('/')
class UserList(Resource):
    @api.doc('List of registered users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return UserService.get_all_user()

    @api.response(201, 'User successfully created')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return UserService.save_new_user(data)

    @api.response(200, 'Password updated successfully')
    @api.doc('update password')
    @api.expect(_user_update_pwd, validate=True)
    @jwt_required()
    def patch(self):
        data = request.json
        return UserService.update_password(data)


@api.route('/<id>')
@api.param('id', 'User ID')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, id):
        user = UserService.get_user(id)
        if not user:
            api.abort(404)
        else:
            return user
