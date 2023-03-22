from sqlalchemy.exc import IntegrityError
from main.model.player import Player
from main.util.db_utils import DBUtils
from main.util.exceptions import EntityAlreadyExists


class PlayerService:
    @staticmethod
    def add_player(data):
        try:
            if isinstance(data, dict):
                obj = Player(**data)
                DBUtils.save_to_db(obj)
            else:
                obj = [Player(**d) for d in data]
                DBUtils.save_to_db(obj, multiple=True)
            return obj, 201
        except IntegrityError:
            raise EntityAlreadyExists("Player already exists")

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
