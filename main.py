from turtle import Screen
from setup import Setup
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.tracer(0)

Setup()
Setup().net()

# place paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# place ball
ball = Ball()

# place scoreboards
r_score = Score((30, 240), "orange")
l_score = Score((-30, 240), "pink")

# move paddles
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "e")
screen.onkey(left_paddle.down, "d")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# x = 0.05
#
# # altering speed of ball/sleep. Should also allow paddles to move incrementally faster
# def increase_speed():
#     global x
#     x += 0.05


# detect collision with paddle
def paddle_collision():
    if ball.xcor() > 330:
        if ball.distance(right_paddle) < 70:
            ball.paddle_bounce()
    if ball.xcor() < -330:
        if ball.distance(left_paddle) < 70:
            ball.paddle_bounce()



def get_points():
    if ball.xcor() > 400:
        l_score.score()
    if ball.xcor() < -400:
        r_score.score()

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    paddle_collision()
    get_points()
    ball.wall_bounce()
    ball.angle_reset()

screen.exitonclick()
