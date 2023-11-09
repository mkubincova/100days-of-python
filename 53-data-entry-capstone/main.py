from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import time
import os
from dotenv import load_dotenv
from seleniumbase import SB


load_dotenv()
GOOGLE_FORM_URL = "https://forms.gle/V4Dn9Hzovd2Hczur6"
REAL_ESTATE_WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_RESULTS_URL = "https://docs.google.com/forms/d/1KyxwXbaj8HEDqon5xg4DAnI1us4CbZ9Xdr7eQR0PoRo/edit#responses"
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_PASSWORD = os.getenv('GMAIL_PSW')


class DataEntryBot:
    def __init__(self):
        self.links = []
        self.prices = []
        self.addresses = []
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_listings(self):
        response = requests.get(REAL_ESTATE_WEBSITE_URL)
        website = response.text
        soup = BeautifulSoup(website, 'html.parser')
        listings = soup.find_all(attrs={"data-test": "property-card"})

        for listing in listings:
            link = listing.find(attrs={"data-test": "property-card-link"})["href"]
            price = listing.find(attrs={"data-test": "property-card-price"}).text
            price_clean = re.sub('[a-z/+]', '', price.split()[0])
            address = listing.find(attrs={"data-test": "property-card-addr"}).text.strip()

            self.links.append(link)
            self.prices.append(price_clean)
            self.addresses.append(address)

    def send_form_responses(self):
        for i in range(len(self.links)):
            self.driver.get(GOOGLE_FORM_URL)
            time.sleep(3)

            inputs = self.driver.find_elements(by="css selector", value="input[type='text']")
            submit_button = self.driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

            inputs[0].send_keys(self.addresses[i])
            inputs[1].send_keys(self.prices[i])
            inputs[2].send_keys(self.links[i])
            submit_button.click()

    def generate_table(self):
        # Bypass Google security issues with SeleniumBase
        with SB(uc=True, headed=True) as sb:
            # Login to google
            sb.open("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?response_type=code&redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&access_type=offline&client_id=407408718192.apps.googleusercontent.com&scope=email&flowName=GeneralOAuthFlow")
            sb.type("input[type=email]", f"{GMAIL_EMAIL}\n")
            sb.type("input[type=password]", f"{GMAIL_PASSWORD}\n")
            time.sleep(3)

            # Edit form
            sb.open(GOOGLE_FORM_RESULTS_URL)
            sb.click("[data-action-id=freebird-view-spreadsheet]")
            time.sleep(3)
            sb.execute_script('document.querySelector(\'[data-id="myVLbc"]\').click();')
            time.sleep(5)


# Run programme
bot = DataEntryBot()
# bot.get_listings()
# bot.send_form_responses()
# bot.generate_table()
