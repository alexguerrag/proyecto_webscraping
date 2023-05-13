import requests
from bs4 import BeautifulSoup

url = 'https://www.adidas.cl/hombre-outlet?sale_percentage_es_cl=50%25%7C55%25%7C60%25'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

products = soup.find_all('div', {'class': 'product-tile-wrapper'})
for product in products:
    name = product.find('div', {'class': 'product-tile-details'}).find('a').text.strip()
    price = product.find('span', {'class': 'product-price'}).text.strip()
    print(name, price)






''' def scrape_fal(url):
    # Realizamos una solicitud GET a la URL de la página de ofertas
    response = requests.get(url)

    # Parseamos el contenido HTML de la página utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontramos todos los productos en la página
    products = soup.find_all('div', {'class': 'grid-item'})

    # Recorremos cada producto y extraemos su información
    for product in products:
        # Extraemos el precio normal del producto
        price = product.find('div', {'class': 'gl-price-item gl-price-item--crossed notranslate'}).text.strip()
        print("Precio normal:", price)
 '''