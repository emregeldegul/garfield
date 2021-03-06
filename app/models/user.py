from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


dictionary_table = db.Table('dictionary',
                            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                            db.Column('word_id', db.Integer, db.ForeignKey('word.id'))
                            )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70), nullable=False, unique=True)
    password = db.Column(db.String(94), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    dictionary = db.relationship('Word',
                                 secondary=dictionary_table,
                                 lazy='dynamic',
                                 backref=db.backref('users', lazy='dynamic')
                                 )
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def generate_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
