import string
import random
from flask_restful import abort
from sqlalchemy.exc import IntegrityError

from projeto.conf.database import db
from projeto.database.user import Users
from projeto.serializer.user import UserSchema

user_schema = UserSchema()

class UsersModel():
    
    def get_user(self, id):
        return Users.query.filter(Users.id == id).first()
    
    def get_random_password(self, length):
        letras = string.ascii_lowercase
        password = ''.join(random.choice(letras) for i in range(length))
        return password
    
    def save(self, dados):
        us = user_schema.load(dados)
        try:
            db.session.add(us)
            db.session.flush()
        except IntegrityError as e:
            db.session.rollback()
            abort(500, error="Erro de integridade")
        
        db.session.commit()

        return user_schema.dump(dados)