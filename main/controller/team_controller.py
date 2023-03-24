
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from flask import request
from main.service.team_service import TeamService
from main.util import admin_required
from main.util.dto import TeamDto


api = TeamDto.api
_team = TeamDto.team

@api.route('/')
class Team(Resource):
    @api.doc("Get all team details")
    @api.response(200, "Successful response for fetching all team details")
    @api.marshal_list_with(_team)
    @jwt_required()
    def get(self):
        return TeamService.get_all_teams()
    
    @api.doc("Create New Team")
    @api.response(201, "team created successfully")
    @api.response(403, "user is not authroized")
    @api.marshal_list_with(_team, mask='id, name, is_active, created_date, last_modified_date')
    @api.expect(_team, validate=True)
    @admin_required()
    def post(self):
        data = request.json
        return TeamService.add_team(data)

