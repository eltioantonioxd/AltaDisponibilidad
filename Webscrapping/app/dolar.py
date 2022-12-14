from selenium import webdriver
from selenium.webdriver.common.by import By
from config import set_chrome_options
from day import current_date_format
from datetime import datetime
import time

def getDolar():
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get("https://www.google.com/finance/quote/USD-CLP?sa=X&ved=2ahUKEwiftpWgm_P7AhUtrpUCHfkZCQsQmY0JegQIBhAc")
    time.sleep(3)
    try:
        dolar = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[4]/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div').text
        now = datetime.now()
        day = current_date_format(now)
        data = {'dolar': dolar, 'day': day}
        return data
    finally:
        driver.close()
