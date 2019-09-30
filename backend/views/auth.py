from flask import redirect, url_for

from adapters.auth import create_user, create_token, get_user_by_token
from adapters.github import create_user_repos, load_user_dependency
from app import app  # for  @app.route
from models.serializers import UserSchema
from oauth import github
from views.decorators import login_required


# auth view
@app.route("/github_login")
def login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    else:
        user = create_user()
        create_token(user)
        create_user_repos()
        res = load_user_dependency.apply_async((user.id,))
        authorized_url = f'{app.config.get("APP_HOST")}/authorized'
        return redirect(authorized_url)


@app.route('/user', methods=['GET'])
@login_required()
def fetch_user():
    user = get_user_by_token(github.token['access_token'])
    return UserSchema().dump(user)
