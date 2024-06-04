from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://news.ycombinator.com")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles_find = soup.find_all(name="span", class_="titleline")
articles_title_list = [article.getText() for article in articles_find]
articles_href_list = [article.span.a.get("href") for article in articles_find]

upvote_find = soup.find_all(name="span", class_="score")
upvote_list = [int(upvote.getText().replace(" points", "")) for upvote in upvote_find]

"""
for article in articles_title_list:
    print(article.getText())

for article in articles_title_list:
    print(article.span.a.get("href"))
"""

# quick-fix line since one of the entries do not have any upvote yet.
upvote_list.insert(8,0)

yc_df = pd.DataFrame({"title": articles_title_list, "link": articles_href_list, "upvote": upvote_list})

max_vote = yc_df['upvote'].max()

for index, row in yc_df.iterrows():
    if row.upvote == max_vote:
        print(row.title, row.link)


# print(len(articles_title_list), len(articles_href_list), len(upvote_list))
# print(articles_title_list)
# print(articles_href_list)
#
#
























"""
with open("website.html", encoding='utf-8') as website:
    contents = website.read()

soup = BeautifulSoup(contents, 'html.parser')
"""

"""
# Part 1
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())

print(soup.a)
print(soup.p)
"""

"""
# Part 2
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

tags = [{tag.getText(): tag.get("href")} for tag in all_anchor_tags]
print(tags)

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.name, section_heading.string)

company_url = soup.select_one(selector="p a")
print(company_url.string)

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)

name = soup.select_one("#name")
print(name.string)

headings = soup.select(".heading")
print(heading.name)
"""




