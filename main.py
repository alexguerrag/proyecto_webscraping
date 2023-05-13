#from scraping.meli import scrape_meli
from scraping.falabella import scrape_fal
import csv

# Llamamos a la función scrape_ml() para realizar el web scraping
#discounts = scrape_meli(url="https://www.mercadolibre.cl/ofertas", min_discount=50)

# Guardamos los datos en un archivo CSV

# Creamos un archivo CSV para almacenar los datos
#with open("descuentos.csv", mode="w", encoding="utf-8", newline="") as csvfile:
#    fieldnames = ['title', 'price', 'old_price', 'discount', 'link']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#    writer.writeheader()
#    for discount in discounts:
#        writer.writerow(discount)




# Llamamos a la función scrape_ml() para realizar el web scraping
discounts_fal = scrape_fal(url="https://www.adidas.cl/hombre-outlet?sale_percentage_es_cl=50%25%7C55%25%7C60%25")

# Guardamos los datos en un archivo CSV
# Creamos un archivo CSV para almacenar los datos
#with open("descuentos_falabella.csv", mode="w", encoding="utf-8", newline="") as csvfile:
#    fieldnames = ['title', 'price']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#    writer.writeheader()
#    for discount in discounts_fal:
#        writer.writerow(discount)