import os
from flask import Flask, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template

blog = Flask(__name__)
blog.config.from_object(os.environ['APP_SETTINGS'])
blog.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(blog)

@blog.route('/view', methods=['GET'])
def view():
    from post import Post
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@blog.route('/new', methods=['POST'])
def post():
    from post import Post
    title = None
    description = None
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        post = Post(title, description)
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('/view'))

@blog.route('/edit', methods=['POST']) #not work
def edit():
    from post import Post
    id = None
    post = None
    if request.method == 'POST':
        id = request.form['id']
        post = Post.query.get(id)
        post.title = request.form['title']
        post.description = request.form['description']
        db.session.commit()
    return redirect(url_for('/post/view'))