from projeto.conf.serializer import ma
from projeto.database.user import Users
from projeto.serializer.roles import RolesSchema

# class UserSchema(ma.SQLAlchemySchema):
class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Users
        # fields = ('name', 'email', 'roles')
        load_instance = True

    id = ma.auto_field(load_only=True)
    name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field(load_only=True)
    role_id = ma.auto_field(load_only=True)

    roles = ma.Nested(RolesSchema)
    # class Meta:
    #     model = Users
    #     fields = ('name', 'email', 'roles')

