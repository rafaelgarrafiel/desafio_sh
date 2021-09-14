from flask_restful import Resource
from projeto.models.users import UsersModel
from projeto.serializer.user import UserSchema


user_schema = UserSchema()

class UserResource(Resource):
    def get(self, user_id):
        users = UsersModel()
        result = users.get_user(user_id)
        if not result:
            return {
                "error": "Usuário não encontrado"
            }
        return user_schema.dump(result), 200
