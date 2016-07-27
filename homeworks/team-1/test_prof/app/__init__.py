from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/test_prof'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
db.create_all()

from test_prof.app import views
