import requests
from urllib.parse import unquote

class NonEncodedSession(requests.Session):
    def send(self,*a,**kw):
        #適用されたエンコードをもとに戻す
        a[0].url = unquote(a[0].url)
        return requests.Session.send(self,*a,**kw)

my_requests = NonEncodedSession()
url = "http://www.example.com/?spaces |pipe"
r = my_requests.get(url)
print(r.url)


#-----------------------------------------------------
def calc(a,b,op):
    url = "http://www.webscrapingfordatascience.com/calchttp/"
    params = {"a":a,"b":b,"op":op}
    r = requests.get(url,params = params)
    return r.text
print(calc(4,6,"*"))
print(calc(4,6,"/"))

#--------------------------------------------------------
url = "https://en.wikipedia.org/w/index.php"+"?title=List_of_Game_of_Thrones_episodes&oldid=802553687"
r = requests.get(url)
print(r.text)