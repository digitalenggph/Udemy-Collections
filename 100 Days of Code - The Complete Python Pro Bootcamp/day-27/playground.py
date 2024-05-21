"""
DAY-27-NOTES:
Unlimited arguments
positional arguments

def add(n1, n2):
    return n1 + n2

for unlimited n,

def add(*args):
    for n in args:
        print(n)


**kwargs
arbitrary number of keyword arguments

"""


def add(*numbers):
    return sum(numbers)


sum_playground = add(1, 2, 3)


# print(sum_playground)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # will return error if values inside square bracket is not defined
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        # solution: will just return None
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car()
print(my_car.model)


