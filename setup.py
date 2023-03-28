from turtle import Turtle, Screen


net = Turtle()


class Setup(Turtle):

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.hideturtle()
        self.screen.setup(800, 600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")

    def net(self):
        net.color("white")
        net.shape("square")
        net.shapesize(30, 0.25)
        net.up()



