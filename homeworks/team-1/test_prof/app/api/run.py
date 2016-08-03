from test_prof.app.api.__init__ import app
from flask import render_template


@app.route('/', methods=['GET'])
def get_first():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
