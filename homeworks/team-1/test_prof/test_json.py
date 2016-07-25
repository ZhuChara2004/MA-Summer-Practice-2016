from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello'

tasks = [
    {
        'id': 1
    }
]


@app.route('/api1.0', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run()
