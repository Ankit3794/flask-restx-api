from main import db
from sqlalchemy import Column, Integer, ForeignKey

team_player = db.Table(
    'team_player',
    Column('team_id', Integer, ForeignKey('team.id'), primary_key=True),
    Column('player_id', Integer, ForeignKey('player.id'), primary_key=True)
)