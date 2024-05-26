from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR,
                                                     width=280,
                                                     text="Question here.", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=0, pady=50)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, command=self.false_answer)
        self.false_button.config(highlightthickness=0, bg=THEME_COLOR)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, command=self.true_answer)
        self.true_button.config(highlightthickness=0, bg=THEME_COLOR)

        self.false_button.grid(row=2, column=0)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz."
                     f"You're final score is: {self.quiz.score}/{self.quiz.question_number}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_answer(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)

    def true_answer(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
