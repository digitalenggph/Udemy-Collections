import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies = response.text

soup = BeautifulSoup(movies, "html.parser")
title_list = soup.find_all(name="h3", class_="title")

titles = [title.getText() for title in title_list]
titles.reverse()

with open("movies.txt", mode='w', encoding="UTF-8") as file:
    for title in titles:
        file.write(f"{title}\n")
