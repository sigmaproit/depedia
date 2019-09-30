import requests
from flask import jsonify, request
from werkzeug.exceptions import abort, NotFound

from adapters.auth import get_current_user, update_user
from adapters.github import get_user_repos, load_user_dependency, create_hook, update_dependence, update_repo, \
    get_dependency_graph
from app import app
from models.serializers import RepoSchema, UserSchema
from oauth import github


@app.route("/user/repos")
def get_repos():
    repos_schema = RepoSchema(many=True)
    all_repos = get_user_repos()
    return repos_schema.dumps(all_repos)


@app.route("/user")
def get_user():
    return UserSchema().dumps(get_current_user())


@app.route("/create/dep")
def create_dep():
    if github.authorized:
        user = get_current_user()
        res = load_user_dependency.apply_async((user.id,))
        return jsonify(message="dep was created")
    else:
        return jsonify(message="an error has happen ")


@app.route("/update/api_url", methods=['POST'])
def update_dependence_api_url():
    """   update dependency  """
    try:
        data = request.get_json()
        update_dependence(data)
    except KeyError as err:
        abort(400, str(err))
    except NotFound:
        abort(404, "dependence not found")

    return jsonify(message="dependence was updated")


@app.route("/update/user", methods=['POST'])
def update_user_endpoint():
    """   update user by id  """
    try:
        data = request.get_json()
        update_user(data)
    except KeyError as err:
        abort(400, str(err))
    except NotFound:
        abort(404, "user not found")

    return jsonify(message="user was updated")


@app.route("/update/repo", methods=['POST'])
def update_repo_endpoint():
    """   update repo by id  """
    try:
        data = request.get_json()
        update_repo(data)
    except KeyError as err:
        abort(400, str(err))
    except NotFound:
        abort(404, "repo not found")

    return jsonify(message="repo was updated")


@app.route("/install")
def install():
    create_hook()
    return jsonify(message="installed")


@app.route("/receiver", methods=['POST'])
def receiver():
    """
        listen to githup webhook  push event  in depending on repo
        call dependency  api_url
        if not call repo api_url
        if not call user api_url
        if not print failed message
     """
    data = request.get_json()
    repo = RepoSchema().get_instance(data['repository'])
    for dependence in repo.repo_dependence:
        if dependence.api_url:
            call_api_url(dependence.api_url)
        elif dependence.repo_depending_on.repo_api_url:
            call_api_url(dependence.repo_depending_on.repo_api_url)
        elif repo.user.user_api_url:
            call_api_url(repo.user.user_api_url)
        else:
            print("api_url not found for repo id = {} and depending_on_repo_id = {} ".format(dependence.repo_id,
                                                                                             dependence.depending_on_repo_id))

    return jsonify("request received")


@app.route("/graph")
def graph():
    return jsonify(get_dependency_graph())


def call_api_url(api_url):
    try:
        requests.get(api_url)
    except Exception as ex:
        print(str(ex))
