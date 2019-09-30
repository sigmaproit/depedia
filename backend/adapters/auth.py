from flask import abort
from flask_dance.contrib.github import github
from werkzeug.exceptions import NotFound

from app import db
from models import User, Tokens
from models.serializers import UserSchema, UpdateUserSchema


def get_current_user():
    resp = github.get("/user")
    if resp.ok:
        user = UserSchema().load(resp.json()).data
        return user
    abort(401, 'unauthorized user!')


def create_user():
    user = get_current_user()
    if not User.query.filter_by(id=user.id).first():
        db.session.add(user)
        db.session.commit()
    return user


def create_token(user):
    token = Tokens()
    token.user_id = user.id
    token.token = github.token['access_token']
    if not Tokens.query.filter_by(token=token.token).first():
        db.session.add(token)
        db.session.commit()
        return 'token created'
    return 'token is already exist'


def get_user_by_token(token):
    token_obj = Tokens.query.filter_by(token=token).first()
    if token_obj:
        return User.query.get(token_obj.user_id)
    abort(401, 'unauthorized user')


def update_user(data):
    try:
        user = User.query.get(data['id'])
        if not user:
            raise NotFound("user not found")
        user = UpdateUserSchema().load(data, instance=user)
    except KeyError:
        raise KeyError("id not found")
    db.session.commit()
