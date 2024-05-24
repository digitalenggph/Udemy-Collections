from tkinter import *

import pandas as pd
from random import choice

global card_front_img, card_back_img, random_word, timer

CARD_FRONT_IMG = "./images/card_front.png"
CARD_BACK_IMG = "./images/card_back.png"
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# --------------------------- DATA SETUP ------------------------------ #

data_source_file = "./data/french_words.csv"
data_df = pd.read_csv(data_source_file)
data_dict = data_df.to_dict(orient="records")


def refresh_card():
    global card_front_img, random_word, timer
    window.after_cancel(timer)

    random_word = choice(data_dict)

    # in case the data is not just French words
    lang_list = [language for language in random_word]
    key = lang_list[0]

    card_front_img = PhotoImage(file=CARD_FRONT_IMG)
    canvas.itemconfig(canvas_img, image=card_front_img)

    canvas.itemconfig(title_text, text=key, fill="black")
    canvas.itemconfig(card_text, text=random_word[key], fill="black")

    timer = window.after(3000, flip_card)


def flip_card():
    global card_back_img, random_word, timer

    # in case the data is not just French words
    lang_list = [language for language in random_word]
    key_translated = lang_list[1]

    card_back_img = PhotoImage(file=CARD_BACK_IMG)
    canvas.itemconfig(canvas_img, image=card_back_img)

    canvas.itemconfig(title_text, text=key_translated, fill="white")
    canvas.itemconfig(card_text, text=random_word[key_translated], fill="white")


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
timer = window.after(3000, flip_card)

# canvas config
canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image="")

# canvas text
title_text = canvas.create_text(400, 150, text="", fill="", font=(FONT_NAME, 40, "italic"))
card_text = canvas.create_text(400, 263, text="", fill="", font=(FONT_NAME, 50, "bold"))
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

"""
REFERENCE:
https://stackoverflow.com/questions/73941559/tkinter-canvas-fails-to-update-image

"""
