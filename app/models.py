from . import db
from datetime import datetime as dt
from app import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String(20), nullable=False, default='rys.png')
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(str(password))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_image}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    title = db.Column(db.String(140), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"