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
    print(question.question)
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
