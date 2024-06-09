from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.level_score += 1
        str_turtle = "Level: " + str(self.level_score)
        self.write(str_turtle,
                   align="center",
                   font=FONT
                   )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!",
                   align="center",
                   font=FONT
                   )
