from turtle import Turtle

MOVE_CONSTANT = 30
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.8, stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(UP)
        self.set_position(side)

    def set_position(self, side):
        if side == "right":
            self.setposition(370, 0)
        elif side == "left":
            self.setposition(-380, 0)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_CONSTANT)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_CONSTANT)

