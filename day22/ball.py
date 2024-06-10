import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('slow')

        def ball_create():
            heading = random.randint(0, 360)
            self.setheading(heading)

        ball_create()

    def ball_move(self):
        self.forward(4)
