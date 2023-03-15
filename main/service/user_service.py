from main import db
from main.model.user import User
from main.service.auth_service import AuthService
from main.util.db_utils import DBUtils
from flask_jwt_extended import get_jwt_identity

from main.util.exceptions import EntityNotFoundError, EntityAlreadyExists


class UserService:
    @staticmethod
    def save_new_user(data):
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            new_user = User(username=data['username'], email=data['email'], password=data['password'])
            DBUtils.save_to_db(new_user)
            return {"message": "successfully registered"}, 201
        else:
            raise EntityAlreadyExists('User with given email already exists')

    @staticmethod
    def get_all_user():
        return User.query.all()

    @staticmethod
    def get_user(_id):
        return User.query.get(_id)

    @staticmethod
    def update_password(data):
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        if not user:
            raise EntityNotFoundError("User not found")
        user.password = data['password']
        db.session.commit()
        AuthService.logout_user()
        return {"message": "Password updated successfully. Please login again!"}
