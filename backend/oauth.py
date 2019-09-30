import os

from flask_dance.contrib.github import make_github_blueprint , github

from app import app

# github oauth
blueprint = make_github_blueprint(client_id=os.environ['CLIENT_ID'], client_secret=os.environ['CLIENT_SECRET'],
                                  scope="admin:repo_hook,repo,user",
                                  redirect_url=os.environ['REDIRECT_URL'])
app.register_blueprint(blueprint, url_prefix="/github_login")
