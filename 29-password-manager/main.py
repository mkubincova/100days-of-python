from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_psw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    psw = ([random.choice(letters) for _ in range(random.randint(8, 10))] +
           [random.choice(symbols) for _ in range(random.randint(2, 4))] +
           [random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(psw)
    random_password = ''.join(psw)

    password_input.delete(0, END)
    password_input.insert(0, string=random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any empty fields!")
        return

    save_to_file = messagebox.askokcancel(title=website,
                                          message=f"These are the details entered: \nUsername: {username} "
                                                  f"\nPassword: {password} \nIs it okay?")
    if save_to_file:
        with open("data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {username} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E")

website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

# Username / Email
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, sticky="E")

username_input = Entry()
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(0, string="mkubincova@proton.me")

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate Password", command=generate_psw)
password_button.grid(column=2, row=3)

# Submit form
submit_button = Button(text="Add", command=save_data)
submit_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
