from flask_restful import Resource
from test_prof.app.service import (question_to_json,
                                   questions_to_json,
                                   direction_to_json,
                                   questions_id_list,
                                   control_question_to_json)
from test_prof.app.test_crud import (create_test, create_direction, create_answers, create_question,
                                     get_question, get_test, get_direction, )


class Question(Resource):
    def get(self, id):
        return {'question': question_to_json(get_question(id))}


class Questions(Resource):
    def get(self, test_id):
        return questions_to_json(get_test(test_id))


class Direction(Resource):
    def get(self, id):
        return direction_to_json(get_direction(id))


class QuestionsIds(Resource):
    def get(self, test_id):
        return questions_id_list(get_test(test_id))


class ControlQuestion(Resource):
    def get(self, question_id, args):
        return control_question_to_json(get_question(question_id), args)
