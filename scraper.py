import requests
from bs4 import BeautifulSoup

url=input("URL: ")
r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"},timeout=15)
r.raise_for_status()
soup=BeautifulSoup(r.text,"html.parser")
for i,tag in enumerate(soup.find_all(["h1","h2","h3","p"])[:50],1):
    text=" ".join(tag.get_text(" ",strip=True).split())
    if text: print(i,text)
