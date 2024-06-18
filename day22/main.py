import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.move_up, 'w')
screen.onkey(paddle_left.move_down, 's')
screen.onkey(paddle_right.move_up, 'Up')
screen.onkey(paddle_right.move_down, 'Down')


def play_game():
    game_is_on = True

    ball.goto(0, 0)

    ball.bounce_x()

    bounces = 0

    while game_is_on:
        time.sleep(0.01)

        ball.move(bounces)
        print(bounces)

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
            bounces += 1

        if ball.xcor() > 330 and ball.distance(paddle_right) < 50:
            ball.bounce_x()
            bounces += 1
        if ball.xcor() > 380:
            scoreboard.l_points()
            game_is_on = False
            time.sleep(1.5)
            play_game()

        if ball.xcor() < -330 and ball.distance(paddle_left) < 50:
            ball.bounce_x()
            bounces += 1
        if ball.xcor() < -380:
            scoreboard.r_points()
            game_is_on = False
            time.sleep(1.5)
            play_game()

        screen.update()


play_game()

screen.exitonclick()
