from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from vertical_line import VerticalLine
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
scoreboard = Scoreboard()
vertical_line = VerticalLine()
ball = Ball()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    ball.move()

    # right_paddle.move()
    # left_paddle.move()


screen.exitonclick()
