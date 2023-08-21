# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/cow')
def cow():
    return 'MOoooOo!'

@app.route('/chicken')
def chicken():
    return 'Pok! Pok! Pok!'

@app.route('/pig')
def pig():
    return 'Oink! Oink!'

@app.route('/sheep')
def sheep():
    return 'Baaaah!'