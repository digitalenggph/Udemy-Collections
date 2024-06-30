from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.y_bounce_dir = 1
        self.x_bounce_dir = 1
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + 10 * self.x_bounce_dir
        new_y = self.ycor() + 10 * self.y_bounce_dir
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_bounce_dir *= -1
        self.move()

    def bounce_x(self):
        self.x_bounce_dir *= -1
        self.move()
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()