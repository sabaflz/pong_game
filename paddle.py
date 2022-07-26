from turtle import Turtle

MOVE_CONSTANT = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(UP)
        self.set_position(side)

    def set_position(self, side):
        if side == "right":
            self.setposition(350, 0)
        elif side == "left":
            self.setposition(-350, 0)

    def move(self):
        self.set_direction()
        self.forward(MOVE_CONSTANT)

    def up(self):
        self.setheading(UP)

    def down(self):
        self.setheading(DOWN)

    def set_direction(self):
        if self.ycor() > 250:
            self.down()
        elif self.ycor() < -250:
            self.up()
