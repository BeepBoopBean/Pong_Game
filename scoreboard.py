from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Score(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.hideturtle()
        self.color(color)
        self.points = 0
        self.up()
        self.goto(position)
        self.update_scoreboard()

    def score(self):
        self.points += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.points, False, align=ALIGNMENT, font=FONT)
