from django.conf import settings

import requests
from bs4 import BeautifulSoup
import re
from json import loads

class USDEGPModule():
    def __init__(self):
        self.url = settings.USDEGP_REQUEST_URL
        self.headers = settings.USDEGP_REQUEST_HEADERS

    def get_price(self) -> str:
        try:
            request = requests.get(self.url, headers=self.headers)
            json = loads(request.text)
            print(json)
            price = json['rates']["EGP"]
            return price

        except Exception as e:
            return settings.USDEGP_REQUEST_DEFAULT_PRICE
    
class IndomieModule():
    def __init__(self):
        self.url = settings.INDOMIE_REQUEST_URL
        self.headers = settings.INDOMIE_REQUEST_HEADERS
    
    def get_price(self) -> str:
        try:
            request = requests.get(self.url, headers=self.headers)
            html = request.text
            soup = BeautifulSoup(html, 'html.parser')
            html_element = soup.find('h2', class_='css-17ctnp')
            text = html_element.text
            pattern = r'EGP \d+.\d+'
            price = re.search(pattern, text).group(0)
            return price

        except Exception as e:
            return f"EGP {settings.INDOMIE_REQUEST_DEFAULT_PRICE}"
