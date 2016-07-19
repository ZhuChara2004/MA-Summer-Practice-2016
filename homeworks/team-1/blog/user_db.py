import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from blog.helpers import create_cookie

Base = declarative_base()


class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(32))
    password = Column(String(128))
    mail = Column(String(128))
    token = Column(String(1024))

engine = create_engine('postgresql://postgres:root@localhost/blog')

Base.metadata.create_all(engine)
Base.metadata.bind = engine
dbs = sessionmaker(bind=engine)
db = dbs()


def user_create(login, password, mail):
    token = uuid.uuid4()
    if '@' not in login:
        created_user = user(login=login, password=password, mail=mail, token=token)
        db.add(created_user)
        db.commit()


def sign_in_user(login, password):
    if '@' in login:
        s_user = db.query(user).filter(user.mail == login, user.password == password).first()
        create_cookie()
    elif '@' not in login:
        s_user = db.query(user).filter(user.login == login, user.password == password).first()
        create_cookie()
    return s_user