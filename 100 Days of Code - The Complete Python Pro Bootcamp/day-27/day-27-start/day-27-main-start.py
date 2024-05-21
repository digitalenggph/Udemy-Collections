"""
DAY-27-NOTES:
Tkinter module for GUI (Graphical User Interface)
    - button clicks
    - input box

Advanced Functions
Default Arguments
    *  Args
    ** Kwargs

Tkinter Layout Managers
    * Pack  - packs widgets next to each other
            - top middle edge start
    * Place - precise positioning
            - with x & y values
            - (0, 0) top left corner
            - super specific
    * Grid  - relative to other components

    Warning:
        * pack & grid cannot be used at the same program
"""

from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # add padding

# Label
# with packer otherwise it will not appear

# Method 1
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

# Method 2
# my_label["text"] = "New Text"


# Method 3
my_label.config(text="New Text")

# Label placement
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button

button = Button(text="Click Me", command=button_clicked)
new_button = Button(text="New Button"
                    )
# Button placement
# button.pack()
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.get()

# Entry placement
# input.pack()
input.grid(column=3, row=2)

# so the window will stay open
window.mainloop()
