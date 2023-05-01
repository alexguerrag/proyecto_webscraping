import requests
from bs4 import BeautifulSoup

def scrape_ml(url, min_discount):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    discount_spans = soup.find_all("span", class_="andes-money-amount__discount")
    discounts = [discount.text.strip() for discount in discount_spans if "%" in discount.text and int(discount.text.split("%")[0]) >= 50]
    
    print(discounts)
    return discounts
