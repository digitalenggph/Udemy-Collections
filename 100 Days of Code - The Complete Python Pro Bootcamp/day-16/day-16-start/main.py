# import another_module
# from turtle import Turtle, Screen
#
# print(another_module.another_variable)
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral", "azure")
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# timmy.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

table.align = "l"


print(table)