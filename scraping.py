import requests
from bs4 import BeautifulSoup

# demo website for web scraping purposes
url = "http://books.toscrape.com/index.html"

response = requests.get(url)
html = response.content

scraped = BeautifulSoup(html, 'html.parser')

articles = scraped.select(".product_pod")

title_prices_description = []

for article in articles:
        title = article.h3.a["title"]
        price = float(article.find("p", class_="price_color").text.lstrip("£"))

        title_prices_description.append({"title": title, "price": price})

print(sorted(title_prices_description, key=lambda d: d['price']))