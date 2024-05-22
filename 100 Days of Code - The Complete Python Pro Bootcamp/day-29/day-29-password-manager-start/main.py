from tkinter import *  # classes only
from tkinter import messagebox  # modules of code
from password_generator import password_generator
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_generator()
    password_textbox.delete(0, END)
    password_textbox.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # concatenate data strings
    data = f"{website_textbox.get()} | {email_user_textbox.get()} | {password_textbox.get()}\n"

    if len(website_textbox.get()) == 0 or \
            len(email_user_textbox.get()) == 0 or \
            len(password_textbox.get()) == 0:

        messagebox.showerror(
            title="Oops",
            message="Please don't leave any fields empty!"
        )

    else:
        # messagebox
        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(
            title=website_textbox.get(),
            message=f"These are the details entered: \
                    \nEmail: {email_user_textbox.get()} \
                    \nPassword: {password_textbox.get()} \
                    \nIs it OK to save?"
        )

        if is_ok:
            # append string to data.txt file
            # with open to automatically open then close the file
            with open("data.txt", mode='a') as file:
                file.write(data)

            # reset all textboxes
            website_textbox.delete(0, END)
            password_textbox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# window config
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas config
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

# label | entry | button config

# website
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_textbox = Entry(width=35)
website_textbox.focus()
website_textbox.grid(column=1, row=1, columnspan=2, sticky="EW")

# email/username
email_user_label = Label(text="Email/Username: ")
email_user_label.grid(column=0, row=2)

email_user_textbox = Entry(width=35)
# insert 0-> start, END-> end
email_user_textbox.insert(END, "cinderella.tinkerbell@snowwhite.com")
email_user_textbox.grid(column=1, row=2, columnspan=2, sticky="EW")

# password
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3, sticky="EW")

# generate password button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
