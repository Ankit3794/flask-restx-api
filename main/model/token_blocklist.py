from main import db
from sqlalchemy import Column, String, Integer, TIMESTAMP


class TokenBlocklist(db.Model):
    id = Column(Integer, primary_key=True)
    jti = Column(String(36), nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False)
