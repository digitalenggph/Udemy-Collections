import pandas as pd
import turtle

# initiate csv data
data = pd.read_csv("50_states.csv")

# initiate screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# load image as shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# score turtle initialize
score = turtle.Turtle()
score.hideturtle()
score.penup()

# game variable initialize
game_is_on = True
point = 0
guessed_state = []

while game_is_on:
    # track point in scoreboard
    scoreboard = f"{point}/50 Guess the State"
    answer_state = screen.textinput(title=scoreboard, prompt="What's another state's name?")

    # convert input to titlecase
    answer_state_title = answer_state.title()

    # check if guess is in csv data
    # proceed with the rest of the code is if it is in

    if answer_state_title in data.values and answer_state_title not in guessed_state:
        guess_state = data[data.state == answer_state_title]

        # get a pair of coordinates for the state guessed
        coor_tuple = (float(guess_state.x.iloc[0]), float(guess_state.y.iloc[0]))

        # write the state name centered at coor_tuple
        score.goto(coor_tuple)
        score.write(answer_state_title,
                    align="center",
                    font=("Courier", 12, "normal")
                    )

        # earn point if the state is freshly guessed
        point += 1

        # add state to the guessed list, so it will not be counted later on if repeated
        guessed_state.append(answer_state_title)

        # game finished if all states are guessed

        if len(guessed_state) == 50:
            print("You win!")
            game_is_on = False

    # exit amd save csv
    if answer_state.lower() == 'exit':
        game_is_on = False
        print("You typed our secret word - exit!")
        not_guessed = []
        for state in data["state"]:
            if state not in guessed_state:
                not_guessed.append(state)

        # create a csv with no index and no header
        not_guessed_df = pd.DataFrame(not_guessed)
        not_guessed_df.to_csv("not_guessed_data.csv", index=False, header=False)
