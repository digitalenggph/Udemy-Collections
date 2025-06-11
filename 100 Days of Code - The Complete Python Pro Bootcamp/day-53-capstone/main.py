from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://appbrewery.github.io/Zillow-Clone/')

# Locator strategies
rent_list = driver.find_elements(By.CSS_SELECTOR,
                                 value='.List-c11n-8-84-3-photo-cards '
                                       '.StyledPropertyCardDataWrapper')


rent_address = driver.find_elements(By.CSS_SELECTOR,
                                  value='.List-c11n-8-84-3-photo-cards '
                                        '.StyledPropertyCardDataWrapper '
                                        '.StyledPropertyCardDataArea-anchor')


rent_price = driver.find_elements(By.CSS_SELECTOR,
                                  value='.List-c11n-8-84-3-photo-cards '
                                        '.StyledPropertyCardDataWrapper '
                                        '.PropertyCardWrapper '
                                        '.PropertyCardWrapper__StyledPriceLine')


rent_link = driver.find_elements(By.CSS_SELECTOR,
                                  value='.List-c11n-8-84-3-photo-cards '
                                        '.StyledPropertyCardPhotoWrapper a')



for n in range(len(rent_list)):
    price = rent_price[n].text

    if '+' in price:
        price = price.split('+')[0]
    elif '/' in price:
        price = price.split('/')[0]
    elif ' ' in price:
        price = price.split(' ')[0]
    else:
        price = price


    print(f"The rent price is {price}.")
    print(f"The rent address is {rent_address[n].text}.")
    print(f"The rent link address is {rent_link[n].get_attribute('href')}.\n\n")

# driver.close()
driver.quit()

# Address, Price , Link