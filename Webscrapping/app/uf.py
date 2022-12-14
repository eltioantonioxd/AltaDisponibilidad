from selenium import webdriver
from selenium.webdriver.common.by import By
from config import set_chrome_options
from day import current_date_format
from datetime import datetime
import time


def getUf():
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get("https://valoruf.cl")

    time.sleep(3)

    try:
        uf = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/span[1]').text
        now = datetime.now()
        day = current_date_format(now)
        data = {'uf': uf, 'day': day}
        return data
    finally:
        driver.close()
