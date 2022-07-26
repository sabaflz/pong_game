from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from vertical_line import VerticalLine
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle_right = Paddle("right")
paddle_left = Paddle("left")
scoreboard = Scoreboard()
vertical_line = VerticalLine()

screen.listen()

screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    paddle_right.move()
    paddle_left.move()


screen.exitonclick()
