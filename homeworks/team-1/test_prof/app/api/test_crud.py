from .models import Questions, Answers, Directions, Test, db


def create_test(name):
    test = Test(name)
    db.session.add(test)
    db.session.commit()


def create_question(question, direction_id, test_id, answers):
    question = Questions(question, direction_id, test_id)
    db.session.add(question)
    db.session.commit()
    for answer in answers:
        create_answers(answer)


def create_answers(answer):
    answer = Answers(answer.answer, answer.question_id, answer.direction_id)
    db.session.add(answer)
    db.session.commit()


def create_direction(name):
    direction = Directions(name)
    db.session.add(direction)
    db.session.commit()


def get_question(id):
    question = Questions.query.filter_by(id=id).first()
    return question


def get_direction(id):
    direction = Directions.query.filter_by(id=id).first()
    return direction


def get_test(id):
    test = Test.query.filter_by(id=id).first()
    return test


def delete_question(self, id):
    question = Questions.query.filter_by(id=id).first()
    db.session.delete(question)
    db.commite()


def delete_direction(self, id):
    direction = Directions.query.filter_by(id=id).first()
    db.session.delete(direction)
    db.session.commit()
