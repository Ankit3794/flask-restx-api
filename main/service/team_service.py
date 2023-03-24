from main import db
from main.util.db_utils import DBUtils
from ..model.team import Team
from ..model.player import Player

class TeamService:
    @staticmethod
    def get_all_teams():
        return Team.query.all()
    
    @staticmethod
    def add_team(data):
        player_ids = data['players']
        players = db.session.query(Player).filter(Player.id.in_(player_ids)).all()
        team = Team(name=data['name'], players=players)
        DBUtils.save_to_db(team)
        return team, 201