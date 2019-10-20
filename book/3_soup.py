import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687"

r = requests.get(url)
html_contents = r.text

#HTMLをpythonで読み込むのにパーサーというものを使っていて､沢山の種類がある
#よってパーサーを指定する必要がある
html_soup = BeautifulSoup(html_contents,"html.parser")

print(html_soup.find("h1"))
print("--------------------------------")
print(html_soup.find("",{"id":"p-logo"}))
print("--------------------------------")
for found in html_soup.find_all(["h1","h2"]):
    print(found)