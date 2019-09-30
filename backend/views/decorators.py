from functools import wraps

from flask import abort
from flask_dance.contrib.github import github


def login_required():
    """Enforces authentication on a route."""

    def decorated(func):
        @wraps(func)
        def decorated_route(*args, **kwargs):
            if not github.authorized:
                abort(401, 'you must be authorized')
            return func(*args, **kwargs)

        return decorated_route

    return decorated
