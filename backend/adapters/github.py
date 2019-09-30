from urllib.request import urlopen

import requests
import sqlalchemy
import yaml
from flask_dance.contrib.github import github
from werkzeug.exceptions import NotFound

from adapters.auth import get_current_user
from app import db, app, celery
from models.auth import User, Tokens
from models.dependency import RepoDependency
from models.github import Repo
from models.serializers import RepoDependencySchema, RepoSchema, RepoLoadSchema, DependencyGraphSchema
from webhook_config import WEBHOOK_CONFS


def get_user_repos(user=None):
    user = get_current_user() if not user else user
    return Repo.query.order_by(Repo.created_at).filter_by(user_id=user.id)


def create_user_repos():
    repos_data = github.get("/user/repos").json()
    repos = RepoSchema(many=True).load(repos_data)
    for i, repo in enumerate(repos.data):
        repo.repo_data = repos_data[i]
        db.session.add(repo)
    db.session.commit()


def get_depend_on(repo_id):
    repolist = db.session.query(RepoDependency.depending_on_repo_id, RepoDependency.api_url, Repo.name, ). \
        join(Repo, Repo.id == RepoDependency.depending_on_repo_id). \
        filter(RepoDependency.repo_id == repo_id).all()
    return repolist


@celery.task(name="load user dependency")
def load_user_dependency(user_id):
    user = User.query.filter_by(id=user_id).first()
    repo_list = get_user_repos(user)
    dep_list = []
    token = Tokens.query.filter_by(user_id=user_id).order_by(sqlalchemy.desc(Tokens.id)).first()
    for repo in repo_list:
        filename = f"https://api.github.com/repos/{user.login}/{repo.name}/contents/{app.config.get('DM_FILENAME')}"
        url = requests.get(filename, headers={'Authorization': 'token {}'.format(token.token)}).json().get(
            'download_url')
        if url:
            # query existed database to get list with repo it depend on
            repo_it_depend_on_me_list = db.session.query(RepoDependency.depending_on_repo_id).filter_by(
                repo_id=repo.id).all()
            with urlopen(url) as response:
                data = yaml.load(response.read(), yaml.FullLoader)
                dep_list = data['github']
                for dep_repo_name in dep_list:
                    dep_repo = Repo.query.filter_by(full_name=dep_repo_name).first()
                    # if dep_repo is exist in repos and it is not exist on dependency table add column in database
                    # current_repo depend on it
                    if dep_repo and (dep_repo.id,) not in repo_it_depend_on_me_list:
                        repo_dependency = RepoDependency()
                        repo_dependency.repo_id = repo.id
                        repo_dependency.depending_on_repo_id = dep_repo.id
                        db.session.add(repo_dependency)

    db.session.commit()


def get_dependence(repo_id):
    return db.session.query(RepoDependency).filter(RepoDependency.repo_id == repo_id).all()


def update_dependence(data):
    try:
        dep = RepoDependency.query.get(data['id'])
        if not dep:
            raise NotFound('dependency not found')
        repo = RepoDependencySchema().load(data, instance=dep)
    except KeyError:
        raise KeyError("id not found")
    db.session.commit()


def update_repo(data):
    """     update repo by id   """
    try:
        repo = Repo.query.get(data['id'])
        if not repo:
            raise NotFound("repo not found")
        repo = RepoLoadSchema().load(data, instance=repo)
        print(repo)
    except KeyError:
        raise KeyError("id not found")
    db.session.commit()


def create_hook():
    """  Create a hook for  repo . """
    user = get_current_user()
    repolist = db.session.query(Repo.full_name). \
        join(RepoDependency, Repo.id == RepoDependency.depending_on_repo_id). \
        filter(Repo.user_id == user.id).all()
    conf = WEBHOOK_CONFS  # configuration for webhook from webhook_config
    data = {"name": "web", "active": True, "events": conf['events'], "config": conf['config']}
    for repo_fullname in repolist:
        github.post("/repos/{}/hooks".format(repo_fullname[0]), json=data)


def get_dependency_graph():
    repodependencyschema = DependencyGraphSchema(many=True)
    user_id = get_current_user().id
    dep = db.session.query(RepoDependency). \
        join(Repo, Repo.id == RepoDependency.depending_on_repo_id). \
        filter(Repo.user_id == user_id).all()
    re, _ = repodependencyschema.dump(dep)
    return re
