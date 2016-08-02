from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/prof', methods=['GET'])
def get_first():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5001)
