from flask import Flask, render_template, request, redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_blog import app, db, models

Entries = models.Entries
Comments = models.Comments

@app.route('/')                    #     index page
def show_entries():
    myAll = list(reversed(Entries.query.all()))
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
    comment = Comments(request.form['text'], request.form['name'])
    post = Entries.query.get_or_404(int(id))
    post.comments.append(comment)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('view', id = id))

@app.route('/<int:id>/delete/<int:comment_id>',methods=['GET'])
def delete_comment(id, comment_id):
    form = Comments.query.filter_by(id=comment_id).first()
    db.session.delete(form)
    db.session.commit()
    return redirect(url_for('view', id = id))