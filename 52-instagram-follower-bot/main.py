import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()
USERNAME = os.getenv("INSTA_EMAIL")
PASSWORD = os.getenv("INSTA_PASSWORD")
SIMILAR_ACCOUNT = "cooking_tree"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.followers = []

    def dismiss_popup(self, by, value):
        WebDriverWait(self.driver, 200).until(
            EC.visibility_of_element_located((by, value))).click()

    def login(self):
        self.driver.get("https://www.instagram.com/")

        # cookies
        self.dismiss_popup("xpath", "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
        time.sleep(3)

        username_input = self.driver.find_element(by="name", value="username")
        password_input = self.driver.find_element(by="name", value="password")

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # dismiss "Save login credentials" and "Turn on notifications" screens
        self.dismiss_popup("css selector", "main section button")
        self.dismiss_popup("xpath", "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(5)

        # open dialog with followers
        show_followers = self.driver.find_element(by="css selector", value="[href*=followers]")
        show_followers.click()

        # scroll down to load more followers
        modal = WebDriverWait(self.driver, 200).until(
            EC.visibility_of_element_located(("class name", "_aano")))

        for i in range(5):
            # scroll the top of the modal element by the height of the modal
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        self.followers = modal.find_elements(by="css selector", value="div[style] > div[style] > div.x1dm5mii")

    def follow(self):
        for follower in self.followers:
            try:
                follower.find_element(by="css selector", value="button[type=button]").click()
            except ElementClickInterceptedException:
                self.dismiss_popup("xpath", "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]")

            time.sleep(2)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
