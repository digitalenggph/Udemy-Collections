from art import logo, vs
from game_data import data
from random import sample
from replit import clear


# Display Art
print(logo)

# Random account generator
def generate_comparison(data_to_randomize):
  objects_to_compare = sample(data_to_randomize, 2)
  return objects_to_compare

# Compares follower count
def compare_followers(data1_list, data2_list):
  if data1_list['follower_count'] > data2_list['follower_count']:
    return 'A'
  else:
    return 'B'


def higher_lower_game(score, dataA_list, dataB_list):
  print(f"Compare A: {dataA_list['name']}, a {dataA_list['description']}, from {dataA_list['country']}.")
  print(vs)
  print(f"Compare B: {dataB_list['name']}, a {dataB_list['description']}, from {dataB_list['country']}.")

  # Ask user who wins
  guess_who_wins = input("Who has more followers? Type 'A' or 'B': ")
  score_counter = score

  # They got it right! So game continues + Position B becomes position A
  if compare_followers(dataA_list, dataB_list) == guess_who_wins:
    score_counter +=1
    if guess_who_wins == 'A':
      dataA_list = dataA_list
    else:
      dataA_list = dataB_list

    dataB_list = generate_comparison(data)[0]
    while dataB_list == dataA_list:
      dataB_list = generate_comparison(data)[0]
    
    clear()
    print(logo)
    print(f"You're right! Current score: {score_counter}.")
    higher_lower_game(score_counter, dataA_list, dataB_list)

  # They got it wrong :> So game stops.
  else:
    print(f"Sorry, that's wrong. Final score: {score_counter}")
    if input("Do you want to play again? Type y or n: ") =="y":
      clear()
      higher_lower_game(0, generate_comparison(data)[0], generate_comparison(data)[1])

# Calls game
"""
parameters(starting score, initial data 1, initial data 2)
"""
initial_dataA_list = generate_comparison(data)[0]
initial_dataB_list = generate_comparison(data)[1]
higher_lower_game(0, initial_dataA_list, initial_dataB_list)


# for i in range(0,len(objects_to_compare)):
#   # print(objects_to_compare[i])
#   for key in objects_to_compare[i]:
#     if key == 'name':
#       print(objects_to_compare[i]['name'])

# print(objects_to_compare[0]['name'])
# print(objects_to_compare[1]['name'])
# for items in objects_to_compare:
#   print(objects_to_compare)

# print("Compare ")