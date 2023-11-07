from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello there!</h1>"


@app.route("/bye")
def say_bye():
    return "<h1>Goodbye my friend...</h1>"


if __name__ == "__main__":
    app.run()
