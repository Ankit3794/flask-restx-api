from .. import jwt, db
from ..model.token_blocklist import TokenBlocklist
from ..model.user import User
from flask_jwt_extended import create_access_token, get_jwt
from datetime import datetime, timezone


class AuthService:
    @staticmethod
    def login_user(data):
        user = User.query.filter_by(email=data.get('email')).first()
        if user and user.check_password(data.get('password')):
            auth_token = create_access_token(data['email'], additional_claims={"is_admin": user.is_admin})
            if auth_token:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'token': auth_token
                }
                return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'email or password does not match.'
            }
            return response_object, 401

    @staticmethod
    def logout_user():
        jti = get_jwt()["jti"]
        now = datetime.now(timezone.utc)
        db.session.add(TokenBlocklist(jti=jti, created_at=now))
        db.session.commit()
        return {'message': 'You are successfully logged out'}

    @staticmethod
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
        jti = jwt_payload["jti"]
        token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

        return token is not None
