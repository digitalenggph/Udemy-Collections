import requests, time, os
import pandas as pd
from bs4 import BeautifulSoup

# get lotto website URL
url = os.getenv("URL")

# initialize session
session = requests.Session()
resp = session.get(url)
initial_soup = BeautifulSoup(resp.text, "html.parser")

# set filter date to desired range --> from the oldest data available to most recent
payload = {
    "__VIEWSTATE": initial_soup.find("input", {"id": "__VIEWSTATE"})["value"],
    "__VIEWSTATEGENERATOR": initial_soup.find("input", {"id": "__VIEWSTATEGENERATOR"})["value"],
    "__EVENTVALIDATION": initial_soup.find("input", {"id": "__EVENTVALIDATION"})["value"],

    # Start date
    "ctl00$ctl00$cphContainer$cpContent$ddlStartMonth": "January",  # Change month here
    "ctl00$ctl00$cphContainer$cpContent$ddlStartDate": "2",  # Change day here
    "ctl00$ctl00$cphContainer$cpContent$ddlStartYear": "2015",  # Change year here

    # End date
    "ctl00$ctl00$cphContainer$cpContent$ddlEndMonth": "August",
    "ctl00$ctl00$cphContainer$cpContent$ddlEndDay": "12",
    "ctl00$ctl00$cphContainer$cpContent$ddlEndYear": "2025",

    # Submit button
    "ctl00$ctl00$cphContainer$cpContent$btnSearch": "Search Lotto"
}

if __name__ == "__main__":
    # use updated url with filtered date range
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        # Proceed with parsing
        soup = BeautifulSoup(response.text, 'html.parser')
        header = [header.get_text() for header in soup.find_all('th')]
        body = [row.get_text().strip() for row in soup.find_all('td')]

        no_of_rows = int(len(body)/len(header))
        lotto_data = []
        for i in range(no_of_rows):
            element_shift = len(header)
            slice_start, slice_end = element_shift * i, element_shift * i + len(header)
            lotto_data.append(body[slice_start:slice_end])

        # see how long did the code took to finish (excluding saving)
        print(time.process_time())

        # save dataframe for data analysis
        lotto_data_df = pd.DataFrame(lotto_data, columns=header)
        lotto_data_df.to_csv("lotto_data.csv")

    else:
        print(f"POST request failed with status code: {response.status_code}")
        exit()