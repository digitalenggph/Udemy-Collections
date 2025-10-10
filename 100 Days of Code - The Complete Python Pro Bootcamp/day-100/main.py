import requests, time, os
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime as dt

# get lotto website URL
url = os.getenv("URL")

# initialize session
session = requests.Session()
resp = session.get(url)
initial_soup = BeautifulSoup(resp.text, "html.parser")

# get most recent draw date
latest_date = [row.get_text().strip() for row in initial_soup.find_all('td')][2]
latest_date_dt = dt.strptime(latest_date, "%m/%d/%Y").date()

hidden_details = {i["name"]: i.get("value", "") for i in initial_soup.find_all("input", type="hidden")}

payload = {
    **hidden_details,

    # Start date
    "ctl00$ctl00$cphContainer$cpContent$ddlStartMonth": "January",  # Change month here
    "ctl00$ctl00$cphContainer$cpContent$ddlStartDate": "2",  # Change day here
    "ctl00$ctl00$cphContainer$cpContent$ddlStartYear": "2015",  # Change year here

    # End date
    "ctl00$ctl00$cphContainer$cpContent$ddlEndMonth": latest_date_dt.strftime("%B"),
    "ctl00$ctl00$cphContainer$cpContent$ddlEndDay": latest_date_dt.strftime("%d"),
    "ctl00$ctl00$cphContainer$cpContent$ddlEndYear": latest_date_dt.strftime("%Y"),

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
