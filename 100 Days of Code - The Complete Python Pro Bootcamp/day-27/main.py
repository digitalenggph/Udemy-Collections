"""
DAY-27-NOTES:
Tkinter module for GUI (Graphical User Interface)
    - button clicks
    - input box

Advanced Functions
Default Arguments
    *  Args
    ** Kwargs
"""

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
# with packer otherwise it will not appear

# Method 1
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

# Method 2
my_label["text"] = "New Text"

# Method 3
my_label.config(text="New Text")

my_label.pack()


def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()


# Button

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()
input.get()

# so the window will stay open
window.mainloop()
