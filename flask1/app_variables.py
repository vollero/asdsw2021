from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Home!'

@app.route('/hidden')
def hidden():
    return 'Hello, Hidden'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hello {}, Welcome to you personal profile!'.format(escape(username))

@app.route('/calcolatrice/+/<add1>/<add2>')
def add(add1, add2):
    return '{} + {} = {}'.format(escape(add1), escape(add2), escape(str(int(add1) + int(add2))))
