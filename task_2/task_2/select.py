from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DateTime
from sqlalchemy.sql import select

metadata_obj = MetaData()

users = Table('users', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
    Column('role_id', None, ForeignKey('roles.id')),
    Column('create_at', DateTime),
    Column('updated_at', DateTime)
)

roles = Table('roles', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('description', String)
)

claims = Table('claims', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('description', String),
    Column('active', Boolean)
)

user_claims = Table('user_claims', metadata_obj,
    Column('user_id', None, ForeignKey('users.id')),
    Column('claim_id', None, ForeignKey('claims.id'))
)

s = select(
    users.c.name.label("nome"),
    users.c.email.label("email"),
    roles.c.description.label("descricao_papel"),
    claims.c.description.label("descricao_permissao")
    ).select_from(
        users.outerjoin(roles),
        users.outerjoin(user_claims),
        user_claims.outerjoin(claims)
        )