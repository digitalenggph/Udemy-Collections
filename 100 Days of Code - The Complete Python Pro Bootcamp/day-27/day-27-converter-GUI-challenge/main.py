from tkinter import *


def calculate():
    input_float = float(textbox.get())
    result_label["text"] = input_float * 1.609344


# For window config
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=100, pady=50)

# For textbox
textbox = Entry(width=10)
textbox.focus()
textbox.insert(END, "0")
textbox.grid(column=1, row=0)

# For Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# For is equal to label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# For result label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# For Km label
km_label = Label(text="km")
km_label.grid(column=2, row=1)

# For Calculate button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
