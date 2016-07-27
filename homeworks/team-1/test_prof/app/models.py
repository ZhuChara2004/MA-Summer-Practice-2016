from test_prof.app.__init__ import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_test = db.Column(db.String(120))
    # questions_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    # questions = db.relationship('Test', backref=db.backref('tests', lazy='dynamic'))


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    # answers_id = db.Column(db.Integer, db.ForeignKey('answers.id'))
    # answers = db.relationship('Answers', backref='question', lazy='dynamic')


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(120))
    # id_question = db.Column(db.Integer, db.ForeignKey('questions.id'))


class Directions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_direction = db.Column(db.String(50))

    def __init__(self, name):
        self.name_direction = name


def create_direction(name):
    direction = Directions('Yurik')
    db.session.add(direction)
    db.session.commit()


def get_direction(id):
    direction = Directions.query.filter_by(id=id).first()
    return direction.name_direction









