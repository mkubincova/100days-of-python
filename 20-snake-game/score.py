from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 20, "normal")
FONT_SM = ("Courier New", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.sety(270)
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.sety(-280)
        self.write("Press 'x' to exit game.", align=ALIGNMENT, font=FONT_SM)

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.print_score()
