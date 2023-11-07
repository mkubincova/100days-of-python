from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</>"
    return wrapper


@app.route("/")
def hello_world():
    return "<h1>Hello there!</h1>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Goodbye my friend..."


@app.route("/<name>")
def greet(name):
    return (f"<h1>Hello there {name}</h1>"
            f"<img src='https://media.giphy.com/media/Y4pAQv58ETJgRwoLxj/giphy-downsized-large.gif' />")


if __name__ == "__main__":
    app.run(debug=True)
