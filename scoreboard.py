from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(-200, 250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(F"score :{self.score}/50 ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
