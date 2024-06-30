"""
DAY-26-NOTES:
List Comprehension
new_list = [new_item for item in list]

Usual for loop
numbers = [1, 2, 3]
new_list = []

for n in list:
    add_1 = n + 1
    new_list.append(add_1)

List comprehension
new_list = [n + 1 for n in numbers]
print(new_list)
"""

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = 'Karen'
new_list = [letter for letter in name]
print(new_list)

new_list = [2 * x for x in range(1, 5)]
print(new_list)

"""
Conditional List Comprehension

new_list = [new_item for item in list if test]
"""
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]
print(short_names)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)