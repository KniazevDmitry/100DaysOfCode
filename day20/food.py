import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_coordinate = random.randint(-14, 14) * 20
        y_coordinate = random.randint(-14, 14) * 20
        self.goto(x_coordinate, y_coordinate)
