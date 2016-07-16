from post import Post

def post_all(db):
    return db.query(Post).all()