import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_sid = os.environ.get("ENV_TWILIO_SID")
        self.twilio_auth = os.environ.get("ENV_TWILIO_AUTH")
        self.twilio_num = os.environ.get("ENV_TWILIO_NUM")
        self.twilio_my_num = os.environ.get("ENV_TWILIO_MY_NUM")

    def send_notif(self, city, origin, destination, departure_date, price):
        sms_body = {
            f"Trip to {city} deals available! Yay :D\n"
            f"{origin} -> {destination} for only {price}!\n"
            f"Local departure date: {departure_date}"
        }

        client = Client(self.twilio_sid, self.twilio_auth)
        messages = client.messages.create(
            from_=f"whatsapp:{self.twilio_num}",
            to=f"whatsapp:{self.twilio_my_num}",
            body=sms_body
        )
        print(messages.status)


