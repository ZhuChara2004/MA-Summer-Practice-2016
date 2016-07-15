from flask import Flask, render_template, request, redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from datetime import datetime



# Created by Demian Kurilenko, Anton Lunyov (backend) and Dima Burkatsky (frontend)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/posts'
app.config['SECRET_KEY']= 'its_strongly_secret'
app.config['SECURITY_REGISTERABLE'] = True

app.debug =True
db = SQLAlchemy(app)


class Entries(db.Model):  #     for text data base
    id = db.Column(db.Integer, db.Sequence('id_seq'), primary_key=True)
    title = db.Column(db.String(100), unique=True)
    text = db.Column(db.String(1000), unique=False)
    time = db.Column(db.DateTime)
    comments = db.relationship('Comments', backref = 'entries', lazy = 'dynamic')

    def __init__(self, title, text, time = None):
        self.title = title
        self.text = text
        if time is None:
            time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self.time = time

class Comments(db.Model):
    id = db.Column(db.Integer, db.Sequence('comm_seq'), primary_key = True)
    text = db.Column(db.String(1000), unique=False)
    time = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('entries.id'))

    def __init__(self, text, time = None):
        self.text = text
        if time is None:
            time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self.time = time
# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):                # for registration
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
                                              # Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route('/')                    #     index page
def show_entries():
    myAll = Entries.query.all()
    return render_template('index.html', entries=Entries,myAll = myAll)

@app.route('/new-post',methods=['POST'])
def add_entry():
    entries = Entries(request.form['title'], request.form['text'])
    db.session.add(entries)
    db.session.commit()
    return redirect(url_for('show_entries'))   


@app.route('/post')
def postPage():
    return render_template('new-post.html')
@app.route("/<int:id>/", methods=("GET","POST"))
def view(id):
    post = Entries.query.get_or_404(id)
    return render_template('view-post.html', post =post)


@app.route("/<int:id>/edit/", methods=("GET", "POST"))
def edit(id):
    post = Entries.query.get_or_404(int(id))
    form = Entries(title=post.title,
                    text = post.text)
    db.session.commit()
    return render_template('update-post.html', fork=form, id=id)

@app.route('/<int:id>/save',methods=['POST'])
def save(id):
    id = id
    form =Entries.query.filter(Entries.id == id).first()
    print(form)
    form.title = request.form['title']
    form.text = request.form['text']
    db.session.commit()
    return redirect(url_for('show_entries'))
@app.route('/<int:id>/delete',methods=['GET'])
def delete(id):
    form = Entries.query.filter_by(id = id).first()
    Comments.query.filter_by(post_id=id).delete()
    db.session.delete(form)
    db.session.commit()
    return redirect(url_for('show_entries'))


@app.route('/<int:id>/comments',methods=['GET'])
def view_comments(id):
    post = Entries.query.get_or_404(int(id))
    return render_template('view-comments.html', post = post)

@app.route("/<int:id>/new-comment/", methods=("GET", "POST"))
def new_comment(id):
    post = Entries.query.get_or_404(int(id))
    form = Entries(title=post.title,
                    text = post.text)
    db.session.commit()
    return render_template('new-comment.html', fork=form, id=id)

@app.route('/<int:id>/save-comment',methods=['POST'])
def add_comment(id):
    comment = Comments(request.form['text'])
    post = Entries.query.get_or_404(int(id))
    post.comments.append(comment)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('view_comments', id = id))

@app.route('/<int:id>/delete/<int:comment_id>',methods=['GET'])
def delete_comment(id, comment_id):
    form = Comments.query.filter_by(id=comment_id).first()
    db.session.delete(form)
    db.session.commit()
    return redirect(url_for('view_comments', id = id))


if __name__ =="__main__":
    app.run()