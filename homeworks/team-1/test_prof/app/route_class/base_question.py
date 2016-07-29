from flask_restful import Resource
from flask import jsonify, Response, after_this_request
from test_prof.app.models import get_question, get_questions
from test_prof.app.service import question_to_json, questions_to_json


class Question(Resource):
    def get(self, id):
        print(jsonify(question_to_json(get_question(id))))
        return {'question': question_to_json(get_question(id))}


class Questions(Resource):
    def get(self, test_id):
        return questions_to_json(get_questions(test_id))


