import random
import smtplib
import datetime as dt
import pandas
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('GMAIL_EMAIL')
password = os.getenv('GMAIL_PSW')


def send_birthday_wish(recipient):
    random_file = random.choice(os.listdir("letter_templates"))

    with open(f'letter_templates/{random_file}') as file:
        template = file.read()
        message = template.replace('[NAME]', recipient['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient['email'],
            msg=f"Subject:Happy Birthday\n\n{message}"
        )


today = (dt.datetime.now().month, dt.datetime.now().day)

try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError as error:
    print(error)
else:
    birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
    if today in birthday_dict:
        send_birthday_wish(birthday_dict[today])
