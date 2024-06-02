import os, smtplib
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_sid = os.environ.get("ENV_TWILIO_SID")
        self.twilio_auth = os.environ.get("ENV_TWILIO_AUTH")
        self.twilio_num = os.environ.get("ENV_TWILIO_NUM")
        self.twilio_my_num = os.environ.get("ENV_TWILIO_MY_NUM")
        self.gmail_from = os.environ.get("ENV_GMAIL_TEST_FROM")
        self.gmail_auth = os.environ.get("ENV_GMAIL_TEST_AUTH")

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

    def send_email(self, firstname, lastname, email, city, origin, destination, departure_date, price):
        email_from = self.gmail_from
        email_to = email
        email_auth = self.gmail_auth
        sms_body = (f"Subject:Trip to {city} deals available! Yay :D\n\n\n"
                    f"Hey {firstname} {lastname}! \n\n"    
                    f"{origin} -> {destination} for only ${price}!\n"
                    f"Local departure date: {departure_date}\n\n"
                    f"Love,\n"
                    f"krloves <3"
                    )

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email_from, password=email_auth)
            connection.sendmail(from_addr=email_from,
                                to_addrs=email_to,
                                msg=sms_body)
