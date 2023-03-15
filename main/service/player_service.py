from main.model.player import Player
from main.util.db_utils import DBUtils


class PlayerService:
    @staticmethod
    def add_player(data):
        player = Player(**data)
        DBUtils.save_to_db(player)
        return player, 201

    @staticmethod
    def get_all():
        return Player.query.all()

    @staticmethod
    def get_player(id):
        player = Player.query.get(id)
        if not player:
            return {"message": "player with given id not found"}, 404
        else:
            return player
