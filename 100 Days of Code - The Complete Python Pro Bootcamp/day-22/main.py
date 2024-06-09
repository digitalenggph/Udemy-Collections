from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_POSITION = [(-350, 0), (350, 0)]

# TODO: 1. Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# TODO: 2. Create and move a paddle
l_paddle = Paddle(STARTING_POSITION[0])

# TODO: 3. Create another paddle
r_paddle = Paddle(STARTING_POSITION[1])

# TODO: 4. Create the ball and make it move
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    x_limit, y_limit = screen.window_width() / 2 - 10, screen.window_height() / 2 - 10

    # TODO: 5. Detect collision with wall and bounce
    if not -y_limit <= ball.ycor() <= y_limit:
        ball.bounce_y()

    # TODO: 6. Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > x_limit - 60 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < -x_limit + 60:
        ball.bounce_x()

    # TODO: 7. Detect when the paddle misses
    if ball.xcor() >= x_limit:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() <= -x_limit:
        ball.reset_position()
        scoreboard.r_point()

    # TODO: 8. Keep score

screen.exitonclick()
