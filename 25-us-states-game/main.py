import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Type another state name:").title()
    if answer_state == "Exit":
        # states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                state_data = data[data.state == state]
                pen.color("red")
                pen.goto(x=int(state_data.x.iloc[0]), y=int(state_data.y.iloc[0]))
                pen.write(state_data.state.iloc[0])
        #         states_to_learn.append(state)
        # new_data = pandas.DataFrame(states_to_learn)
        # new_data.to_csv("states_to_lear.csv")
        break
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        pen.goto(x=int(state_data.x.iloc[0]), y=int(state_data.y.iloc[0]))
        pen.write(answer_state)
        guessed_states.append(answer_state)


turtle.mainloop()
