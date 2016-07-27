from test_prof.app.__init__ import app
from flask import render_template
# from test_prof.app.models import create_direction, get_test
from flask_restful import Api
from .route_class.base_question import Question, Questions


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/prof', methods=['GET'])
def get_first():
    return render_template('index.html')


api = Api(app, prefix='/api/v1.0')
api.add_resource(Question, '/question/<id>')
api.add_resource(Questions, '/questions/<test_id>')
