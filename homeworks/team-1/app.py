from flask import Flask, render_template, request, redirect
from db import db_all, db_new, db_post, db_delete, db_update
from user_db import user_create, sign_in_user

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


@app.route('/update<id>', methods=['POST'])
def update_post(id):
    title = request.form['title']
    body = request.form['description']
    print(title)
    print(body)
    db_update(id, title, body)
    return redirect('/')


@app.route('/delete<id>')
def delete(id):
    # check auth
    db_delete(id)
    return redirect('/')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'GET':
        return render_template('sign-up.html')
    elif request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        password_r = request.form['password_repeat']
        mail = request.form['mail']
        if password == password_r:
            user_create(login, password, mail)
            return redirect('/signIn')
        elif password != password_r:
            redirect('/auth')


@app.route('/signIn', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign-in.html')
    elif request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        request_user = sign_in_user(login, password)
        if not request_user:
            return render_template('/signIn')
        else:
            print(request_user.login)
            return redirect('/')


if __name__ == '__main__':
    app.run()

