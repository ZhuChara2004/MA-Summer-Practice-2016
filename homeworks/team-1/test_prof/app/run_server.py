from flask import Flask, render_template
# from test_prof.app.api.__init__ import app

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/prof', methods=['GET'])
def get_first():
    # url = "http://127.0.0.1:5000/api/v1.0/tests"
    # obj = urllib3.urlopen(url).read()
    # data = json.loads(obj)
    # print(data)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5001, debug=True)
