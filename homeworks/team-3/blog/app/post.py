from datetime import datetime
from blog import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    category = db.relationship('Comment',
                               backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.created_at = datetime.utcnow
        self.updated_at = datetime.utcnow

        def __repr__(self):
            return '<Post %r>' % self.title
