import sqlite3
import requests
from bs4 import BeautifulSoup
conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Назва_звіра TEXT,
    Тип_звіра TEXT
)
""")

cursor.executemany(
    "INSERT INTO Animals (Назва_звіра, Тип_звіра) VALUES (?, ?)",
    [
        ("Лев", "Ссавець"),
        ("Крокодил", "Плазун"),
        ("Орел", "Птах"),
        ("Морська черепаха", "Плазун"),
        ("Мавпа", "Ссавець")
    ]
)

cursor.execute(
    "UPDATE Animals SET Назва_звіра = 'Сокіл' WHERE Назва_звіра = 'Орел'"
)

cursor.execute("SELECT * FROM Animals WHERE Тип_звіра = 'Ссавець'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Animals")
print(cursor.fetchall())

conn.commit()
conn.close()
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