from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from Blogger import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, user: dict):
        self.name = user['name']
        self.email = user['email']
        self.password = generate_password_hash(user['password'], 'sha256')

    @classmethod
    def find_user_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if not user:
            return False
        return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        if not check_password_hash(self.password, password):
            return False
        return True

    def __repr__(self):
        return f" name:{self.name}, email: {self.email}, created_at:{self.created_at}"
