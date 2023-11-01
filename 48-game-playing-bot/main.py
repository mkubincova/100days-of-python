from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by="id", value="cookie")


def buy_addons():
    available_addons = driver.find_elements(by="css selector", value="#store > div:not(.grayed) b")
    prices = [int(item.text.split()[-1].replace(",", "")) for item in available_addons]
    available_addons[prices.index(max(prices))].click()


timeout = time.time() + 5
end_time = time.time() + 60 * 5  # 5 minutes

while True:
    cookie.click()

    if time.time() > timeout:
        buy_addons()
        timeout = time.time() + 5

    if time.time() > end_time:
        cookie_per_s = driver.find_element(by="id", value="cps").text
        print(cookie_per_s)
        break

driver.quit()


