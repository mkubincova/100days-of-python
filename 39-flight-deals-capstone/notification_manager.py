from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
my_phone_num = os.getenv('MY_NUM')
twilio_phone_num = os.getenv('TWILIO_NUM')


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages.create(
            from_=twilio_phone_num,
            to=my_phone_num,
            body=message
        )
