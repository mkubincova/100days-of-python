from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.lvl = 1
        self.print_lvl()

    def print_lvl(self):
        self.clear()
        self.write(f"Level: {self.lvl}", font=FONT)

    def lvl_up(self):
        self.lvl += 1
        self.print_lvl()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)