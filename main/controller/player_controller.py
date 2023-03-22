from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from main.service.player_service import PlayerService
from main.util import admin_required
from main.util.dto import PlayerDto

api = PlayerDto.api
_player = PlayerDto.player


@api.route('/')
class PlayerList(Resource):

    @jwt_required()
    @api.marshal_list_with(_player)
    @api.doc("get all players")
    def get(self):
        return PlayerService.get_all()

    # @api.expect(_player, validate=True)
    @api.doc("add new player")
    @api.marshal_with(_player)
    @api.marshal_list_with(_player)
    @admin_required()
    def post(self):
        data = request.json
        return PlayerService.add_player(data)


@api.route('/<id>')
@api.param("id", description="Player ID")
class Player(Resource):
    @jwt_required()
    def get(self, id):
        return PlayerService.get_player(id)
