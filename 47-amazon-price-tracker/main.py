from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
MY_EMAIL = os.getenv('GMAIL_EMAIL')
MY_PASSWORD = os.getenv('GMAIL_PSW')

target_price = 10


def send_email(price, name="The product", url=""):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon price alert!\n\n{name} is now available for {price}.\n{url}"
        )


# Scrape amazon
product_url = "https://www.amazon.com/gp/product/B08P3LYDBL/ref=ewc_pr_img_1?smid=A95X41C6DY4I2&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en,cs-CZ;q=0.9,cs;q=0.8"
}
response = requests.get(product_url, headers=headers)
website = response.text
soup = BeautifulSoup(website, "lxml")

# Extract product info
price_symbol = soup.find(name="span", class_="a-price-symbol").getText()
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_decimal = soup.find(name="span", class_="a-price-fraction").getText()
full_price_text = f"{price_symbol}{price_whole}{price_decimal}"
full_price_value = float(f"{price_whole}{price_decimal}")

product_name = soup.find(name="h1", id="title").getText().strip()

# Alert if price is below threshold
if full_price_value < target_price:
    send_email(full_price_text, product_name, product_url)



