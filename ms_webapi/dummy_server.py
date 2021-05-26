import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Dummy Message Server</h1>'''

@app.route('/api/v1/messages/registration', methods=['POST'])
def api_registration():
    response = {}
    response['code'] = 'ok'
    response['token'] = '11223344556677889900'
    response['request'] = request.args
    return jsonify(response)

@app.route('/api/v1/messages/authentication', methods=['GET'])
def api_authentication():
    response = {}
    response['code'] = 'ok'
    response['token'] = '11223344556677889900'
    response['request'] = request.args
    return jsonify(response)

@app.route('/api/v1/messages/send', methods=['POST'])
def api_send():
    response = {}
    if 'token' not in request.args:
        response['code'] = 'error'
        response['description'] = 'token not present'
    elif not request.args['token'] == '11223344556677889900':
        response['code'] = 'error'
        response['description'] = 'wrong token'
    else:
        response['code'] = 'ok'
    response['request'] = request.args
    return jsonify(response)

@app.route('/api/v1/messages/receive', methods=['GET'])
def api_receive():
    response = {}
    if 'token' not in request.args:
        response['code'] = 'error'
        response['description'] = 'token not present'
    elif not request.args['token'] == '11223344556677889900':
        response['code'] = 'error'
        response['description'] = 'wrong token'
    else:
        response['code'] = 'ok'
    response['messages'] = []
    response['request'] = request.args
    return jsonify(response)

if __name__ == '__main__':
    app.run()
