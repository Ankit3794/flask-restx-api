from main.controller import api
from main.util.exceptions import EntityNotFoundError, UserNotAuthorizedError, EntityAlreadyExists


@api.errorhandler(EntityNotFoundError)
def resource_not_found(error):
    return {'message': str(error)}, 404


@api.errorhandler(UserNotAuthorizedError)
def user_not_authorized(error):
    return {'message': str(error)}, 403


@api.errorhandler(EntityAlreadyExists)
def entity_already_exists(error):
    return {'message': str(error)}, 409
