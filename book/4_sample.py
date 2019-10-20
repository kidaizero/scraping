import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687"

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents,"html.parser")
#最初の<h1>タグを検索する
first_h1 = html_soup.find("h1")

print(first_h1.name)
print(first_h1.contents)

print(str(first_h1))

print(first_h1.text) #Game of Thrones episodesのリスト
print(first_h1.get_text()) #上と同じ処理

print(first_h1.attrs)

print(first_h1.attrs["id"])
print(first_h1["id"])#上と同じ処理
print(first_h1.get("id"))#上と同じ処理

print("-----------CITATIONS-------------")
print("citationクラスを持つcite要素のうちの最初の5個を検索する")
cites = html_soup.find_all("cite",class_ = "citation",limit = 5)
print(cites)
for citation in cites:
    print(citation.get_text())
    #このcite要素の内部で最初タグを検索する
    link = citation.find("a")
    #さらにURLを表示する
    print(link.get("href"))
    print()

#linkに求めるものが存在しない場合Noneが返されてエラーが起こる 注意する


