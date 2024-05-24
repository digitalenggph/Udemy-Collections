import smtplib

"""
VANILLA CODE
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()  # TLS - Transport Layer Security
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs=to_email,
                    msg="Subject:Hello \n\n"
                        "This is the body of my email.")
connection.close()

"""

"""
# Better code
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # TLS - Transport Layer Security
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg="Subject:Hello again \n\n"
                            "This is the body of my email.")

"""

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

# create datetime object
date_of_birth = dt.datetime(year=1800, month=12, day=31, hour=4)
print(date_of_birth)





# To generate app password
# https://accounts.google.com/v3/signin/challenge/pwd?TL=ALv_Gf9B-jaKH1Z3ecm5_giDra1XImwTCE2dVp4WmzHHtkreHvwHcTiQaj9wBJ1A&cid=2&continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&ifkv=AaSxoQywhCn-N--se6q6TgnAvNlla4zfL5ZZRZ4oheoryUEwB7lCml_C4uDdpgxqeCKl9cYJKDbX&osid=1&rart=ANgoxcfpRHN7yBIHhkY_z3n88mZJd--4vHssHwauXfy7wLMtZwBFNafjhek8dVzytBaBO88CACtM-YR0AMYOlpI_l67-hMoYqNdCP-LUFfHdBoJ0Rfn8FkU&rpbg=1&service=accountsettings
