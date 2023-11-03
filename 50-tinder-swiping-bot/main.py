# I'm not making a fake Tinder profile and waiting for matches to do this.
# Instead, these are notes with the new stuff:

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


# 01 - HANDLING POP-UP WINDOWS:

# get hold of driver windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# switch to pop-up (and fill out the form)
driver.switch_to.window(fb_login_window)
# switch back to site
driver.switch_to.window(base_window)


# 02 - HANDLING EXCEPTIONS (obscured and missing elements):

like_button = driver.find_element(
    by="xpath",
    value='//*[@id="c-1420294622"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')

try:
    # profile is loaded
    like_button.click()

except NoSuchElementException:
    # profile is not loaded yet
    time.sleep(3)
    like_button.click()

except ElementClickInterceptedException:
    # profile is blocked by "It's a match" screen
    try:
        # hide pop up (it's a match)
        driver.find_element(by="xpath", value='//*[@id="c-1089923421"]/div/div/div[1]/div/div[4]/button').click()
    except:
        # sometimes tinder shows (add to home screen pop up) so we need to click cancel
        driver.find_element(by="xpath", value='//*[@id="c1146291598"]/div/div/div[2]/button[2]/span').click()

    # wait for 2 seconds for any of the above two exceptions and then try to click like button
    time.sleep(3)
    like_button.click()

