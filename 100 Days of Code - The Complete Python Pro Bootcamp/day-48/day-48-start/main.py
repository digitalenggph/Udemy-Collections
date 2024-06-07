import os

from selenium import webdriver
from selenium.webdriver.common.by import By

PRODUCT_URL = os.environ.get("ENV_PRODUCT_URL")
# ----------------------------------------------------- LESSON 1 ----------------------------------------------------- #
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PRODUCT_URL)

# closes single active tab
# driver.close()

# quit the entire browser
# driver.quit()

# ----------------------------------------------------- LESSON 2 ----------------------------------------------------- #
# Use link from day-47 exercise

# Selenium locator strategies: CLASS
price_php = driver.find_element(By.CLASS_NAME, "FirstPrice")
item_name = driver.find_element(By.CLASS_NAME, "Title-pdp-title")

print(f"{item_name.text} is now {price_php.text}")

# Selenium locator strategies: NAME
newsletter_subscribe_bar = driver.find_element(By.NAME, value="newsletter_subscribe[email_address]")
print(newsletter_subscribe_bar.tag_name)

# getAttribute
print(newsletter_subscribe_bar.get_attribute("name"))
print(newsletter_subscribe_bar.get_attribute("placeholder"))

# Selenium locator strategies: ID
newsletter_subscribe_button = driver.find_element(By.ID, value="newsletterSignUpFormSubmitButton")
print(newsletter_subscribe_button.size)

# Selenium locator strategies: CSS
developer_link = driver.find_element(By.CSS_SELECTOR, value=".Breadcrumbs-item a")
print(developer_link.text)

# Selenium locator strategies: XPath -> My favorite!!!!!!!
scholarship_link = driver.find_element(By.XPATH, value='//*[@id="classifieds_footer_more_info_en"]/p/a[3]')
print(scholarship_link .text)

#


driver.quit()

"""
REFERENCES:

https://selenium-python.readthedocs.io/
https://www.selenium.dev/documentation/webdriver/elements/locators/

"""
