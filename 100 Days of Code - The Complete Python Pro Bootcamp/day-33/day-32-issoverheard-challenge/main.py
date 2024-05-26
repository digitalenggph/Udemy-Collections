from datetime import datetime

import requests
import smtplib
import time
from haversine import haversine, Unit

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


# If the ISS is close to my current position
def is_close():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    iss_tuple = (iss_latitude, iss_longitude)
    my_tuple = (MY_LAT, MY_LONG)

    haversine_distance = haversine(iss_tuple, my_tuple, unit=Unit.DEGREES)
    return haversine_distance <= 5


# and it is currently dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    return sunrise <= time_now.hour <= sunset


def send_mail():
    if is_close() and is_night():
        # Then email me to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg="Subject: ISS Overhead\n\n"
                                    "Look up!")


# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    send_mail()
