from flask_restx import Api
from .user_controller import api as ns1
from .auth_controller import api as ns2
from .player_controller import api as ns3
from .expense_controller import api as ns4

api = Api(
    title="Fantasy Cricket API"
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(ns4)