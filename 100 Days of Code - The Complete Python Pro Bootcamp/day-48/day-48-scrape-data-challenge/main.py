from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

driver = webdriver.Chrome()
driver.get(URL)


events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

events_list = events.text.split("\n")
events_dict = {}

for i in range(len(events_list)):
    if i % 2 == 0:
        events_dict[int(i/2)] = {
            "time": events_list[i],
            "name": events_list[i+1]
        }

print(events_dict)





