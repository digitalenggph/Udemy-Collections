from tkinter import *

# draw window
window = Tk()
window.title("Let's play Tic-Tac-Toe!")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)

# pass function to button
# when the button is clicked, the X or O should appear
def click_x(btn):
    btn['text'] = 'X'

button = Button(text='',
                command= lambda: click_x(button),
                height = 10,
                width = 10)
button.grid(column=0, row=0)

button1 = Button(text='',
                command=lambda: click_x(button1),
                height = 10,
                width = 10 )
button1.grid(column=1, row=0)


window.mainloop()