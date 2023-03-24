
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from main.service.event_service import EventService
from main.util import admin_required
from main.util.dto import EventDto


api = EventDto.api
_event = EventDto.event

@api.route('/')
class Event(Resource):
    @api.response(200, 'successfully get all active events')
    @api.doc("Get all Active events")
    @api.marshal_list_with(_event)
    @jwt_required()
    def get(self):
        return EventService.get_all_active_events()
    

    
    @api.response(201, "Event created successfully")
    @api.response(403, "User is not authorized")
    @api.doc("Create New Event")
    @api.expect(_event, validate=True)
    @admin_required()
    def post(self):
        data = request.json
        return EventService.create_event(data)



    