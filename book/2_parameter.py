import requests
from urllib.parse import quote,quote_plus
 
#query文字も出力される
url = "http://www.webscrapingfordatascience.com/paramhttp/?query=test"
r = requests.get(url)
print(r.text)

#クエリ文字に空白があった場合､エンコーディングされる
url = "http://www.webscrapingfordatascience.com/paramhttp/?query= a query with spaces"
r = requests.get(url)

print(r.request.url)
print(r.text)

#パラメーターはエンコーディングできない
url = "http://www.webscrapingfordatascience.com/paramhttp/?query=complex?&"
r = requests.get(url)
print(r.request.url)
print(r.text)


# &などのクエリ文字に含まれる特殊文字をエンコーディングする
# plus はスペースをプラスに置き換える ほかはquoteとほぼ同じ スラッシュもエンコードする
raw_string = "aquery with/,spaces and?&"
print(quote(raw_string))
print(quote_plus(raw_string))

print("---------------------------------------------------------------------------------")
url = "http://www.webscrapingfordatascience.com/paramhttp/?query="
print("\nUsing quote:")
# /を含め安全な文字はないので全てエンコードする
r = requests.get(url+quote(raw_string,safe=""))
print(r.url)
print(r.text)

print("\nUsing quote_plus:")
r = requests.get(url + quote_plus(raw_string))
print(r.url)
print(r.text)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー 
#上記のサンプルを書き換える
url = "http://www.webscrapingfordatascience.com/paramhttp/"
parameters = {
    "query":"a query with /, spaces and?&"
}
r = requests.get(url,params = parameters)
print(r.url)
print(r.text)