from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

BORDER_LINE_X = (-280, 280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() >= BORDER_LINE_X[0]:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())
        else:
            self.goto(BORDER_LINE_X[0], self.ycor())

    def move_right(self):
        if self.xcor() <= BORDER_LINE_X[1]:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())
        else:
            self.goto(BORDER_LINE_X[1], self.ycor())

    def reset(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.9

