from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from question import Question
from base import Base

class pTest(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    questions = relationship('Question', backref='test',
                                lazy='dynamic')
