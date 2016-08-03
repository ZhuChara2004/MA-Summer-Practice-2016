from test_prof.app.api.__init__ import app
from flask import render_template


@app.route('/', methods=['GET'])
def get_first():
    # url = "http://127.0.0.1:5000/api/v1.0/tests"
    # obj = urllib3.urlopen(url).read()
    # data = json.loads(obj)
    # print(data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
