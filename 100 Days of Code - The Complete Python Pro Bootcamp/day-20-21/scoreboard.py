from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

with open("data.txt", mode='r') as store_score:
    high_score = int(store_score.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as update_score:
                update_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def add(self):
        self.score += 1
        self.update_scoreboard()
