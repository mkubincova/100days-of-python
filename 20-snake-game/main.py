import turtle as t
import random
import time
from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()


# TODO: detect collision wih food
# TODO: create score board
# TODO: detect collision with wall
# TODO: detect collision with tail


screen.exitonclick()
