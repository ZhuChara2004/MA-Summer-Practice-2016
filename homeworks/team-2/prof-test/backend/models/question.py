from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from answer import Answer
from base import Base

class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    question = Column(String(256))
    answers = relationship('Answer', backref='question',
                                lazy='dynamic')
    test_id = Column(Integer, ForeignKey('test.id'))
