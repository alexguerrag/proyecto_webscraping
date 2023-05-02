from scraping.meli_v02 import scrape_ml2

# Llamamos a la función scrape_ml() para realizar el web scraping
discounts = scrape_ml2(url="https://www.mercadolibre.cl/ofertas", min_discount=50)

# Guardamos los datos en un archivo CSV
import csv
# Creamos un archivo CSV para almacenar los datos
with open("descuentos.csv", mode="w", encoding="utf-8", newline="") as csvfile:
    fieldnames = ['title', 'price', 'old_price', 'discount', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for discount in discounts:
        writer.writerow(discount)
