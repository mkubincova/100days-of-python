import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter color: ")

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
is_race_on = False

for turtle_index in range(0, len(colors)):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230, y=-70 + turtle_index * 30)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You won! The winner is {winning_color} turtle.")
            else:
                print(f"You lost...The winner is {winning_color} turtle.")

screen.exitonclick()