from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

my_phone_num = os.getenv('MY_NUM')
twilio_phone_num = os.getenv('TWILIO_NUM')

MY_EMAIL = os.getenv('GMAIL_EMAIL')
MY_PASSWORD = os.getenv('GMAIL_PSW')


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            from_=twilio_phone_num,
            to=my_phone_num,
            body=message
        )

    def send_emails(self, message, emails):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
