from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # for non-alphanumeric keys like Enter

URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)

# get input bars
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# get Sign-Up button
sign_up = driver.find_element(By.XPATH, value="/html/body/form/button")

# the automation
first_name.send_keys("krloves", Keys.TAB)
last_name.send_keys("testing", Keys.TAB)
email.send_keys("sample@gmail.com", Keys.TAB)

sign_up.click()


