"""
DAY-27-NOTES:
Unlimited arguments

def add(n1, n2):
    return n1 + n2

for unlimited n,

def add(*args):
    for n in args:
        print(n)

"""


def add(*numbers):
    return sum(numbers)


sum_playground = add(1, 2, 3)

print(sum_playground)
