from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.up()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        self.penup()
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        self.penup()
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
