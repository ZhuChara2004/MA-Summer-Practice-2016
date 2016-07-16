from post import Post
from sqlalchemy import desc
from datetime import datetime


def post_all(db):
    return db.query(Post).order_by(desc(Post.created_at)).all()


def post_look(db, post_id):
    return db.query(Post).filter(Post.id == post_id).first()


def post_new(db, title, body):
    if title != "" and body != "":
        new_post = Post(title, body)
        db.add(new_post)
        db.commit()


def post_update(db, post_id, new_title, new_body):
    updated_post = post_look(db, post_id)
    updated_post.title = new_title
    updated_post.body = new_body
    updated_post.updated_at = datetime.now().strftime("%Y.%m.%d %H:%M:$S")
    db.add(updated_post)
    db.commit()