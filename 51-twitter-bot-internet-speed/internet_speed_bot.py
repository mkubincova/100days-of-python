from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        cookies_button = self.driver.find_element(by="id", value="onetrust-accept-btn-handler")
        cookies_button.click()

        start_button = self.driver.find_element(by="css selector", value=".start-button a")
        start_button.click()

        # wait till testing is finished
        WebDriverWait(self.driver, 200).until(
            EC.visibility_of_element_located(("class name", "mobile-test-complete")))

        self.down = float(self.driver.find_element(by="class name", value="download-speed").text)
        self.up = float(self.driver.find_element(by="class name", value="upload-speed").text)

    def tweet_at_provider(self, expected_down, expected_up):
        self.login_to_twitter()

        tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
                 f"when I pay for {expected_down}down/{expected_up}up?")
        tweet_input = WebDriverWait(self.driver, 200).until(
            EC.visibility_of_element_located(("xpath", "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))
        tweet_input.send_keys(tweet)

        post_button = self.driver.find_element(by="css selector", value="[data-testid='tweetButtonInline']")
        post_button.click()

        time.sleep(2)
        self.driver.quit()

    def login_to_twitter(self):
        self.driver.get("https://twitter.com/login")

        email_input = WebDriverWait(self.driver, 200).until(
            EC.visibility_of_element_located(("name", "text")))
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)

        # Resolve safety measures after many consecutive logins
        username_input = WebDriverWait(self.driver, 200).until(
            EC.visibility_of_element_located(("name", "text")))
        if username_input.is_enabled():
            username_input.send_keys(TWITTER_USERNAME)
            username_input.send_keys(Keys.ENTER)

        password_input = WebDriverWait(self.driver, 200).until(
            EC.visibility_of_element_located(("name", "password")))
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)


