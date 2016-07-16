from flask import Flask, render_template, request, redirect
from db import db_all, db_new, db_post, db_delete

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    list_posts = list(reversed(db_all()))
    return render_template('index.html', posts=list_posts)


@app.route('/create')
def create():
    return render_template('create-post.html')


@app.route('/addPost', methods=['POST'])
def add_post():
    title = request.form['title']
    body = request.form['description']
    if title:
        db_new(title, body)
    return redirect('/')


@app.route('/post<id>', methods=['GET'])
def get_post(id):
    post = db_post(id)
    return render_template('post.html', post=post)


@app.route('/update<id>', methods=['GET'])
def get_post_to_update(id):
    post = db_post(id)
    return render_template('update-post.html', post=post)


@app.route('/update', methods=['POST'])
def update_post():
    return redirect('/')


@app.route('/delete<id>')
def delete(id):
    # check auth
    db_delete(id)
    return redirect('/')


if __name__ == '__main__':
    app.run()

