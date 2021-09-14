import datetime

from projeto.conf.database import db
from projeto.database.claim import user_claims
from projeto.database.role import Roles

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    role_id =db.Column(db.Integer,db.ForeignKey('roles.id'), nullable=True)
    roles = db.relationship("Roles", backref="roles")

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    claims = db.relationship('Claims', secondary=user_claims,
                            backref=db.backref('users', lazy='dynamic'))



