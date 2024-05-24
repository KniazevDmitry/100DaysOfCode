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

        x_coordinate = random.randint(-14, 14) * 20
        y_coordinate = random.randint(-14, 14) * 20
        print(f"x: {x_coordinate}, y: {y_coordinate}")

        self.goto(x_coordinate, y_coordinate)
