from test_prof.app.__init__ import app
from test_prof.app.models import create_direction, get_direction


@app.route('/')
@app.route('/index')
def index():
    # create_direction('Yurik')
    return "Hello, World!"


@app.route('/<id>', methods=['GET'])
def get_first(id):
    return get_direction(id)
