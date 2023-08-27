import requests
from bs4 import BeautifulSoup

#def scrape_adi(url):
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
html_page = requests.get("https://www.adidas.cl/performance", headers=hdr, timeout=15)
soup = BeautifulSoup(html_page.content, 'html.parser')
print(soup)

#    return soup