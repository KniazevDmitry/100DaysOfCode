import random
import time
from turtle import Screen
from day20.food import Food
from day20.scoreboard import Scoreboard
from day20.snake import Snake


class Bomb(Food):
    def create(self):
        super().create()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food1 = Food()
food2 = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
is_bomb_food1 = random.choice([True, False])  # Randomly assign one as a bomb

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food1) < 15:
        if is_bomb_food1:  # If food1 is the bomb
            game_is_on = False
            scoreboard.game_over()
            screen.bgcolor("red")
            screen.update()
            time.sleep(0.5)
            screen.bgcolor("black")
        else:  # If food1 is not the bomb
            food2.refresh()  # Keep food2 and refresh food1
            food1.refresh()
            scoreboard.increase_score()
            snake.extend()
            is_bomb_food1 = random.choice([True, False])  # Randomly reassign bomb

    if snake.head.distance(food2) < 15:
        if not is_bomb_food1:  # If food2 is the bomb
            game_is_on = False
            scoreboard.game_over()
            screen.bgcolor("red")
            screen.update()
            time.sleep(0.5)
            screen.bgcolor("black")
        else:  # If food2 is not the bomb
            food1.refresh()  # Keep food1 and refresh food2
            food2.refresh()
            scoreboard.increase_score()
            snake.extend()
            is_bomb_food1 = random.choice([True, False])  # Randomly reassign bomb

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
