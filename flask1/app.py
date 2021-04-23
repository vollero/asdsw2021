from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Home!'

@app.route('/hidden')
def hidden():
    return 'Hello, Hidden'
