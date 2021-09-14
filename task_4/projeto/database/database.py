# import datetime
# from projeto.conf.database import db
# from flask_security import UserMixin, RoleMixin

# user_claims = db.Table('user_claims',
#         db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#         db.Column('claim_id', db.Integer, db.ForeignKey('claims.id')))

# class Roles(db.Model, RoleMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(255))

# class Users(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
#     claims = db.relationship('Claims', secondary=user_claims,
#                             backref=db.backref('users', lazy='dynamic'))

# class Claims(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(255))
#     active = db.Column(db.Boolean, default=True)

