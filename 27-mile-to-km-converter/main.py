import tkinter as t

window = t.Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)


def convert_miles():
    km = float(input_miles.get()) * 1.60934
    km_value.config(text=f"{round(km)}")


# Miles
input_miles = t.Entry(width=10)
input_miles.grid(column=1, row=0)

input_label = t.Label(text="Miles")
input_label.grid(column=2, row=0)

# Description text
text = t.Label(text="is equal to")
text.grid(column=0, row=1)

# Kilometers
km_value = t.Label(text="0")
km_value.grid(column=1, row=1)

km_label = t.Label(text="Km")
km_label.grid(column=2, row=1)

# Submit
button = t.Button(text="Calculate", command=convert_miles)
button.grid(column=1, row=2)


window.mainloop()