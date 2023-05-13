import requests
from bs4 import BeautifulSoup

url = 'https://www.adidas.cl/hombre-outlet?sale_percentage_es_cl=50%25%7C55%25%7C60%25'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

products = soup.find_all('div', {'class': 'grid-item'})
for product in products:
    name = product.find('p', {'class': 'glass-product-card__title'}).find('a').text.strip()
    price = product.find('div', {'class': 'gl-price-item gl-price-item--crossed notranslate'}).text.strip()
    print(name, price)