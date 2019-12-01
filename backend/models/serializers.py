from marshmallow import Schema, fields
from marshmallow.decorators import post_load, pre_load, post_dump

import adapters
from app import ma
from models.auth import User
from models.github import Repo


class RepoDependencySchema(ma.ModelSchema):
    """
    it is used in reposchema to return dependency nested inside repo ,
    used to update api url

    """
    id = fields.Int()
    name = fields.Method("get_repo_name")
    api_url = fields.Str()
    depending_on_repo_id = fields.Int()

    def get_repo_name(self, obj):
        return obj.depending_on_repo.name


class RepoSchema(ma.ModelSchema):
    class Meta:
        model = Repo
        repo_data = fields.Raw(load_only=True)
        depend_on = fields.Nested(RepoDependencySchema)
        fields = (
        'id', 'name', 'full_name', 'url', 'default_branch', 'created_at', 'update_at', 'user_id', 'repo_api_url')

    @pre_load
    def add_user_id(self, data, **kwargs):
        user = adapters.auth.get_current_user()
        data['user_id'] = user.id
        return data

    repodependencyschema = RepoDependencySchema(many=True)

    @post_dump(pass_many=True)
    def add_depend_on(self, data, many):
        if many:
            for i, repo in enumerate(data):
                repo['depend_on'], _ = self.repodependencyschema.dump(adapters.github.get_dependence(repo['id']))
                data[i] = repo
            return data
        else:
            data['depend_on'] = self.repodependencyschema.dump(adapters.github.get_dependence(data['id']))
            return data


class RepoLoadSchema(ma.ModelSchema):
    """    that schema was created to be used in update this fields    """

    class Meta:
        Model = Repo
        fields = ['id', 'name', 'full_name', 'url', 'default_branch', 'repo_api_url']


class UserSchema(Schema):
    id = fields.Integer()
    url = fields.String()
    avatar_url = fields.String(required=False, allow_none=True)
    name = fields.String(required=False, allow_none=True)
    login = fields.String()
    user_api_url = fields.String()
    email = fields.Email(required=False, allow_none=True)
    bio = fields.String(required=False, allow_none=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class UpdateUserSchema(ma.ModelSchema):
    bio = fields.String(required=False, allow_none=True)

    class Meta:
        Model = User
        fields = ['id', 'url', 'avatar_url', 'name', 'login', 'user_api_url', 'email', 'bio']


class DependencyGraphSchema(ma.ModelSchema):
    id = fields.Int()
    from_repo = fields.String(attribute='repo_depending_on.name', dump_to='from')
    to_repo = fields.String(attribute='depending_on_repo.name', dump_to='to')
