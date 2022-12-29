from turtle import Turtle
FONT = ("Courier", 24, "normal")
TEXT_POSITION = (-200, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(TEXT_POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)


