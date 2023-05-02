import requests
from bs4 import BeautifulSoup

def scrape_ml2(url, min_discount):
    # Realizamos una solicitud GET a la URL del producto
    response = requests.get(url)

    # Parseamos el contenido HTML de la página utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontramos todos los productos en la página
    products = soup.find_all('li', {'class': 'promotion-item'})

    # Creamos una lista para almacenar los datos de los productos que cumplan con nuestro criterio de descuento mínimo
    discounted_products = []

    # Recorremos cada producto y extraemos su información
    for product in products:
        # Extraemos el título del producto
        title = product.find('p', {'class': 'promotion-item__title'}).text.strip()

        # Extraemos el precio actual del producto
        price = product.find('span', {'class': 'andes-money-amount__fraction'}).text.strip()

        # Extraemos el precio anterior del producto, si existe
        old_price_tag = product.find('s', {'class': 'andes-money-amount-combo__previous-value'})
        if old_price_tag is not None:
            old_price = old_price_tag.find('span', {'class': 'andes-money-amount__fraction'}).text.strip()
        else:
            old_price = price

        # Buscamos el porcentaje de descuento
        discount_tag = product.find('span', {'class': 'andes-money-amount__discount'})
        if discount_tag is not None:
            discount = discount_tag.text.strip().replace('% OFF', '')
            discount = float(discount)
        else:
            discount = 0.0

        # Obtenemos el enlace del producto
        link_tag = product.find('a', {'class': 'promotion-item__link-container'})
        link = link_tag['href'] if link_tag is not None else ''

        # Si el porcentaje de descuento es mayor o igual al mínimo deseado, agregamos el producto a la lista
        if discount >= min_discount:
            discounted_products.append({'title': title, 'price': price, 'old_price': old_price, 'discount': discount, 'link': link})

    return discounted_products
