#!/usr/bin/python3
'''
    script that starts a Flask web application
    listening in on 0.0.0.0 port 5000
    route '/'
          '/hbnb'
          '/c/<text>'
          '/python/<text>'
          '/number/<n>'
          '/number_template/<n>'
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''display greeting'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' display "HBNB" '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    ''' display “C ” followed by the value of the text variable
        and replace underscore _ symbols with a space
    '''
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    ''' display “C ” followed by the value of the text variable
        display “Python ”, followed by the value of the text variable
        and replace underscore _ symbols with a space
    '''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def int_n(n):
    ''' display “n is a number” only if n is an integer '''
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    ''' display a HTML page only if n is an integer '''
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
