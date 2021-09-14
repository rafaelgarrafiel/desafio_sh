from projeto.conf.serializer import ma
from projeto.database.role import Roles

class RolesSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Roles
