from flask import Flask, render_template, request, redirect
from db import db_all, db_new

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


if __name__ == '__main__':
    app.run()

