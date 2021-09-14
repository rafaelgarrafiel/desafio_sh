from projeto.conf.database import db

user_claims = db.Table('user_claims',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('claim_id', db.Integer, db.ForeignKey('claims.id')))

class Claims(db.Model):
    __tablename__ = "claims"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, description):
        self.description = description
