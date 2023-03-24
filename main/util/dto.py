from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.Integer(),
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
        'id': fields.Integer(),
        'name': fields.String(required=True),
        'is_active': fields.Boolean(required=True),
        'is_batsman': fields.Boolean(required=True),
        'is_bowler': fields.Boolean(required=True),
        'is_allrounder': fields.Boolean(required=True),
        'is_wicketkeeper': fields.Boolean(required=True)
    })


class TeamDto:
    api = Namespace('team', description='Event Team related operations')
    team = api.model('team', {
        'id': fields.Integer(),
        'name': fields.String(required=True),
        'is_active': fields.Boolean(),
        'created_date': fields.DateTime(),
        'last_modified_date': fields.DateTime(),
        'players': fields.List(fields.Integer, required=True)
    })


class EventDto:
    api = Namespace('event', description="Event related operations")
    event = api.model('event', {
        'id': fields.Integer(),
        'description': fields.String(),
        'home_team': fields.Integer(required=True),
        'away_team': fields.Integer(required=True),
        'start_time': fields.DateTime(required=True),
        'end_time': fields.DateTime(required=True)
    })