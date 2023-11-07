from flask import Flask
import random

app = Flask(__name__)
random_num = 0


@app.route("/")
def home():
    global random_num
    random_num = random.randint(0, 9)
    print(random_num)
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/bYg33GbNbNIVzSrr84/giphy-downsized-large.gif' alt='Matrix style puppy'/>")


@app.route("/<int:guess>")
def guess_number(guess):
    if guess == random_num:
        return ("<h1 style='color: green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/TjGm3jg5sgV1mBmq8d/giphy.gif' alt=''/>")
    elif guess > random_num:
        return ("<h1 style='color: purple'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/dsdN8wbqOAuhGbb4Sw/giphy.gif' alt=''/>")
    else:
        return ("<h1 style='color: orange'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/URoLoCo1s9jm8/giphy.gif' alt=''/>")


if __name__ == "__main__":
    app.run(debug=True)
