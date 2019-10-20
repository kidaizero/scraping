from bs4 import BeautifulSoup
import requests

url = "https://ja.wikipedia.org/wiki/%E9%BD%8A%E8%97%A4%E4%BA%AC%E5%AD%90"

#urlから文字を取得
r = requests.get(url)
contents = r.text

#下準備
html_soup = BeautifulSoup(contents,"html.parser")


#タイトルを受取り出力
print(html_soup.title)
#タグを含まないで中の文字列だけ取得
print(html_soup.title.string)

#複数のurlを取得 <a>などから受け取る
print(html_soup.a) #この場合一個しか取れない

#find_allメソッドを使ってすべての要素を取り出すことができる リスト形式
print(html_soup.find_all("a"))
#一つ一つ表示する
tags = html_soup.find_all("a")
for tag in tags:
    #タグの文字を取りたい
    print(tag.string)
    #リンクだけを取りたい場合
    #print(tag.get("href"))

print("------------------------------きれいに並べる")
#print(html_soup.prettify())

#print(html_soup.findall("h3",{"class":"??????"}))
