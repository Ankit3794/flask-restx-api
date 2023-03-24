from main import db
from sqlalchemy import Column, Sequence, String, Integer, TIMESTAMP, Boolean

class Event(db.Model):
    id = Column(Integer(), Sequence('event_seq', start=1), primary_key=True)
    description = Column(String(50))
    home_team = Column(Integer, db.db.ForeignKey('team.id'), nullable=False)
    away_team = Column(Integer, db.db.ForeignKey('team.id'), nullable=False)
    winner_team = Column(Integer, db.db.ForeignKey('team.id'), default=None)
    is_completed = Column(Boolean, default=False)
    start_time = Column(TIMESTAMP, nullable=False)
    end_time = Column(TIMESTAMP, nullable=False)
