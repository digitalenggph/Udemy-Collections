# This code was migrated from replit to GitHub

from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program. ")

bidders_list = {}

any_bidders = "yes"

while any_bidders == "yes":
    bidder_name = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))
    bidders_list[bidder_name] = bid_price
    any_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    clear()

highest_bid = 0
for bidder in bidders_list:
    if bidders_list[bidder] > highest_bid:
        highest_bid = bidders_list[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}.")