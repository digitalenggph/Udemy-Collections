import colorgram
import turtle as t
import random
from color import color_list

timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)

x_pos = int(-1 * (50 * 9)/2)
y_pos = x_pos
timmy.speed("fastest")

for i in range(100):
    timmy.penup()
    timmy.sety(y_pos)
    timmy.setx(x_pos)

    if i % 10 == 0 and i != 0:
        y_pos += 50
        x_pos = int(-1 * (50 * 9)/2)

    timmy.teleport(x_pos, y_pos)
    timmy.dot(20, random.choice(color_list))
    x_pos += 50

timmy.pendown()
timmy.teleport(0, 0)
timmy.hideturtle()

screen.exitonclick()













# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r , g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


# size 20 spaced 50
