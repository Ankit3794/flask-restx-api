from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt

from ..service.auth_service import AuthService
from ..util.dto import AuthDto

api = AuthDto.api
_user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    @api.doc('user login')
    @api.expect(_user_auth, validate=True)
    def post(self):
        data = request.json
        return AuthService.login_user(data)


@api.route('/logout')
class UserLogout(Resource):
    @api.doc('user logout')
    @api.response(200, 'Successfully logged out')
    @jwt_required()
    def delete(self):
        return AuthService.logout_user()


