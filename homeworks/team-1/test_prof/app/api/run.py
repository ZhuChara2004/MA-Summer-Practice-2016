from test_prof.app.api.__init__ import app
from flask import render_template


@app.route('/', methods=['GET'])
def get_first():
    return render_template('index.html')


@app.route('/<id>', methods=['GET'])
def test(id):
    return render_template("test.html", id=id)

if __name__ == '__main__':
    app.run(debug=True)
