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


def print_state(state_data, color="black"):
    pen.color(color)
    pen.goto(x=int(state_data.x.iloc[0]), y=int(state_data.y.iloc[0]))
    pen.write(state_data.state.iloc[0])


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Type another state name:").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        for state in missing_states:
            print_state(data[data.state == state], "red")
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_lear.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        print_state(data[data.state == answer_state])
        guessed_states.append(answer_state)


turtle.mainloop()
