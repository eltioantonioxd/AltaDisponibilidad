import requests
from bs4 import BeautifulSoup
from day import current_date_format
from datetime import datetime
import time


def getUf():
    page = requests.get('https://valoruf.cl')
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        span_items = soup.find_all('span')
        uf = span_items[0].text
        now = datetime.now()
        day = current_date_format(now)
        data = {'uf': uf, 'day': day}
        return data
    finally:
        print("Error Scrapper")
