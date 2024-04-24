# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("img.jpeg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import random
from turtle import Turtle, Screen

rgb_colors = [(171, 6, 99), (221, 155, 88), (112, 170, 210), (199, 63, 167), (197, 132, 178), (180, 41, 145),
              (46, 106, 164), (181, 80, 24), (236, 213, 91), (112, 89, 204)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(20)
tim.hideturtle()
tim.speed(0)

screen.screensize(700, 700)


def start_position():
    tim.penup()
    tim.setpos(- screen.canvwidth / 2, - screen.canvheight / 2)
    tim.pendown()


def random_color():
    return random.choice(rgb_colors)


def draw_dots_line():
    for _ in range(10):
        tim.color(random_color())
        tim.forward(1)
        tim.penup()
        tim.forward(49)
        tim.pendown()
    tim.penup()
    tim.goto(- screen.canvwidth / 2, tim.ycor() + 50)
    tim.pendown()


def draw_dots():
    for _ in range(1, 11):
        draw_dots_line()


start_position()
draw_dots()

screen.exitonclick()
