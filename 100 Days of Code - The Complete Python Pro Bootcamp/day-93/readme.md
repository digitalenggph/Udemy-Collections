## Well Scraper PH

#### Tools used:
```pip install selenium``` ```pip install beautifulsoup4```

#### Requirements
1. Extract the following data:

| Field Name           | Description                                      |
|----------------------|--------------------------------------------------|
| Prov Code            | Provincial Code                                  |           
| Mun Code             | Municipal Code                                   |          
| Well No              | Well Number                                      |          
| Local No             | Local Number                                     |           
| Other No             | Other Number                                     |           
| Ground Elev MASL     | Ground Elevation (MASL)                          |           
| Owner                | Ownder                                           |           
| Location             | Address                                          |           
| Casing Diam mm       | Casing Diameter                                  |           
| #Rec SDPT            | Recorded StandpipeStandpipe Piezometers (SDPTs)* |           
| #Rec CDPT            | Recorded Cased Drive-Point Piezometers (CDPTs)*  |          
| #Rec Disc            | Recorded Discrete Monitoring Points*             |           

**Note: Inferred descriptions*

2. Store it in CSV/JSON
3. Store it in database (for next time

#### Steps Implemented:
1. Use Selenium to scrape data.
2. Use Pandas/json to store data
3. Use ______ to store data in a database (in another project maybe)

#### FINAL OUTPUT
![day-93-beautiful-soup](https://github.com/user-attachments/assets/3ccf67e2-cfd0-458b-a948-99e22c8a3836)
![day-93-selenium](https://github.com/user-attachments/assets/a7acbc56-e3a6-455d-bf72-915b9a1866ca)

#### Questions that came up:
1. Xpath is not working (/html/body/div/b/table). 
Turns out the HTML I'm trying to scrape is using "frames" to divide the html website into two frames (left & right).
2. [What is the fastest way to add rows to a dataframe?](https://stackoverflow.com/questions/57000903/what-is-the-fastest-and-most-efficient-way-to-append-rows-to-a-dataframe)
3. [How to open new tab in Chrome using Selenium](https://stackoverflow.com/questions/37088589/selenium-wont-open-a-new-url-in-a-new-tab-python-chrome)
4. [How do I make my code run still even when my laptop (running on MacOS) is sleeping](https://stackoverflow.com/questions/61271448/how-to-make-python-script-running-continuously-while-computer-system-in-sleeping/65228117)
5. [How to remove leading spaces only (not trailing)](https://stackoverflow.com/questions/959215/how-do-i-remove-leading-whitespace-in-python)
