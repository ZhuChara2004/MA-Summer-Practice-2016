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
        list_questions.append({
            'question': question_to_json(q)
        })
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
        'question': question.question,
        'id': question.id,
        'answers': list_answers
    }
