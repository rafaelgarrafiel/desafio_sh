from projeto.conf.serializer import ma
from projeto.database.user import Users

class UserSchema(ma.SQLAlchemyAutoSchema):


    class Meta:
        model = Users
        fields = ('name', 'email', 'role_id')
