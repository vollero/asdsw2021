from flask import Flask

app = Flask(__name__)

def h1_decorator(function):
    def wrapper_h1():
        func = function()
        add_h1 = '<h3>{}</h3>'.format(func)
        return add_h1
    return wrapper_h1

def h2_decorator(function):
    def wrapper_h2():
        func = function()
        add_h1 = '<h2>{}</h2>'.format(func)
        return add_h1
    return wrapper_h2

@app.route('/')
@h1_decorator
def hello():
    return 'Hello, Home!'

@app.route('/hidden')
@h2_decorator
def hidden():
    return 'Hello, Hidden'
