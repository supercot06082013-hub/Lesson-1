import requests
from bs4 import BeautifulSoup
base = "http://books.toscrape.com/"
url = base + "catalogue/page-1.html"

while True:
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    for b in s.select("article.product_pod"):
        title = b.h3.a["title"]
        price = b.select_one(".price_color").text
        stock = b.select_one(".availability").text.strip()
        print(title, "|", price, "|", stock)

    n = s.select_one("li.next a")
    if not n:
        break
    url = base + "catalogue/" + n["href"]