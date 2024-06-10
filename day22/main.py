from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

ball = Ball()

screen.listen()

screen.onkey(paddle_left.move_up, 'w')
screen.onkey(paddle_left.move_down, 's')

screen.onkey(paddle_right.move_up, 'Up')
screen.onkey(paddle_right.move_down, 'Down')

game_is_on = True
while game_is_on:
    ball.ball_move()
    screen.update()

screen.exitonclick()
