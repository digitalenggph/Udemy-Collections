import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from time import sleep

URL = os.environ.get("ENV_URL")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)

# -------------------------------------------------FOR TESTING ONLY-------------------------------------------------- #
# test to see if we have access to the site
test_title = driver.find_element(By.XPATH, value='//*[@id="post-280"]/div/div/div/div/div/div/div[2]/div/p[1]/span')
print(test_title.text)
# ------------------------------------------------------------------------------------------------------------------- #

# ---------------------------------------------GET INTERACTIVE ELEMENTS---------------------------------------------- #
# input
first_name_field = driver.find_element(By.ID, value='wpforms-252-field_1')
last_name_field = driver.find_element(By.ID, value='wpforms-252-field_1-last')
email_field = driver.find_element(By.ID, value='wpforms-252-field_2')

# upload
upload_resume_button = driver.find_element(By.XPATH, value='//*[@id="wpforms-252-field_5-container"]/div')
upload_cover_button = driver.find_element(By.XPATH, value='//*[@id="wpforms-252-field_6-container"]/div')

# explain
exp_fbapi_field = driver.find_element(By.ID, value='wpforms-252-field_7')
exp_dpl_field = driver.find_element(By.ID, value='wpforms-252-field_8')
exp_stat_field = driver.find_element(By.ID, value='wpforms-252-field_10')
exp_cloud_field = driver.find_element(By.ID, value='wpforms-252-field_11')
exp_slackapi_field = driver.find_element(By.ID, value='wpforms-252-field_14')

# hourly rate
my_rate = driver.find_element(By.ID, value='wpforms-252-field_13')

# submit
submit_button = driver.find_element(By.ID, value='wpforms-submit-252')

# -------------------------------------------INTERACT WITH THESE ELEMENTS-------------------------------------------- #

keyboard = Controller()

MY_FIRST_NAME = os.environ.get("ENV_FIRST_NAME")
MY_LAST_NAME = os.environ.get("ENV_LAST_NAME")
MY_EMAIL = os.environ.get("ENV_EMAIL")
MY_RATE = os.environ.get("ENV_HOURLY_RATE")

MY_CV = os.environ.get("ENV_CV_PATH")
MY_COVER = os.environ.get("ENV_COVER_PATH")
MY_EXPLANATION = os.environ.get("ENV_EXPLAIN_PATH")

OP_NAME = os.environ.get("ENV_OP_NAME")

# Type for input and explain fields
first_name_field.send_keys(MY_FIRST_NAME)
last_name_field.send_keys(MY_LAST_NAME)
email_field.send_keys(MY_EMAIL)

# upload
upload_resume_button.click()
sleep(1.0)                      # not to fast, make PC rest for a while
keyboard.type(MY_CV)            # sendkeys is not working, so I had to consult Dr. YouTube.
keyboard.press(Key.enter)       # after typing path, press & release enter
keyboard.release(Key.enter)
sleep(2.0)

upload_cover_button.click()
sleep(1.0)
keyboard.type(MY_COVER)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(5.0)

# explain stuff
explanation = pd.read_csv(MY_EXPLANATION, header=None)
explanation.columns = ['question', 'answer']

explanation_dict = {row.question: row.answer for index, row in explanation.iterrows()}

exp_fbapi_field.send_keys(explanation_dict['fbapi'])
exp_dpl_field.send_keys(explanation_dict['dpl'])
exp_stat_field.send_keys(explanation_dict['stat'])
exp_cloud_field.send_keys(explanation_dict['cloud'])
exp_slackapi_field.send_keys(explanation_dict['slackapi'])

# hourly rate
my_rate.send_keys(f"Hi {OP_NAME}, my rate would be {MY_RATE}.\n"
                  f"Please contact me if you would like to discuss:)")

# submit
submit_button.click()


# -----------------------------------------------------REFERENCES----------------------------------------------------- #

"""
https://www.youtube.com/watch?v=ZohudLX9FfY
"""

