# This code was migrated from replit to GitHub

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_component = []
for letter in range(0, nr_letters):
  letter_component.append(random.choice(letters))

symbol_component = []
for symbol in range(0, nr_symbols):
  symbol_component.append(random.choice(symbols))

number_component = []
for number in range(0, nr_numbers):
  number_component.append(random.choice(numbers))

len_password = nr_letters+nr_symbols+nr_numbers
password_unrandomised_list = letter_component + symbol_component + number_component

password_unrandomised_string = ""
for char in password_unrandomised_list:
  password_unrandomised_string += char

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_randomised_list = []
for char_pass in range(0,len_password):
  # password_randomised_list.append(random.choice(password_unrandomised_list))
    password_randomised_list += random.sample(password_unrandomised_string,1)

password_randomised_string = ""
for char in password_randomised_list:
  password_randomised_string += char

password_randomised_string=''.join(random.sample(password_unrandomised_string,len_password))

print(password_unrandomised_string)
print(password_randomised_string)


