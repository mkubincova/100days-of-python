import tkinter as t

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    heading.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        heading.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        heading.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        heading.config(text="Work", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    formatted_time = f"{int(count / 60):0>2}:{int(count % 60):0>2}"
    canvas.itemconfig(timer_text, text=formatted_time)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

heading = t.Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
heading.grid(column=1, row=0)

canvas = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = t.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_btn = t.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = t.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)

checkmarks = t.Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()

