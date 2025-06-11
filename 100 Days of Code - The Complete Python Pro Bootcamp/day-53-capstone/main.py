from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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



address_list, price_list, link_list = [], [], []


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

    address_list.append(rent_address[n].text)
    price_list.append(price)
    link_list.append(rent_link[n].get_attribute('href'))

    print(f"The rent price is {price}.")
    print(f"The rent address is {rent_address[n].text}.")
    print(f"The rent link address is {rent_link[n].get_attribute('href')}.\n\n")


driver.close()

# Open new browser

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc--o1J3zmqvVNmgu9ZTHeGZ_vYc8T1v9BrUp_TCKAGZckwAQ/viewform')



for n in range(len(rent_list)):
    address_form = driver.find_element(By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/'
                                             'div/div[1]/div/div[1]/input')

    price_form = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/'
                                           'div/div[1]/div/div[1]/input')

    link_form = driver.find_element(By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                          'div/div[1]/div/div[1]/input')

    time.sleep(1)


    address_form.send_keys(address_list[n])
    price_form.send_keys(price_list[n])
    link_form.send_keys(link_list[n])

    time.sleep(0.5)
    submit_button = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    time.sleep(0.25)

    submit_again_link = driver.find_element(By.LINK_TEXT,
                                            value='Magsumite ng iba pang tugon')
    submit_again_link.click()
    time.sleep(1)





