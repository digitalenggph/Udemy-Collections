from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import random, smtplib
import pandas as pd
import datetime as dt

global updated_df, name_entry, email_entry, month_combobox, day_combobox, year_combobox

BACKGROUND_COLOR = "#02BAC3"
FONT_NAME = "Arial"
MONTH_LIST = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
YEAR_LIST = [str(year) for year in range(1900, dt.datetime.now().year + 1)]
YEAR_LIST.reverse()
DAY_LIST = [str(day) for day in range(1, 31)]
LETTER_LIST = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

# -------------------------- CURRENT DATE ------------------------------ #

date_now = dt.datetime.now()
year_now = date_now.year
month_now = int(date_now.strftime("%m"))
day_now = int(date_now.strftime("%d"))


# --------------------Extra Hard Starting Project------------------- #

# TODO 1. Update the birthdays.csv

# -------------------------- UI SETUP ------------------------------ #

def new_birthday_UI():
    global name_entry, email_entry, month_combobox, day_combobox, year_combobox

    window = Tk()
    window.title("Happy Birthday!")
    window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

    balloon_img = PhotoImage(file="images/balloon.png")
    canvas = Canvas(height=500, width=500)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.create_image(250, 250, image=balloon_img)
    canvas.create_text(250, 25,
                       text="Happy",
                       fill="white",
                       font=("Segoe UI", 50, "bold", "italic"))
    canvas.create_text(250, 450,
                       text="Birthday!",
                       fill="white",
                       font=("Segoe UI", 50, "bold", "italic"))
    canvas.grid(row=0, column=0, columnspan=4)

    # label
    name_label = Label(text="Name:",
                       font=(FONT_NAME, 20, "bold"),
                       bg=BACKGROUND_COLOR,
                       fg="white")
    email_label = Label(text="E-mail:",
                        font=(FONT_NAME, 20, "bold"),
                        bg=BACKGROUND_COLOR,
                        fg="white")
    birthday_label = Label(text="Birthday:",
                           font=(FONT_NAME, 20, "bold"),
                           bg=BACKGROUND_COLOR,
                           fg="white")

    name_label.grid(row=1, column=0, sticky="W")
    email_label.grid(row=2, column=0, sticky="W")
    birthday_label.grid(row=3, column=0, sticky="W")

    # entry boxes
    name_entry = Entry(width=30, font=(FONT_NAME, 20, "bold"), fg=BACKGROUND_COLOR)
    email_entry = Entry(width=30, font=(FONT_NAME, 20, "bold"), fg=BACKGROUND_COLOR)
    name_entry.grid(row=1, column=1, columnspan=3, sticky="EW")
    email_entry.grid(row=2, column=1, columnspan=3, sticky="EW")

    # combo boxes
    month_combobox = ttk.Combobox(state="readonly", values=MONTH_LIST)
    year_combobox = ttk.Combobox(state="readonly", values=YEAR_LIST)
    day_combobox = ttk.Combobox(state="readonly", values=DAY_LIST)

    # combobox default values upon opening
    month_combobox.current(month_now - 1)
    year_combobox.current(0)
    day_combobox.current(day_now - 1)

    # combobox config
    month_combobox.config(width=15, font=(FONT_NAME, 20, "bold"), foreground=BACKGROUND_COLOR)
    year_combobox.config(width=5, font=(FONT_NAME, 20, "bold"), foreground=BACKGROUND_COLOR)
    day_combobox.config(width=5, font=(FONT_NAME, 20, "bold"), foreground=BACKGROUND_COLOR)

    month_combobox.grid(row=3, column=1, sticky="W")
    year_combobox.grid(row=3, column=3, sticky="E")
    day_combobox.grid(row=3, column=2, sticky="EW")

    # button config
    get_data_img = PhotoImage(file="./images/save_the_date_resized.png")
    get_data_button = Button(image=get_data_img,
                             command=get_birthday_data)
    get_data_button.config(fg=BACKGROUND_COLOR, bg=BACKGROUND_COLOR,
                           highlightthickness=0, borderwidth=0,
                           highlightcolor=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR,
                           relief='flat')

    check_bday_img = PhotoImage(file="./images/send_bday_greetings_resized.png")
    check_bday_button = Button(image=check_bday_img,
                               command=check_birthday)
    check_bday_button.config(fg=BACKGROUND_COLOR, bg=BACKGROUND_COLOR,
                             highlightthickness=0, borderwidth=0,
                             highlightcolor=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR,
                             relief='flat')

    get_data_button.grid(row=4, column=1, columnspan=3, sticky="EW")
    check_bday_button.grid(row=5, column=1, columnspan=3, sticky="EW")

    window.mainloop()


def ask_user_birthday():
    global updated_df
    try:
        birthday_df = pd.read_csv("data/birthdays.csv")
    except FileNotFoundError:
        messagebox.showinfo(title="File created.",
                            message="There was no data source for the birthdays."
                                    "The program created one for you :'>")
        # adding header
        df = pd.DataFrame()
        headerlist = ['name', 'email', 'year', 'month', 'day']

        # converting data frame to csv
        df.to_csv("data/birthdays.csv", header=headerlist, index=False)
        birthday_df = pd.read_csv("data/birthdays.csv")

    finally:
        updated_df = birthday_df


# TODO 2. Check if today matches a birthday in the birthdays.csv
# TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
def check_birthday():
    filtered_df = updated_df.loc[(updated_df["year"] == year_now) &
                                 (updated_df["month"] == month_now) &
                                 (updated_df["day"] == day_now)]

    if len(filtered_df) > 0:
        for index, row in filtered_df.iterrows():
            letter_file = random.choice(LETTER_LIST)
            with open(letter_file, mode='r') as letter:
                template = letter.read()
                new_letter = template.replace("[NAME]", row['name'].title())
                print(new_letter)
        # TODO 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row.email,
                                msg=f"Subject:Birthday greetings for you, {row['name'].title()} <3 \n\n"
                                    f"{new_letter}")


def get_birthday_data():
    global updated_df
    ask_user_birthday()

    birthday_celebrant_name = name_entry.get()
    birthday_celebrant_email = email_entry.get()
    birthday_month = MONTH_LIST.index(month_combobox.get()) + 1
    birthday_day = int(day_combobox.get())
    birthday_year = int(year_combobox.get())

    to_add_df = {
        'name': birthday_celebrant_name,
        'email': birthday_celebrant_email,
        'year': birthday_year,
        'month': birthday_month,
        'day': birthday_day
    }

    updated_df = pd.concat([updated_df, pd.DataFrame(to_add_df, index=[0])], ignore_index=True)
    print(updated_df)
    updated_df.to_csv("./data/birthdays.csv", index=False)


new_birthday_UI()
