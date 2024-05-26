from tkinter import *
from tkinter import messagebox

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR,
                                                     text="Question here.", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=0, pady=50)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img)
        self.false_button.config(highlightthickness=0, bg=THEME_COLOR)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img)
        self.true_button.config(highlightthickness=0, bg=THEME_COLOR)

        self.false_button.grid(row=2, column=0)
        self.true_button.grid(row=2, column=1)

        self.window.mainloop()

