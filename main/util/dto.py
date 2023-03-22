from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='Email address'),
        'username': fields.String(required=True, description='Username'),
        'password': fields.String(required=True, description='Password')
    })
    user_update_pwd = api.model('user_update_password', {
        'password': fields.String(required=True, description='Password')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='Email address'),
        'password': fields.String(required=True, description='Password')
    })


class PlayerDto:
    api = Namespace('player', description='player related operation')
    player = api.model('player', {
        'name': fields.String(required=True),
        'is_active': fields.Boolean(required=True),
        'is_batsman': fields.Boolean(required=True),
        'is_bowler': fields.Boolean(required=True),
        'is_allrounder': fields.Boolean(required=True)
    })