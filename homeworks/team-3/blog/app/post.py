from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from comment import Comment
from database import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    comments = relationship(Comment, backref='post')

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.created_at = datetime.now().strftime("%Y.%m.%d %H:%M:$S")

        def __repr__(self):
            return '<Post %r>' % self.title
