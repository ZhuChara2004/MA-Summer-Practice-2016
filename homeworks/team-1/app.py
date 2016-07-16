from flask import Flask, render_template, request, redirect
from db import db_all

app = Flask(__name__)


@app.route('/')
def index():
    list_posts = list(reversed(db_all()))
    return render_template('index.html', posts=list_posts)


if __name__ == '__main__':
    app.run()

