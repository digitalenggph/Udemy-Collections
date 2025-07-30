print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
first_round = input(
    "You are at a crossroads. To the left is where the CEAT building is and to the right is where the library inside a forest is.\nWhich way do you want to go? L or R? \n")

if first_round == "L":
    print("You have arrived at the CEAT building where you are greeted by your hydrology teacher Sir Mau. \n")

    second_round = input(
        "\n He told you that you have to get a water sample along Molawin Creek that will be used for water quality activity. Where do you want to go get a sample? Type S if you want to get a sample near SU building or type L if you want to get a sample near the library. \n")
    if second_round == "S":
        print(
            "You have been saved by the stinky waters of Molawin Creek nearby SU building! \n You have successfully collected the sample from the Molawin Creek. \n You put your sample in three separate test tubes, put it in a centrifuge machine and waited for 5 minutes for the sediment to settle at the bottom. \n You picked up the tubes and saw that test tube 1 has turned to brown B, test tubes 2 and 3 have turned to igneous red and bulbasaur green, respectively.")
        third_round = input(
            "Which one do you think will help you find the treasure that is a 1.00 in the hydrology subject? Type B for brown, R for red or G for green.\n")
        if third_round == "B":
            print("You have released a very unmighty smell in the room. You fainted and died. Game over.")
        elif third_round == "R":
            print(
                "Waaaaang waaaaaang!! You have set the laboratory on fire??!! Sir Mau is furious. You have been expelled from the CEAT and UPLB itself. Game over.")
        elif third_round == "G":
            print(
                "*sprinkle* *sprinkle* *sprinkle* You have found the treasure that is Maria Makiling's smol fairy that was playing in the water of Molawin Creek. The 'diwata' has enchanted your professor to give you the treasure that is the mighty UNO.You have won the game. Congratulations you lucky bastard!")
        else:
            "Oh no you get a 5.0! No treasure for you!"
    else:
        print("Stop going to the library! Game over!")

else:
    "Oh no, you have been stranded in a traffic near Raymundo Gate! GAME OVER :'>"


# This code was migrated from replit to GitHub