import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

API_KEY = os.getenv('API_KEY')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
my_phone_num = os.getenv('MY_NUM')
twilio_phone_num = os.getenv('TWILIO_NUM')

MY_LAT = 45.95
MY_LONG = 12.633333
OWM_URL = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(OWM_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()

twelve_hour_data = weather_data["hourly"][:12]

will_rain = False
for hour in twelve_hour_data:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True
        break


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=twilio_phone_num,
        to=my_phone_num,
        body="It's going to rain today. Take an ☔"
    )
    print(message.status)
