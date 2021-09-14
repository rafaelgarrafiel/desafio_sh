from flask import Blueprint
from flask_restful import Api

from projeto.api.user.api import UserResource

bp_api = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(bp_api)


def init_app(app):
    api.add_resource(UserResource, "/user/<user_id>")
    
    app.register_blueprint(bp_api)
