import smtplib
import datetime as dt
import random
import calendar

# ---------------------------- GET TIME NOW ------------------------------- #

day_list = ["Monday", ""]
now = dt.datetime.now()
day_of_week = now.strftime("%A")

# ---------------------------- LOAD-READ-FILE ------------------------------- #

with open("quotes.txt", mode='r') as quotes:
    quotes_list = [quote.strip() for quote in quotes.readlines()]

random_quote = random.choice(quotes_list)

# ---------------------------- SEND EMAIL ------------------------------- #

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg=f"Subject: Quote for {day_of_week}\n\n"
                            f"{random_quote}")
