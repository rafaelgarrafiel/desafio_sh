from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError

from projeto.conf.database import db
from projeto.models.users import UsersModel
from projeto.serializer.user import UserSchema


user_schema = UserSchema()


class UsersResource(Resource):
    
    def post(self):
        user = UsersModel()
        json_input = request.get_json()
        
        if not 'password' in json_input:
            json_input['password'] = user.get_random_password(8)

        errors = user_schema.validate(json_input)
        if errors:
            return {
                    'error': errors
                }, 401

        result = user.save(json_input)

        return result, 201

class UserResource(Resource):
    def get(self, user_id):
        users = UsersModel()
        result = users.get_user(user_id)
        if not result:
            return {
                "error": "Usuário não encontrado"
            }
        return user_schema.dump(result), 200
