import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
my_phone_num = os.getenv('MY_NUM')
twilio_phone_num = os.getenv('TWILIO_NUM')

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv('STOCK_API_KEY')
}

NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apikey": os.getenv('NEWS_API_KEY')
}


def get_stock_data():
    response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
    response.raise_for_status()
    data = response.json()
    return data


def get_news_data():
    response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    response.raise_for_status()
    data = response.json()
    return data


def calculate_price_difference(yesterday, day_before_yesterday):
    yesterday_closing_price = float(yesterday['4. close'])
    day_before_yesterday_closing_price = float(day_before_yesterday['4. close'])
    price_difference = yesterday_closing_price - day_before_yesterday_closing_price
    percentage = (price_difference / yesterday_closing_price) * 100
    return percentage


def send_sms(articles):
    for article in articles:
        sms_text = f"""
TSLA: {'🔺' if percentage_difference > 0 else '🔻'}{abs(percentage_difference)}%
Headline: {article['title']}
Brief: {article['description']}
"""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=twilio_phone_num,
            to=my_phone_num,
            body=sms_text
        )
        print(message.status)


stock_data = get_stock_data()
data_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
percentage_difference = round(calculate_price_difference(data_list[0], data_list[1]))


if abs(percentage_difference) >= 0:
    news_data = get_news_data()
    send_sms(news_data["articles"][:3])
