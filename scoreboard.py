from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_WEIGHT = "normal"
FONT_SIZE = 48


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score_a = 0
        self.score_b = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_a}   {self.score_b}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))

