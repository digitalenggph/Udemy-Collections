import turtle as t
from random import choice, randint
from tkinter_colors import colors

timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.color("black", "coral")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    randcolor = (r, g, b)
    return randcolor


# move
# # make square
# for sides in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# # dashed line
# for segment in range(20):
#     if segment % 2 == 0:
#         timmy.pendown()
#     else:
#         timmy.penup()
#
#     timmy.forward(10)

# # draw polygon with 3 side to 10 sides
# for n_polygon in range(3, 11):
#     exterior_angle = 360/n_polygon
#     pencolor = choice(colors)
#     timmy.pencolor(pencolor)
#     for segment in range(n_polygon):
#         timmy.right(exterior_angle)
#         timmy.forward(100)


# for i in range(200):
#     # pencolor = choice(colors)
#     pencolor = random_color()
#     timmy.pencolor(pencolor)
#     timmy.pensize(10)
#     timmy.speed(10)
#     t_rotate = randint(1, 5) * 90
#     timmy.right(t_rotate)
#     timmy.forward(25)

timmy.speed("fastest")

for i in range(int(360/5)):
    timmy.pencolor(random_color())
    timmy.circle(100)
    timmy.setheading(5*i)



screen = t.Screen()
screen.exitonclick()
