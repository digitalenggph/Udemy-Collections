from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    # call global variables
    global timer
    global reps

    # stop timer
    window.after_cancel(timer)

    # set timer_text to 00:00
    canvas.itemconfig(timer_text, text="00:00")

    # timer name to timer in place of work or break
    timer_label.config(text='TIMER', fg=GREEN)

    reps = 0
    check_marks["text"] = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = int(count // 60)
    seconds = int(count % 60)

    # dynamic typing
    if seconds < 10:
        seconds = f"0{seconds}"

    """
    # vanilla if-then
    if len(str(count % 60)) < 2:
        seconds = '0' + str(count % 60)
    else:
        seconds = count % 60
    """
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        global reps
        if reps % 2 == 0:
            check_marks["text"] = "✔" * int(reps / 2)


# ---------------------------- UI SETUP ------------------------------- #
# window config
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas config
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # values in pixels
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # center x, y
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# check label
check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

# start and reset buttons
start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 12), highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 12), highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
