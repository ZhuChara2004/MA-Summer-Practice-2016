from test.app.__init__ import app
from test.app.models import create_direction, get_f


@app.route('/')
@app.route('/index')
def index():
    # create_direction('Yurik')
    return "Hello, World!"


@app.route('/<id>', methods=['GET'])
def get_first(id):
    return get_f(id)
