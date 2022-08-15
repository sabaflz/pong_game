from turtle import Turtle
import random

MOVE_CONSTANT = 10
MOVE_SPEED = 0.1
BALL_SPEED_RATE = 0.9


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = MOVE_CONSTANT
        self.y_move = MOVE_CONSTANT
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= BALL_SPEED_RATE

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED
        self.bounce_x()
