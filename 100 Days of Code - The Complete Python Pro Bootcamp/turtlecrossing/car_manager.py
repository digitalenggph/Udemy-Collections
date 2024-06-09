from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
BORDER_Y_LIMIT = (-240, 240)
STRETCH_LEN = [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=choice(STRETCH_LEN))
        self.color(choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(260, randint(-240, 240))
        self.move()

    def move(self):
        self.forward(10)

