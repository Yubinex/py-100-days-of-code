from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif" />'


@app.route('/bye')
@make_bold
@make_underline
@make_emphasis
def say_bye():
    return "Bye"


@app.route('/username/<name>/<int:number>')
def greet(name: str, number: int):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
