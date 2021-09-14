from projeto.conf.database import db
from projeto.database.user import Users
from projeto.database.role import Roles
from projeto.database.claim import Claims
# from app.database.pedidos import Pedidos


def create_db():
    """Criando o banco de dados"""
    db.create_all()


def drop_db():
    """Limpando o banco de dados"""
    db.drop_all()


def populate_db():
    """Populando o banco de dados"""
    data_role = [
        Roles(description='Admin'),
    ]
    db.session.bulk_save_objects(data_role)
    db.session.commit()

    data_claim = [
        Claims(description='Administração'),
    ]
    db.session.bulk_save_objects(data_claim)
    db.session.commit()

    data_user = [
        Users(name='Admin', email='admin@projeto.com', password='12345', role_id=1),
    ]
    db.session.bulk_save_objects(data_user)
    db.session.commit()
    return True