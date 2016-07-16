import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class post(Base):
    __tablename__ = 'post'
    pid = Column(Integer, primary_key=True)
    datetime = Column(String(32))
    title = Column(String(128))
    body = Column(String(1024))


engine = create_engine('postgresql://root:12124343@localhost/blog')

Base.metadata.create_all(engine)
Base.metadata.bind = engine
dbs = sessionmaker(bind=engine)
db = dbs()


def db_all():
    return db.query(post).all()


def db_new(title, body):
    now = datetime.datetime.now().strftime("Posted at %Y.%m.%d %H:%M")
    new_post = post(datetime=now, title=title, body=body)
    db.add(new_post)
    db.commit()


def db_delete(pid):
    dp = db.query(post).filter(post.pid == pid).first()
    db.delete(dp)
    db.commit()


def db_post(pid):
    return db.query(post).filter(post.pid == pid).first()


def db_delete(pid, title, body):
    update_post = db.query(post).filter(post.pid == pid).first()
    update_post.title = title
    update_post.body = body
    db.updete(update_post)
    db.commit
    return update_post
