from tkinter import *  # classes only
from tkinter import messagebox  # modules of code
from password_generator import password_generator
import pyperclip
import json


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    website = website_textbox.get()
    if len(website) !=0:
        try:
            with open("data.json", mode='r') as data_file:
                # reads old data
                data = json.load(data_file)
                # retrieves data from json
                email = data[website]["email"]
                password = data[website]["password"]
        except FileNotFoundError:
            messagebox.showinfo(title="No file yet.",
                                message="No file yet.")
        except KeyError:
            messagebox.showinfo(title="Website not found",
                                message=f"No entries found for website {website}")
        else:
            messagebox.showinfo(
                title=website,
                message=f"Email: {email} \nPassword: {password}"
            )
    else:
        messagebox.showinfo(title="Empty website",
                            message="Input website in the entry box please.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_generator()
    password_textbox.delete(0, END)
    password_textbox.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_textbox.get()
    email_user = email_user_textbox.get()
    password = password_textbox.get()

    # data_string = f"{website} | {email_user} | {password}\n"
    new_data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if len(website) == 0 or \
            len(email_user) == 0 or \
            len(password) == 0:

        messagebox.showerror(
            title="Oops",
            message="Please don't leave any fields empty!"
        )

    else:
        try:
            with open("data.json", mode='r') as data_file:
                # reads old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                # creates new data
                # first input
                json.dump(new_data, data_file, indent=4)
        else:
            # updates old data with new data
            data.update(new_data)

            with open("data.json", mode='w') as data_file:
                # saves updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_textbox.delete(0, END)
            password_textbox.delete(0, END)
            print(data)


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

website_textbox = Entry(width=21)
website_textbox.focus()
website_textbox.grid(column=1, row=1, columnspan=1, sticky="EW")

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

# generate buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=search_website)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
