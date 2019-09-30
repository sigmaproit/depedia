from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), unique=True, nullable=False)
    avatar_url = db.Column(db.String(512), unique=True, nullable=False)
    name = db.Column(db.String(80))
    login = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    user_api_url = db.Column(db.String, nullable=True)
    bio = db.Column(db.String(255), unique=True, nullable=True)
    repo = db.relationship("Repo", backref="owner")

    def __init__(self, id=None, url=None, avatar_url=None, name=None, login=None, email=None, bio=None):
        self.id = id
        self.url = url
        self.avatar_url = avatar_url
        self.name = name
        self.login = login
        self.email = email
        self.bio = bio

    def __repr__(self):
        return '<User %r>' % self.login


class Tokens(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    token = db.Column(db.String(40), unique=True)
    user = db.relationship(User)
