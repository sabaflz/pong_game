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
    time.sleep(0.09)

    ball.move()

    # Detect the collision of the ball with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect when the right paddle misses
    if ball.xcor() > 340:
        ball.reset_position()

    # Detect when the left paddle misses
    if ball.xcor() < -350:
        ball.reset_position()


screen.exitonclick()
