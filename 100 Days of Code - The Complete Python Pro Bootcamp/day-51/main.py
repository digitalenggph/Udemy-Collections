import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# -------------------------------------------------FOR TESTING ONLY-------------------------------------------------- #
URL_TESTING = os.environ.get("ENV_URL_TESTING")
URL_SHARING = os.environ.get("ENV_URL_SHARING")

# --------------------------------------------------SELENIUM SETUP--------------------------------------------------- #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.forward()
driver.get(URL_TESTING)

# ------------------------------------------------GET INTERNET SPEED------------------------------------------------- #

# get Go Button
test_button = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
sleep(10.0)
test_button.click()
print('clicked')
sleep(30.00)

# get result
download_mbps = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                              '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

upload_mbps = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                            '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

# ------------------------------------IF DOES NOT MEET ISP PROMISE THEN COMPLAIN-------------------------------------- #

MIN_DOWNLOAD_MBPS = 30
MIN_UPLOAD_MBPS = 30
ISP_ACCOUNT = os.environ.get("ENV_ISP_ACCOUNT")


def complain():
    if float(download_mbps) < MIN_DOWNLOAD_MBPS and float(download_mbps) < MIN_DOWNLOAD_MBPS:
        return f"Hey {ISP_ACCOUNT}, your service sucks. Both my up and download speed is below minimum aaaarrggh!"

    elif float(download_mbps) < MIN_DOWNLOAD_MBPS:
        return f"Hey {ISP_ACCOUNT}, my download speed is below minimum speed!"

    elif float(download_mbps) < MIN_DOWNLOAD_MBPS:
        return f"Hey {ISP_ACCOUNT}, my upload speed is below minimum speed!"
    else:
        return f"Hey {ISP_ACCOUNT}, thanks for the very fast internet :'>"


# -------------------------------------------SEND IT TO TWITTER FOR CLOUT-------------------------------------------- #

URL_LOGIN = os.environ.get('ENV_URL_LOGIN')
U_NAME = os.environ.get('ENV_U_NAME')
PASS = os.environ.get('ENV_PASS')

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(URL_LOGIN)

sleep(2.0)


sleep(3.0)
user_input_box = driver.find_element(By.NAME, value='text')
user_input_box.send_keys(U_NAME, Keys.ENTER)

sleep(3.0)
# get pass input box
pass_input_box = driver.find_element(By.NAME, 'password')
pass_input_box.send_keys(PASS, Keys.ENTER)

sleep(5.0)
# get post box
post_box = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                         '3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                         '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                         '1]/div/div/div/div/div/div[2]/div/div/div/div')
post_box.send_keys(complain())
sleep(1.0)

# post button
post_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                            '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div['
                                            '2]/div/div/div/button/div/span/span')
post_button.click()

driver.quit()

# -----------------------------------------------------REFERENCES----------------------------------------------------- #


"""
# open new tab
https://paveltashev.medium.com/python-and-selenium-open-focus-and-close-a-new-tab-4cc606b73388
"""
