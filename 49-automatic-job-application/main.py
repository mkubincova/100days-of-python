from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "YOUR LOGIN EMAIL"
ACCOUNT_PASSWORD = "YOUR LOGIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by="class name", value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by="class name", value="artdeco-modal__confirm-dialog-btn")[0]
    discard_button.click()


# Open browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3738192249&f_AL=true&geoId=104508036&keywords=accountant&location=Czechia&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by="css selector", value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(2)
sing_in_button = driver.find_element(by="link text", value="Přihlásit se")
sing_in_button.click()

# Sign in
time.sleep(5)
email_input = driver.find_element(by="id", value="username")
email_input.send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element(by="id", value="password")
password_input.send_keys(ACCOUNT_PASSWORD)
sing_in_button = driver.find_element(by="css selector", value="button[type='submit']")
sing_in_button.click()

# Get Listings
time.sleep(10)
job_list = driver.find_elements(by="class name", value="jobs-search-results__list-item")

# Apply for Jobs
for job in job_list:
    print("Opening Listing")
    job.click()
    time.sleep(2)

    try:
        # Click Apply Button
        easy_apply_button = driver.find_element(by="css selector", value=".jobs-apply-button--top-card > button")
        easy_apply_button.click()

        # Insert Phone Number
        time.sleep(5)
        phone = driver.find_element(by="css selector", value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the next Button
        next_button = driver.find_element(by="css selector", value="[data-easy-apply-next-button]")
        next_button.click()

        # Check the review Button
        review_button = driver.find_elements(by="css selector", value=".artdeco-button__text")
        if review_button[-1].text != "Review":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            review_button[-1].click()

        # Check the submit Button
        submit_button = driver.find_elements(by="css selector", value=".artdeco-button__text")
        if submit_button[-1].text != "Submit application":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button[-1].click()

        time.sleep(2)

        # Click Close Button
        close_button = driver.find_element(by="class name", value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue


time.sleep(60)
driver.quit()


