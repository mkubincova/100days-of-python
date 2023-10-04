from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.goto(position)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

