from app import db


class RepoDependency(db.Model):
    __tablename__ = 'repo_dependency'

    id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer, db.ForeignKey('repo.id'))
    depending_on_repo_id = db.Column(db.Integer, db.ForeignKey('repo.id'))
    api_url = db.Column(db.String, nullable=True)
    depending_on_repo = db.relationship("Repo", foreign_keys=[depending_on_repo_id])
    repo_depending_on = db.relationship("Repo", foreign_keys=[repo_id])
