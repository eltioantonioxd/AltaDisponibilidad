import requests
from bs4 import BeautifulSoup
from day import current_date_format
from datetime import datetime
import time

def getDolar():
    page = requests.get('https://www.google.com/finance/quote/USD-CLP?sa=X&ved=2ahUKEwiftpWgm_P7AhUtrpUCHfkZCQsQmY0JegQIBhAc')
    soup = BeautifulSoup(page.text, 'html.parser')

    try:
        span_items = soup.find_all('span')
        for span in span_items:
            if span.find(class_='YMlKec fxKbKc') != None:
                dollar = span.find(class_='YMlKec fxKbKc').text
                
        now = datetime.now()
        day = current_date_format(now)
        data = {'dollar': dollar, 'day': day}
        return data
    finally:
        print("Error Scrapper")