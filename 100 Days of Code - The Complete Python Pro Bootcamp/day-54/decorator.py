"""
DAY-54 NOTES
    Python Decorator    - function that wraps another function
    Syntactic sugar     -

"""
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


# @delay_decorator
# def say_hello():
#     print("Hello")
#
#
# def say_bye():
#     print("Bye")
#
#
# @delay_decorator
def say_greeting():
    print("Greeting")


decorated_function = delay_decorator(say_greeting)
decorated_function()
