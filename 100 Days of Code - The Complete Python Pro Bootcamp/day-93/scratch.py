import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# environment variables
well_url = os.getenv("WELL_URL")

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# go to website
driver = webdriver.Chrome(options=chrome_options)
driver.get(well_url)


def get_table(driver_name):
    table = driver_name.find_element(By.XPATH, value='/html/body/div/b/table')
    header = [header.text.strip() for header in table.find_elements(By.XPATH, "thead/tr/th")]
    body = table.find_elements(By.XPATH, "tbody/tr")

    return header, body


def get_data(header, body):
    table_rows = []
    for row in body:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = {header[i]: cells[i].text.strip() for i in range(len(cells))}

        # add link to be clicked
        try:
            link = cells[0].find_element(By.TAG_NAME, "a").get_attribute("href")
        except NoSuchElementException:
            link = None  # fallback if there's no link

        row_data['link'] = link

        # excludes total row
        table_rows.append(row_data)

    if table_rows[-1][header[0]] == 'TOTAL':
        table_rows.pop()  # removes last row which shows Total
    return table_rows


# get province table
province_header, province_body = get_table(driver)

# get province list of dictionary
province_data = get_data(province_header, province_body)

municipalities_data = []
# get municipality table
for province in province_data:
    link_to_municipalities = province["link"]
    if link_to_municipalities:
        driver.execute_script(f"window.open('{link_to_municipalities}', 'new_window')")
        # Switch to the new tab (it's the last one)
        driver.switch_to.window(driver.window_handles[-1])

        # Optional: wait for page to load
        time.sleep(1)

        municipal_header, municipal_body = get_table(driver)
        municipal_data = get_data(municipal_header, municipal_body)
        for municipality in municipal_data:
            municipality['Province'] = province["Province"]

        municipalities_data.extend(municipal_data)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    if province['Province'] == 'Agusan Del Sur':
        print(municipalities_data)
        exit()









