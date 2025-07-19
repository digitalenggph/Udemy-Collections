from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.start_position()
        self.head = self.snake_body[0]

    def start_position(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
            # self.snake_body[0].left(90)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.start_position()
        self.head = self.snake_body[0]

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.snake_body[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
