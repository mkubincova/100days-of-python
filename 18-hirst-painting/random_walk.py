import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
angles = [90, 180, 270, 360]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.pensize(10)
tim.speed(9)

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.right(random.choice(angles))


screen = t.Screen()
screen.exitonclick()
