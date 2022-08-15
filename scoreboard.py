from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_WEIGHT = "normal"
FONT_SIZE = 48


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score_r = 0
        self.score_l = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.update_score("none")

    def update_score(self, winner):
        self.clear()
        if winner == "right":
            self.score_r += 1
        elif winner == "left":
            self.score_l += 1

        self.write(f"{self.score_l}   {self.score_r}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))

