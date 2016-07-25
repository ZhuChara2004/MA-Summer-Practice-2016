from test_prof.app.__init__ import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
