from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("YOU DIED", True, align=ALIGNMENT, font=FONT)
