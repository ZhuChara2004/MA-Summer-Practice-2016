from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_blog import db
from datetime import datetime

class Entries(db.Model):  #     for text data base
    id = db.Column(db.Integer, db.Sequence('id_seq'), primary_key=True)
    title = db.Column(db.String(100), unique=True)
    text = db.Column(db.String(1000), unique=False)
    time = db.Column(db.DateTime)
    comments = db.relationship('Comments', backref = 'entries', lazy = 'dynamic')

    def __init__(self, title, text, time = None):
        self.title = title
        self.text = text
        if time is None:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time = time

class Comments(db.Model):
    id = db.Column(db.Integer, db.Sequence('comm_seq'), primary_key = True)
    name = db.Column(db.String(16), unique=False)
    text = db.Column(db.String(1000), unique=False)
    time = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('entries.id'))

    def __init__(self, name, text, time = None):
        self.text = text
        self.name = name
        if time is None:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time = time

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):                # for registration
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username