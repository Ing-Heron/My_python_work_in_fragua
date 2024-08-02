from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    def inner():
        return f"<em>{func()}</em>"
    return inner


def make_underline(func):
    def inner():
        return f"<u>{func()}</u>"
    return inner


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTZyZjlldXozNXRzMnRnajIzdmFzMnE3ajBsZm4zNzlzZmN'
            'lOXo1ZiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/AfYUx4B4AHCzeGR2mM/giphy.gif"/>')


# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return '"<p style="font-size: 2rem">Bye!</p>"'


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
