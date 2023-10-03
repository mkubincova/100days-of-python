import turtle as t
import random
import colorgram

tim = t.Turtle()
t.colormode(255)
tim.speed("fast")
colors = colorgram.extract('original.jpeg', 30)


def random_color():
    color = random.choice(colors)
    return color.rgb[:]


def draw_dots(row, column, dot_size=20, gap=50):
    tim.up()
    tim.hideturtle()
    start_x = (column - 1) * gap / 2 * -1
    start_y = (row - 1) * gap / 2 * -1
    tim.setx(start_x)
    tim.sety(start_y)
    for i in range(row):
        for j in range(column):
            tim.down()
            tim.dot(dot_size, random_color())
            tim.up()
            tim.forward(gap)

        tim.setheading(tim.heading() + 90)
        tim.forward(gap)
        tim.setheading(tim.heading() - 90)
        tim.setx(start_x)


draw_dots(10, 10)

screen = t.Screen()
screen.exitonclick()
