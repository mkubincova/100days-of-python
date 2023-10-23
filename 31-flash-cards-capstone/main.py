from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_lear.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_front_label, text="French", fill="#000")
    canvas.itemconfig(card_front_word, text=current_card["French"], fill="#000")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_front_label, text="English", fill="#fff")
    canvas.itemconfig(card_front_word, text=current_card["English"], fill="#fff")


def right_answer():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("./data/words_to_lear.csv", index=False)

    next_card()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Card
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)

card_front_label = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="#000")
card_front_word = canvas.create_text(400, 253, text="word", font=("Arial", 60, "bold"), fill="#000")

canvas.grid(column=0, row=0, columnspan=2)

# Right
right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=right_answer)
button_right.grid(column=1, row=1)

# Wrong
wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(column=0, row=1)

next_card()

window.mainloop()
