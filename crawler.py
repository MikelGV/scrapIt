import requests
from bs4 import BeautifulSoup
import sys

def web(page, webUrl):
    if page > 0:
        url = webUrl
        code = requests.get(url)
        plain = code.text
        soup = BeautifulSoup(plain, 'html.parser')
        for link in soup.findAll('a', {'class': 'soup-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet2 = link.get('href')
            print(tet2)
web(1, 'https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles')