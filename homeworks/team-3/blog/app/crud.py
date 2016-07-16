from post import Post
from sqlalchemy import desc


def post_all(db):
    return db.query(Post).order_by(desc(Post.created_at)).all()


def post_look(db, post_id):
    return db.query(Post).filter(Post.id == post_id).first()
