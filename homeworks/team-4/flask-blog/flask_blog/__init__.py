from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost/posts'
app.config['SECRET_KEY']= 'its_strongly_secret'
app.config['SECURITY_REGISTERABLE'] = True
app.debug =True

db = SQLAlchemy(app)

import flask_blog.views, flask_blog.models
                                              # Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

