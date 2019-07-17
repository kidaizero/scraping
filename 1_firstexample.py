import requests


url = "http://www.webscrapingfordatascience.com/basichttp/"
r = requests.get(url)  #HTTPレスポンスに関する多くの情報が格納される
print(r.text)



#サーバーから返されたHTTPステータスコード
print(r.status_code)

#テキストのステータスメッセージ
print(r.reason)

#HTTPレスポンスヘッダー
print(r.headers)

#リクエスト情報はr.requestにPythonオブジェクトとして保存される
print(r.request)

#HTTPリクエストヘッダー
print(r.request.headers)

#HTTPレスポンスのコンテンツ
print(r.text)


url = "http://www.webscrapingfordatascience.com/paramhttp/" 
#http://www.webscrapingfordatascience.com/paramhttp/?query=test  ?････ はクエリ文字列  =の後の文字列が代入される
#http://www.webscrapingfordatascience.com/paramhttp/?query=another%20test%3F%26   &にエンコーディングされる
#パラメーター同士は&で区切る  キーと値の間には=(等号)を入れる 
#同じサイトの中でも絞り込みなどに使う
#このサイトがわかりやすい  https://online.dhw.co.jp/kuritama/query-string/
r = requests.get(url)
print(r.text)