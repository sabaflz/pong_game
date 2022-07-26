from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_WEIGHT = "normal"
FONT_SIZE = 48

UP = 90
MOVE_CONSTANT = 20


class VerticalLine(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.penup()
        self.setheading(UP)
        self.setposition(0, -280)
        self.draw_vertical_line()

    def draw_vertical_line(self):
        while self.ycor() < 290:
            self.dot()
            self.forward(MOVE_CONSTANT)

