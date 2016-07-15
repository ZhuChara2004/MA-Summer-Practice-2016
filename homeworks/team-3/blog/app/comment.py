from blog import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, body):
        self.body = body
        self.created_at = datetime.utcnow

        def __repr__(self):
            return '<Comment %r>' % self.body
