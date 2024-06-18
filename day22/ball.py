from turtle import Turtle
from scoreboard import Scoreboard


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 2
        self.y_move = 2

    def move(self, bounces):
        speed_modifier = 1 + bounces / 8
        new_x = self.xcor() + self.x_move * speed_modifier
        new_y = self.ycor() + self.y_move * speed_modifier
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
