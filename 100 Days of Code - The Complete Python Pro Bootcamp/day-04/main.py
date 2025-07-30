# This code was migrated from replit to GitHub

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_elements = [rock, paper, scissors]

import random

computer_choice = random.randint(0, 2)

your_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

if your_choice < 0 and your_choice > 2:
  print("You typed an invalid number, you lose!")

else:
  print(game_elements[your_choice])
  print("Computer chose:")
  print(game_elements[computer_choice])

  if your_choice == 0 and computer_choice == 1:
      print("You lose!")
  elif your_choice == 0 and computer_choice == 2:
      print("You win!")
  elif your_choice == 1 and computer_choice == 0:
      print("You win!")
  elif your_choice == 1 and computer_choice == 2:
      print("You lose!")
  elif your_choice == 2 and computer_choice == 0:
      print("You lose!")
  elif your_choice == 2 and computer_choice == 1:
      print("You win!")
  else:
      print("It's a tie!")
