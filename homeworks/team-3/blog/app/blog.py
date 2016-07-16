import os
from flask import Flask, request, redirect, url_for
from flask import render_template
from crud import post_all, post_look

blog = Flask(__name__)
blog.config.from_object(os.environ['APP_SETTINGS'])
blog.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db_session


@blog.route('/', methods=['GET'])
def index():
    posts = post_all(db_session)
    return render_template('index.html', posts=posts)


@blog.route('/<id>', methods=['GET'])
def look(id):
    post = post_look(db_session, id)
    return render_template('post.html', post=post)


@blog.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    blog.run()
