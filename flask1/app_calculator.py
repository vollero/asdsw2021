from flask import Flask
from markupsafe import escape
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Welcome!\nThis is my calculator /calculator\n...'

@app.route('/calculator/sum/<op1>/<op2>')
def add(op1, op2):
    result = str(int(op1) + int(op2))
    output = {}
    output['op1'] = op1
    output['op2'] = op2
    output['res'] = result
    return '{}'.format(json.dumps(output))

@app.route('/calculator/diff/<op1>/<op2>')
def diff(op1, op2):
    result = str(int(op1) - int(op2))
    output = {}
    output['op1'] = op1
    output['op2'] = op2
    output['res'] = result
    return '{}'.format(json.dumps(output))

@app.route('/calculator/div/<op1>/<op2>')
def div(op1, op2):
    result1 = str(int(op1)//int(op2))
    result2 = str(int(op1)%int(op2))
    output = {}
    output['op1'] = op1
    output['op2'] = op2
    output['res'] = result1
    output['mod'] = result2
    return '{}'.format(json.dumps(output))

@app.route('/calculator/mul/<op1>/<op2>')
def mul(op1, op2):
    result = str(int(op1)*int(op2))
    output = {}
    output['op1'] = op1
    output['op2'] = op2
    output['res'] = result
    return '{}'.format(json.dumps(output))
