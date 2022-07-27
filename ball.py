from turtle import Turtle
import random

MOVE_CONSTANT = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        if 360 > self.xcor() > -360 and 280 > self.ycor() > -280:
            self.setheading(37)
            self.forward(MOVE_CONSTANT)
        # self.goto(370, 280)
