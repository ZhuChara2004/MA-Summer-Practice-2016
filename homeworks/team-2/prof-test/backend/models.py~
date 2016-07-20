import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import desc
 
Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    questions = relationship('Question', backref='test',
                                lazy='dynamic')
 
class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    question = Column(String(256))
    type = Column(Integer)
    answers = relationship('Answer', backref='question',
                                lazy='dynamic')
    test_id = Column(Integer, ForeignKey('test.id'))

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    answer = Column(String(256))
    type = Column(Integer)
    question_id = Column(Integer, ForeignKey('question.id'))

engine = create_engine("postgresql://dima:12124343@localhost/proftest")

Base.metadata.create_all(engine)
Base.metadata.bind = engine
dbs = sessionmaker(bind=engine)
db = dbs()

def db_q(num):
    return db.query(Question).all()

def db_save(q, t):
    qq = Question(question=q, type=t)
    db.add(qq)
    db.commit()

def db_delete(id):
    qq = db.query(Question).filter(Question.id == id).first()
    db.delete(qq)
    db.commit()
