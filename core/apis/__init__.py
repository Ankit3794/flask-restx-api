from flask_restx import Api
from .todo import api as ns1
from .user import api as ns2

api = Api(
    title="Flask RestX"
)

api.add_namespace(ns1)
api.add_namespace(ns2)
