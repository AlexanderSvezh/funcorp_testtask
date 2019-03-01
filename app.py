from flask import Flask, jsonify, make_response, request, abort
from files import task as t
from files.operations import action

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/get', methods=['GET'])
def get_example():
    return jsonify({'tasks': t.tasks})


@app.route('/post', methods=['POST'])
def post_example():
    if not request.json or not 'data' in request.json:
        abort(404)
    task = {
        'id': t.tasks[-1]['id'] + 1,
        'data': request.json['data'],
    }
    t.tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/calc/addition', methods=['POST'])
def get_add():
    return jsonify({'result': action(request.json, 'sum')})


@app.route('/calc/subtraction', methods=['POST'])
def get_subtract():
    return jsonify({'result': action(request.json, 'sub')})


@app.route('/calc/multiply', methods=['POST'])
def get_multiply():
    return jsonify({'result': action(request.json, 'mul')})


@app.route('/calc/division', methods=['POST'])
def get_division():
    return jsonify({'result': action(request.json, 'div')})


@app.route('/')
def index():
    return "Light FunCorp test service!"

if __name__ == '__main__':
    app.run(debug=True)