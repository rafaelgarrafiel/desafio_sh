from projeto.conf.database import db
from projeto.database.user import Users

class UsersModel():
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
    
    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password
    
    def get_user(self, id):
        return Users.query.filter(Users.id == id).first()