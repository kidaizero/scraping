import requests
from bs4 import BeautifulSoup

url = "https://qiita.com/nezuq/items/3cc9772118ad112c18dc"

r = requests.get(url)
contents = r.text

html_soup = BeautifulSoup(contents,"html.parser")

print(html_soup.title)
print(html_soup.title.string)

tags = html_soup.find_all("a")
#for tag in tags:
    #print(tag.string)
    #print(tag.get("href"))

# tag_h2 = html_soup.find_all("h2")
# for tag in tag_h2:
#     print(tag)

tags = html_soup.find_all("h2")

for tag in tags:
    print(tag.text)