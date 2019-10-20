from bs4 import BeautifulSoup
import requests

url = requests.get("https://news.yahoo.co.jp/")
content = url.content

soup = BeautifulSoup(content,"html.parser")

# f_soup = soup.find("ul","newsFeed_list")
f_soup = soup.find_all("li")

# f_soup = soup.find_all("li","newsFeed_item")

for ingre in f_soup:
    print(ingre.text)

# print(f_soup)
# print(f_soup.text)