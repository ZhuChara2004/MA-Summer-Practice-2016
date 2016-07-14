from post_db import db_all, db_new, db_delete, db_post
from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    posts = list(reversed(db_all()))
    return render_template('index.html', posts=posts)

@app.route('/<pid>', methods=['GET'])
def look(pid):
    look = db_post(int(pid))
    return render_template('post.html', post=look)

@app.route('/new', methods=['GET'])
def new():
    return render_template('new.html')

@app.route('/del/<pid>', methods=['GET'])
def delete_py(pid):
    db_delete(int(pid))
    return redirect('/')

@app.route('/new_py', methods=['POST'])
def new_py():
    title = request.form['title']
    body = request.form['comment']
    if title != "" and body != "":
    	db_new(title=title, body=body)
    return redirect('/')

if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'some_secret'
    app.run(host='0.0.0.0')
