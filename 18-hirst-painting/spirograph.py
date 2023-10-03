import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(50)
        tim.right(gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
