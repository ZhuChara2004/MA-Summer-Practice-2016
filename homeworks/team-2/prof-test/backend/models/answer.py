from sqlalchemy import Column, ForeignKey, Integer, String
from base import Base

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    answer = Column(String(256))
    type = Column(Integer)
    question_id = Column(Integer, ForeignKey('question.id'))
