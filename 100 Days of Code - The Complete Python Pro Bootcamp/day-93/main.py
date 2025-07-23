import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, random, json

# for measuring runtime
start_time = time.time()

# environment variables
well_url = os.getenv("WELL_URL")

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# go to website
driver = webdriver.Chrome(options=chrome_options)
driver.get(well_url)

def get_table(driver_name):
    try:
        table = driver_name.find_element(By.XPATH, value='/html/body/div/b/table')     # for province/municipalities
    except NoSuchElementException:
        table = driver_name.find_element(By.XPATH, value='/html/body/div/table')       # for well records

    header = [header.text.strip() for header in table.find_elements(By.XPATH, "thead/tr/th")]
    body = table.find_elements(By.XPATH, "tbody/tr")
    random_sleep()
    return header, body

def get_data(header, body):
    table_rows = []
    if body:
        for row in body:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = {header[i]: cells[i].text.strip() for i in range(len(cells))}

            if 'Google Map' in header:
                try:
                    row_data['Google Map'] = cells[header.index('Google Map')].find_element(By.TAG_NAME, "a")\
                                                                          .get_attribute('href')
                except NoSuchElementException:
                    row_data['Google Map'] = None


            # add link to be clicked
            try:
                link = cells[0].find_element(By.TAG_NAME, "a").get_attribute("href")
            except NoSuchElementException:
                link = None  # fallback if there's no link

            row_data['link'] = link

            # excludes total row
            table_rows.append(row_data)

        if table_rows and table_rows[-1][header[0]] == 'TOTAL':
            table_rows.pop() # removes last row which shows Total

    return table_rows

def click_link(driver_name, link):
    driver_name.execute_script(f"window.open('{link}', 'new_window')")
    driver_name.switch_to.window(driver_name.window_handles[-1])
    random_sleep()

def close_tab(driver_name):
    driver_name.close()
    driver_name.switch_to.window(driver_name.window_handles[0])
    random_sleep()


# to simulate slight human interaction (non-uniform clicks)
def random_sleep():
    sleep_duration = random.uniform(0.1, 0.5)
    time.sleep(sleep_duration)



# ---------------------- GET PROVINCE DATA (LIST OF DICTIONARY) ---------------------- #
province_header, province_body = get_table(driver)
province_data = get_data(province_header, province_body) # <-- Data


# -------------------- GET MUNICIPALITY DATA (LIST OF DICTIONARY) -------------------- #
municipalities_data = []

for province in province_data:
    link_to_municipality = province["link"]
    if link_to_municipality:
        click_link(driver, link_to_municipality)

        municipal_header, municipal_body = get_table(driver)
        municipal_data = get_data(municipal_header, municipal_body)
        for municipality in municipal_data:
            municipality['Province'] = province["Province"]

        municipalities_data.extend(municipal_data) # <-- Data
        close_tab(driver)


# -------------------- GET RECORDS DATA (LIST OF DICTIONARY) -------------------- #

well_records = []

for municipality in municipalities_data:
    link_to_records = municipality["link"]
    if link_to_records:
        click_link(driver, link_to_records)

        # get indices
        indices = driver.find_elements(By.XPATH, '/html/body/p/a')
        indices_link_list = [index.get_attribute("href") for index in indices if index.text != 'Google Map']

        # loop in all indices
        for index in indices_link_list:
            click_link(driver, index)
            records_header, records_body = get_table(driver)
            records_data = get_data(records_header, records_body)
            for records in records_data:
                records['Province'] = municipality["Province"]
                records['Municipality'] = municipality["Municipality"]

            well_records.extend(records_data) # <-- Data
            close_tab(driver)


# with open('records.txt', "w") as file:
#     file.write(f"{well_records}")

with open('records.json', 'w') as file:
    json.dump(well_records, file, indent=4)

print("--- %s seconds ---" % (time.time() - start_time))