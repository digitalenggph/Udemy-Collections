from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     # for non-alphanumeric keys like Enter

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)

# Hone in on anchor tag using XPATH
article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count.click()
print(article_count.text)

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value='search')

# Type Python in send key
search.send_keys("Python", Keys.ENTER)