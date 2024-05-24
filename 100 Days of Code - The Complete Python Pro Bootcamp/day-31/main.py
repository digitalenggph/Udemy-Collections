from tkinter import *

import pandas as pd
from random import choice

global random_word

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# --------------------------- DATA SETUP ------------------------------ #

data_source_file = "./data/french_words.csv"
data_df = pd.read_csv(data_source_file)
data_dict = data_df.to_dict(orient="records")


def refresh_card():
    global random_word
    random_word = choice(data_dict)
    # in case the data is not just French words
    lang_list = [language for language in random_word]
    key = lang_list[0]
    canvas.itemconfig(title_text, text=key)
    canvas.itemconfig(card_text, text=random_word[key])


# -------------------------- BUTTON SETUP ------------------------------ #

def known_word():
    refresh_card()


def unknown_word():
    refresh_card()


# ---------------------------- UI SETUP ------------------------------- #

# window config
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# canvas config
card_front_img = PhotoImage(file="./images/card_front.png")
canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)

# canvas text

title_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
card_text = canvas.create_text(400, 263, text="", fill='black', font=(FONT_NAME, 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# button config

unknown_button_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_button_img, command=unknown_word, borderwidth=0, highlightthickness=0)
unknown_button.grid(row=1, column=0)

known_button_img = PhotoImage(file="./images/right.png")
known_button = Button(image=known_button_img, command=known_word, borderwidth=0, highlightthickness=0)
known_button.grid(row=1, column=1)

refresh_card()

window.mainloop()
