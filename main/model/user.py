from datetime import datetime
from main import db, bcrypt
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True)
    email = Column(String(100), unique=True)
    password_hash = Column(String(60), nullable=False)
    is_admin = db.Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    last_modified_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError("Password read access is not allowed")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
