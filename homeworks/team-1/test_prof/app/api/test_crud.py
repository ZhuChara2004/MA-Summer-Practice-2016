from .models import Questions, Answers, Directions, Test, db


def create_test(name):
    test = Test(name)
    db.session.add(test)
    db.session.commit()


def create_question(json):
    question = Questions(json["question"], json["direction_id"], json["test_id"], json["is_control"])
    db.session.add(question)
    db.session.flush()
    answers = json["answers"]
    for answer in answers:
        create_answers(answer, question.id)
    db.session.commit()


def create_answers(answer, id):
    answer = Answers(answer["answer"], id, answer["direction_id"])
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


def get_tests():
    return Test.query.all()


def delete_question(id):
    question = Questions.query.filter_by(id=id).first()
    answers = Answers.query.filter_by(id=id).all()
    db.session.delete(answers)
    db.session.delete(question)
    db.commite()


def delete_direction(id):
    direction = Directions.query.filter_by(id=id).first()
    db.session.delete(direction)
    db.session.commit()


def delete_test(id):
    test = Test.query.filter_by(id=id).first()
    db.session.delete(test)
    db.session.commit()
