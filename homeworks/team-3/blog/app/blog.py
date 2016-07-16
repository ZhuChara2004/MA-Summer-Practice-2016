import os
from flask import Flask, request, redirect, url_for
from flask import render_template
from crud import post_all, post_look, post_new, post_update

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


@blog.route('/new', methods=['POST'])
def new():
    title = request.args.get('title')
    body = request.args.get('body')
    post_new(db_session, title, body)
    return redirect('/')


@blog.route('/update', methods=['POST'])
def update():
    id = request.args.get('id')
    title = request.args.get('title')
    body = request.args.get('body')
    post_update(db_session, id, title, body)
    return redirect('/')


@blog.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    blog.run()
