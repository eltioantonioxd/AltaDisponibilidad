import requests
from bs4 import BeautifulSoup
from day import current_date_format
from datetime import datetime
import time

def getTemp():
    page = requests.get('https://www.tiempo3.com/south-america/chile/region-metropolitana/santiago?page=today')
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        td_items = soup.find_all('td')
        hours = []
        temp = []
        cont = 0
        for td in td_items:
            if cont < 8:
                hours.append(td.text)
                cont = cont + 1
            elif 8 <= cont and cont < 16:
                temp.append(td.text)
                cont = cont + 1

        now = datetime.now()
        day = current_date_format(now)
        data = {'day': day, 'hours': hours, 'temp': temp}
        return data
    except:
        print("Error Scrapper")