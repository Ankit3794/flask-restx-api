from sqlalchemy import Column, Integer, String, Boolean

from main import db


class Player(db.Model):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    is_active = Column(Boolean, default=False)
    is_batsman = Column(Boolean, default=False)
    is_bowler = Column(Boolean, default=False)
    is_allrounder = Column(Boolean, default=False)
    is_wicketkeeper = Column(Boolean, default=False)
