import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_counter_clockwise():
    tim.left(10)


def clear_canvas():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_canvas)


screen.exitonclick()