from projeto.conf.database import db

class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False, unique=True)

    users = db.relationship("Users",lazy="dynamic",primaryjoin="Roles.id == Users.role_id")

    def __init__(self, description):
        self.description = description
