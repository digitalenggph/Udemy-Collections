#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_split = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
tip_percentage_float = float(tip_percentage)
people_split_float = float(people_split)

tip_percentage_float_final = tip_percentage_float / 100
total_bill_with_tip = total_bill_float * (1 + tip_percentage_float_final)

bill_with_tip_per_person = "{:.2f}".format(total_bill_with_tip / people_split_float)

print(f"Each person should pay: ${bill_with_tip_per_person}")
# This code was migrated from replit to GitHub