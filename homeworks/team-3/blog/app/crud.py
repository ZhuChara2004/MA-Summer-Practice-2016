from post import Post
from sqlalchemy import desc


def post_all(db):
    return db.query(Post).order_by(desc(Post.created_at)).all()