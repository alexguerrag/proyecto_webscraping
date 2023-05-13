import requests
from bs4 import BeautifulSoup

def scrape_meli(url, min_discount):
    # Realizamos una solicitud GET a la URL de la página de ofertas
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Obtenemos el enlace de la última página
    last_page_link = soup.find("li", class_="andes-pagination__button--next").find("a")["href"]
    last_page_number = int(last_page_link.split("=")[-1])
    
    # Creamos una lista para almacenar los datos de los productos que cumplan con nuestro criterio de descuento mínimo
    discounted_products = []

    # Recorremos todas las páginas y extraemos los productos en oferta de cada una de ellas
    for page_number in range(1, last_page_number + 1):
        page_url = f"{url}?container_id=MLC779365-1&page={page_number}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontramos todos los productos en la página actual
        products = soup.find_all('li', {'class': 'promotion-item'})

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
