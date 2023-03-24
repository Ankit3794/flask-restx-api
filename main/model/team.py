from main import db
from sqlalchemy import Boolean, Column, Integer, String, Sequence, TIMESTAMP
from datetime import datetime
from .tables import team_player

class Team(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    created_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_modified_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    players = db.relationship('Player', secondary=team_player, lazy='subquery', backref=db.backref('teams', lazy=True))