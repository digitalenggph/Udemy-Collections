import time

import requests, os, json
from bs4 import BeautifulSoup

# for measuring runtime
start_time = time.time()
main_url = os.getenv("WELL_DATABANK_URL")

def get_soup(url_concat):
    url = main_url + url_concat
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def get_link(soup, loc):
    for tr in soup.find_all('a'):
        if tr.get_text().strip() == loc:
            return tr.get('href')
    return None

def get_table(url_concat, well=None):
    soup = get_soup(url_concat)
    table = [row.get_text() for row in soup.find_all('tr')]
    header = [thead.strip() for thead in table[0].strip().split('\n') if thead.strip() != '']

    if well:
        # some of the new lines in the right end represents empty data so they must not be stripped
        body = [trow.lstrip() for trow in table[1:]]
    else:
        body = [trow.strip() for trow in table[1:]]

    return  soup, header, body

def get_data(soup, header, body, level=None):
    table_rows = []
    if body:
        for row in body:
            cells = row.split('\n')

            if level=='municipal':
                try:
                    empty_cell_index = cells.index('')
                except ValueError:
                    pass
                else:
                    cells.pop(empty_cell_index)

            elif level=='well':
                cells = [cell for cell in cells if cell != '\r']
                if cells[-1].strip() == '':
                    cells.pop()

                if len(header) != len(cells):
                    print(len(cells) == len(header), [cell.strip() for cell in cells])
                    # Somewhere in DAS
                    merged_address = cells[7] + ', ' + cells[8]
                    cells = cells[:7] + [merged_address] + cells[9:]
                    print(cells)

            row_data = {header[i]: cells[i].strip() for i in range(len(cells))}

            if 'Google Map' in header:
                 row_data['link'] = get_link(soup, row_data[header[0]])
                 row_data['Google Map'] = get_link(soup, 'Google Map')

            if row_data[header[0]] != 'TOTAL':
                table_rows.append(row_data)

    return table_rows

# ---------------------- GET PROVINCE DATA (LIST OF DICTIONARY) ---------------------- #
province_soup, province_header, province_body = get_table('ProvSum.asp')
province_data = get_data(province_soup, province_header, province_body)
print(province_data)

# -------------------- GET MUNICIPALITY DATA (LIST OF DICTIONARY) -------------------- #
municipalities_data = []

for province in province_data:
    link_to_municipality = province["link"]
    if link_to_municipality:
        time.sleep(1.0)
        municipality_soup, municipality_header, municipality_body = get_table(link_to_municipality)
        municipality_data = get_data(municipality_soup, municipality_header, municipality_body,
                                     level='municipal')

        for municipality in municipality_data:
            municipality['Province'] = province["Province"]

        print('municipal: ', municipality_data)
        municipalities_data.extend(municipality_data) # <-- Data

with open('municipalities_beautiful_soup.json', 'w') as file:
    json.dump(municipalities_data, file, indent=4)


# -------------------- GET RECORDS DATA (LIST OF DICTIONARY) -------------------- #

well_records = []

for municipality in municipalities_data:
    link_to_records = municipality["link"]
    if link_to_records:
        well_indices_soup = get_soup(link_to_records)
        indices = {int(index.get_text().strip()): index.get('href')
                        for index in well_indices_soup.find_all('a')
                        if index.get_text().strip() != 'Google Map'}

        for index, link_to_wells in indices.items():
            time.sleep(1.0)
            records_soup, records_header, records_body = get_table(link_to_wells, well=True)
            records_data = get_data(records_soup, records_header, records_body,
                                    level='well')

            for records in records_data:
                records['Province'] = municipality["Province"]
                records['Municipality'] = municipality["Municipality"]

            well_records.extend(records_data)
            print(records_data) # for tracking

with open('records_beautiful_soup.json', 'w') as file:
    json.dump(well_records, file, indent=4)

print("--- %s seconds ---" % (time.time() - start_time))