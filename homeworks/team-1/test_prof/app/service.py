import json
from .test_crud import create_test, create_direction
from .admin import equals


def answer_to_json(answer):
    return {
        'id': answer.id,
        'body': answer.answer,
        'direction': answer.direction_id
    }


def answers_to_json(question):
    tmp_answers = []
    for a in question.answers:
        tmp_answers.append(answer_to_json(a))
    return tmp_answers


def question_to_json(question):
    return {
        'id': question.id,
        'body': question.question,
        'direction': question.direction_id,
        'test_id': question.test_id,
        'answers': answers_to_json(question)
    }


def questions_to_json(test):
    list_questions = []
    for q in test.questions:
        list_questions.append(question_to_json(q))
    return {
        'test': test.name_test,
        'questions': list_questions
    }


def direction_to_json(direction):
    return {'direction': direction.name_direction}


def questions_id_list(test):
    list_ids = []
    for q in test.questions:
        list_ids.append({
            'question_id': q.id,
            'direction_id': q.direction_id
        })
    return {'list_ids': list_ids}


def control_question_to_json(question, args):
    if question.direction_id == 0:
        return {'error': 'question is not control'}
    args = args.split('/')
    list_answers = []
    for a in question.answers:
        for item in args:
            if a.id is int(item):
                list_answers.append({
                    'answer': a.answer,
                    'direction_id': a.direction_id
                })
    return {
        'body': question.question,
        'id': question.id,
        'answers': list_answers
    }


def create(j):
    print(j)
    obj = json.loads(j)
    if equals(obj["token"]):
        method_name = obj["method"]
        print(method_name)
        if method_name == "c_test":
            create_test(obj['body'][0]['name'])
            return {"response": "ok"}
        elif method_name == "c_question":
            # add create question
            return {"response": "ok"}
        elif method_name == "c_direction":
            create_direction(obj['body'][0]['name'])
            return {"response": "ok"}

# http://127.0.0.1:5000/api/v1.0/create/{"method" : "c_test", "body" :[ {"name" : "CDTU_test"}], "token":"secret_token"}
