import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('toon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title", "name", "star"])

toon_URL = f'https://comic.naver.com/webtoon/weekdayList?week=fri'
toon_html = requests.get(toon_URL)
webtoon_soup = BeautifulSoup(toon_html.text, "html.parser")
toon_img_list = webtoon_soup.find("ul", {"class": "img_list"})
toon_list = toon_img_list.find_all("li")

final_result = []
final_result += extract_info(toon_list)


# csv
for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['name'])
    row.append(result['star'])
    writer.writerow(row)

print(final_result)
