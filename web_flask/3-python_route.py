#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    txt = text.replace('_', " ")
    return "C {}". format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    txt = text.replace('_', " ")
    return "Python {}". format(txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
