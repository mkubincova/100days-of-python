from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_FORM_URL = "https://forms.gle/KdfBvikxrBi6CBUo7"
REAL_ESTATE_WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_RESULTS_URL = "https://docs.google.com/forms/d/14QQTnPcKyAchZt6JrkdGrIA2cnP3VJye6ICzm1EhA9E/edit#responses"
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_PASSWORD = os.getenv('GMAIL_PSW')


class DataEntryBot:
    def __init__(self):
        self.links = []
        self.prices = []
        self.addresses = []
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

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
        self.login_to_google()
        time.sleep(3)
        self.driver.get(GOOGLE_FORM_RESULTS_URL)
        time.sleep(3)

        view_in_sheets_button = self.driver.find_element(by="css selector",value="[data-action-id=freebird-view-spreadsheet]")
        view_in_sheets_button.click()

        create_button = self.driver.find_element(by="xpath",value="//*[@id='yDmH0d']/div[13]/div/div[2]/div[3]/div[2]")
        create_button.click()

    def login_to_google(self):
        self.driver.get("https://accounts.google.com/ServiceLogin?hl=en-GB")
        time.sleep(3)

        email = self.driver.find_element(by="css selector", value="input[type=email]")
        email.send_keys(GMAIL_EMAIL)
        email.send_keys(Keys.ENTER)

        password = self.driver.find_element(by="css selector", value="input[type=password]")
        password.send_keys(GMAIL_PASSWORD)
        password.send_keys(Keys.ENTER)

        submit_button = self.driver.find_element(by="xpath", value="//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[4]/div[1]/button")
        submit_button.click()


# Run programme
bot = DataEntryBot()
# bot.get_listings()
# bot.send_form_responses()

# TODO: finish login and sheet creation when account gets unblocked
# bot.generate_table()