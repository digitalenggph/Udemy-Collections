from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)

cookie = driver.find_element(By.ID, value="cookie")

# initial count
cursor_count, grandma_count, factory_count, mine_count, shipment_count = 0, 0, 0, 0, 0

# alchemy_lab_count, portal_count, time_machine_count = 0, 0, 0
# commented out as the running time is 5 mins and it's not enough to get here

timeout = time() + 5
end = time() + 60 * 5
time_sleep = 0.01

while time() < end:

    if time() > timeout:
        cursor = driver.find_element(By.ID, value="buyCursor")
        grandma = driver.find_element(By.ID, value="buyGrandma")
        factory = driver.find_element(By.ID, value="buyFactory")
        mine = driver.find_element(By.ID, value="buyMine")
        shipment = driver.find_element(By.ID, value="buyShipment")

        if shipment.get_attribute("class") != 'grayed':
            shipment.click()
            shipment_count += 1
            sleep(time_sleep)
        elif mine.get_attribute("class") != 'grayed':
            mine.click()
            mine_count += 1
            sleep(time_sleep)
        elif factory.get_attribute("class") != 'grayed':
            factory.click()
            factory_count += 1
            sleep(time_sleep)
        elif grandma.get_attribute("class") != 'grayed':
            grandma.click()
            grandma_count += 1
            sleep(time_sleep)
        elif cursor.get_attribute("class") != 'grayed':
            cursor.click()
            cursor_count += 1
            sleep(time_sleep)

        timeout = time() + 5

    else:
        cookie.click()

cookies_per_second = driver.find_element(By.ID, value="cps")
print(cookies_per_second.text)
"""
If the running time is longer, this blcok can be included at the first part of the 
including this, cookies produced/second = 37.2

alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
portal = driver.find_element(By.ID, value="buyPortal")
time_machine = driver.find_element(By.ID, value="buyTime machine")

if time_machine.get_attribute("class") != 'grayed' and time_machine_count < 1:
    time_machine.click()
    time_machine_count += 1
    sleep(time_sleep)
elif portal.get_attribute("class") != 'grayed' and portal_count < 2:
    portal.click()
    portal_count += 1
    sleep(time_sleep)
elif alchemy_lab.get_attribute("class") != 'grayed' and alchemy_lab_count < 2:
    alchemy_lab.click()
    alchemy_lab_count += 1
    sleep(time_sleep)
"""
