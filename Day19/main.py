import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False

screen.setup(500, 500)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? Print a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for t in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=-230, y=y_position[t])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            print(f"The winning turtle is {winning_color}")
            if user_bet == winning_color:
                print("You win!")
            else:
                print("You lose!")

        random_distance = random.randint(0, 10)
        t.forward(random_distance)


screen.exitonclick()
