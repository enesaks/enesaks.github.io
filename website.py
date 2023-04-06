from flask import flask

app = flask(__name__)

@app.route('/')
def index():
    return '<h1>TEST PYTHON</h1>'