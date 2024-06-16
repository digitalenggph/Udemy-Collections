"""`
DAY-55 NOTES
    LESSON 1:
    * Debug mode    - ON/OFF -> automatic reloader
                    - ON -> debug=True

    LESSON 2:
    * HTML styles


`"""
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return '<em>' + function() + '</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return '<u>' + function() + '</u>'
    return wrapper_function


@app.route("/")
def hello():
    return ('<h1 style="text-align:center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media2.giphy.com/media/v1'
            '.Y2lkPTc5MGI3NjExeHdncHl0Y2kwNWN4ZHlxYWZ0ZXh6ZzMxZW'
            'RuYmVrdmV2MTJhdnE3dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pJmnk86fXFNmrUb8LB/giphy.webp">')


@app.route("/bye")
@make_emphasis
@make_underlined
@make_bold
def say_bye():
    return "Bye"


@app.route("/<name>")
def greet(name):
    return f"Hello there! {name}"


if __name__ == "__main__":
    app.run(debug=True)

# --------------------------------------------------- REFERENCES ---------------------------------------------------- #
"""
https://stackoverflow.com/questions/70676351/is-there-a-flask-function-called-mak
e-bold-i-am-very-confused-as-i-am-not-abl
"""

