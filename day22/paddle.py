from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        def paddle_create(coordinates):
            self.goto(coordinates)

        paddle_create(position)

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)
