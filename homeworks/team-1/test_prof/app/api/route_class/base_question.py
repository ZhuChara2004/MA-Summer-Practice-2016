from flask_restful import Resource, request
from test_prof.app.api.service import (question_to_json,
                                       questions_to_json,
                                       direction_to_json,
                                       questions_id_list,
                                       # control_question_to_json,
                                       create,
                                       Delete,
                                       get_t,
                                       direction_a_to_json)

from test_prof.app.api.test_crud import (get_question, get_test, get_direction, get_control_question, get_dir_answer)


class Question(Resource):
    def get(self, id):
        return {'question': question_to_json(get_question(id))}

    def delete(self, id):
        return Delete.delete_q(id)


class Questions(Resource):
    def get(self, test_id):
        return questions_to_json(get_test(test_id))


class Direction(Resource):
    def get(self, id):
        return direction_to_json(get_direction(id))

    def post(self, id):
        print(request.json)

    def delete(self, id):
        Delete.delete_d(id)


class QuestionsIds(Resource):
    def get(self, test_id, direction):
        return questions_id_list(get_test(test_id), direction)


class ControlQuestion(Resource):
    def get(self, test_id, direction_id):
        return question_to_json(get_control_question(test_id, direction_id))


class Create(Resource):
    def post(self, method):
        json = request.json
        return create(method, json)


class Tests(Resource):
    def get(self):
        return get_t()


class DirectionAnswer(Resource):
    def get(self, id):
        return direction_a_to_json(get_dir_answer(id))
