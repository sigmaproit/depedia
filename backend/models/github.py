from sqlalchemy.dialects.postgresql import JSON

from app import db
from models.auth import User
from models.dependency import RepoDependency


class Repo(db.Model):
    __tablename__ = 'repo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    full_name = db.Column(db.String(255), unique=True, nullable=False)
    url = db.Column(db.String(512), unique=True, nullable=False)
    default_branch = db.Column(db.String(52), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    update_at = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    repo_data = db.Column(JSON, nullable=True)
    repo_api_url = db.Column(db.String, nullable=True)
    user = db.relationship(User)
    repo_dependence = db.relationship("RepoDependency", foreign_keys=[RepoDependency.depending_on_repo_id],
                                      backref="repo")

    def __repr__(self):
        return '<Repo %r>' % self.name
