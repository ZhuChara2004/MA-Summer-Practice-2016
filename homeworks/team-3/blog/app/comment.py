from _datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from database import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    body = Column(Text)
    created_at = Column(DateTime)
    post_id = Column(Integer, ForeignKey('posts.id'))

    def __init__(self, body):
        self.body = body
        self.created_at = datetime.now().strftime("%Y.%m.%d %H:%M:$S")
        def __repr__(self):
            return '<Comment %r>' % self.body
