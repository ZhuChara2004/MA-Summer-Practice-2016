from test_prof.app.api.__init__ import app
from .route_class.base_question import Question, Questions, Direction, QuestionsIds, ControlQuestion, Create, Tests
from .unicode_api import UnicodeApi


api = UnicodeApi(app, prefix='/api/v1.0')
api.add_resource(Question, '/question/<id>')
api.add_resource(Direction, '/direction/<id>')
api.add_resource(Tests, '/tests')
api.add_resource(Questions, '/questions/<test_id>')
api.add_resource(QuestionsIds, '/questions/<test_id>/direction/<direction>')
api.add_resource(ControlQuestion, '/control/<test_id>/direction/<direction_id>')
api.add_resource(Create, '/create/<method>')
