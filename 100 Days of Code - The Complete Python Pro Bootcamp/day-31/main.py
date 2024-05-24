from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

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
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
card_text = canvas.create_text(400, 263, text="Word", fill='black', font=(FONT_NAME, 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# button config
unknown_button_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_button_img, borderwidth=0, highlightthickness=0)
unknown_button.grid(row=1, column=0)

known_button_img = PhotoImage(file="./images/right.png")
known_button = Button(image=known_button_img, borderwidth=0, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()
