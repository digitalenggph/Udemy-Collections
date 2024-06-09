import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    cars = []
    player = Player()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=player.move_up, key="Up")
    screen.onkey(fun=player.move_left, key="Left")
    screen.onkey(fun=player.move_right, key="Right")

    game_is_on = True
    while game_is_on:
        time.sleep(player.move_speed)
        screen.update()

        # create car
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            cars.append(CarManager())

        for car in cars:
            car.move()
            stretch_width = car.shapesize()[1]
            car_dist = stretch_width * 20 / 2

            # identify collisions
            if player.distance(car) < 20 and (player.ycor() > car.ycor() - 10 or
                                              car.xcor() - car_dist <= player.xcor() <= car.xcor() + car_dist):
                scoreboard.game_over()
                game_is_on = False

        if player.ycor() >= 260:
            scoreboard.update_scoreboard()
            player.reset()


    screen.exitonclick()
