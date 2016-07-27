from test_prof.app.__init__ import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_test = db.Column(db.String(120))
    questions = db.relationship('Questions', backref=db.backref('test', lazy='dynamic'))


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    direction_id = db.Column(db.Integer, db.ForeignKey('directions.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))
    answers = db.relationship('Answers', backref=db.backref('questions', lazy='dynamic'))


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(120))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    directions = db.relationship('Directions', backref=db.backref('answers', lazy='dynamic'))


class Directions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_direction = db.Column(db.String(50))
    answers_id = db.Column(db.Integer, db.ForeignKey('answers.id'))

    def __init__(self, name):
        self.name_direction = name


db.create_all()


def create_direction(name):
    direction = Directions('Yurik')
    db.session.add(direction)
    db.session.commit()


def get_direction(id):
    direction = Directions.query.filter_by(id=id).first()
    return direction.name_direction









