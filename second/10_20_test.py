import requests
from bs4 import BeautifulSoup

#webサイトからhtmlや、httpの情報を入手している
url = requests.get("https://ja.wikipedia.org/wiki/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF)")

#そのサイトを作っているコードを抽出する
content = url.content

soup = BeautifulSoup(content,"html.parser")

#サイトの文字だけ表示
# print(soup.text)

#それぞれサイトを構成している要素を出力 soupになると整理されている
#print(content)
#print(soup)

# 紹介だけを抽出
person_text = soup.find_all("p")
# person_text = soup.find_all("p").text  使えない
# person_text = soup.find("p")
#person_text = soup.find("p").text

#print(person_text)

for te in person_text:
    print(te.text)
