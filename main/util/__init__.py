from functools import wraps
from flask import abort
from flask_jwt_extended import get_jwt, verify_jwt_in_request

from main.util.exceptions import UserNotAuthorizedError


def admin_required():
    """
    This will check if logged_in user is admin or not.
    If admin then request will be fulfilled or else 403 response will be returned
    """

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_admin"]:
                return fn(*args, **kwargs)
            else:
                raise UserNotAuthorizedError("you are not authorized")

        return decorator

    return wrapper
