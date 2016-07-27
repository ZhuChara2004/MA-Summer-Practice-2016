from test_prof.app.__init__ import app
from flask import render_template
from test_prof.app.models import create_direction, get_test


@app.route('/')
@app.route('/index')
def index():
    # create_direction('Yurik')
    return "Hello, World!"


@app.route('/prof', methods=['GET'])
def get_first():
    for a in get_test(1).questions:
        print(a.question)
        for b in a.answers:
            print(b.answer)
    return render_template('index.html')

