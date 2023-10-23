import datetime as dt
import os
import pandas
import random
import smtplib
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('GMAIL_EMAIL')
password = os.getenv('GMAIL_PSW')


def send_birthday_wish(recipient_email, recipient_name):
    random_file = random.choice(os.listdir("letter_templates"))

    with open(f'letter_templates/{random_file}') as file:
        template = file.read()
        message = template.replace('[NAME]', recipient_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday\n\n{message}"
        )


now = dt.datetime.now()

try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError as error:
    print(error)
else:
    for index, row in data.iterrows():
        if row['day'] == now.day and row['month'] == now.month:
            send_birthday_wish(row['email'], row['name'])
