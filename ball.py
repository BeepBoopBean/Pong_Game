from turtle import Turtle, Screen
import random
import time

screen = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.direction = None
        self.shape("circle")
        self.color("white")
        self.up()
        self.goto(0, 0)
        self.random_direction()
        self.speed = 10

    def random_direction(self):
        choice_a = random.randint(10, 60)
        choice_b = random.randint(120, 170)
        choice_c = random.randint(190, 240)
        choice_d = random.randint(300, 350)
        self.direction = random.choice([choice_a, choice_b, choice_c, choice_d])
        self.setheading(self.direction)

    def move(self):
        self.forward(self.speed)

    def wall_bounce(self):
        # bouncing against top of screen
        if self.ycor() > 290:
            # if it goes to the top-right
            if self.heading() < 90:
                x = 90 - self.heading()
                self.setheading(270 + x)
            # if it goes to the top-left
            if 180 > self.heading() > 90:
                x = 270 - self.heading()
                self.setheading(90 + x)
        # bouncing against bottom of screen
        if self.ycor() < -290:
            # if it goes to the bottom-right
            if 270 < self.heading() < 360:
                x = self.heading() - 270
                self.setheading(90 - x)
            # if it goes to the bottom-left
            if 180 < self.heading() < 270:
                x = self.heading() - 90
                self.setheading(270 - x)

    def angle_reset(self):
        if self.xcor() > 400 or self.xcor() < -400:
            self.goto(0, 0)
            self.color("white")
            screen.tracer(1)
            screen.delay(30)
            self.speed = 10
            self.random_direction()
            screen.tracer(0)

    def paddle_bounce(self):
        # if it goes toward the top-right
        if 0 < self.heading() < 90:
            x = 90 - self.heading()
            self.setheading(90 + x)
            self.forward(10)
            self.color("orange")
            self.speed += 1
        # if it goes toward the top-left
        elif 180 > self.heading() > 90:
            x = 270 - self.heading()
            self.setheading(270 + x)
            self.color("pink")
            self.speed += 1
        # if it goes toward the bottom-right
        elif self.heading() > 270:
            x = self.heading() - 270
            self.setheading(270 - x)
            self.forward(10)
            self.color("orange")
            self.speed += 1
        # if it goes toward the bottom-left
        elif 180 < self.heading() < 270:
            x = self.heading() - 90
            self.setheading(90 - x)
            self.forward(10)
            self.color("pink")
            self.speed += 1
# Abby you have bad math the ball only turns pink and blue yo udingsu
# ELIF YOU GOOBER
