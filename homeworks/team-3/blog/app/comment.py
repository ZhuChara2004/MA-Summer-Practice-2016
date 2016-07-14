from blog import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500), required=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, body, created_at):
        self.body = body
        self.created_at = created_at


        def __repr__(self):
            return '<Comment %r>' % self.body