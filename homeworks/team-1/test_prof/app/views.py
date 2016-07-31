from flask import render_template
from test_prof.app.__init__ import app
from .route_class.base_question import Question, Questions, Direction, QuestionsIds
from .unicode_api import UnicodeApi


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/prof', methods=['GET'])
def get_first():
    return render_template('index.html')


api = UnicodeApi(app, prefix='/api/v1.0')
api.add_resource(Question, '/question/<id>')
api.add_resource(Questions, '/questions/<test_id>')
api.add_resource(Direction, '/direction/<id>')
api.add_resource(QuestionsIds, '/listQ/<test_id>')
