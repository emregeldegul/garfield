from app import db


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='user')
    point = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
