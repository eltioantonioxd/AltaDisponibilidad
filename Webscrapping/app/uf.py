from selenium import webdriver
from selenium.webdriver.common.by import By
from config import set_chrome_options
import time

def getUf():
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get("https://valoruf.cl")
    time.sleep(3)
    try:
        uf = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/span[1]').text
        day = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/span[2]').text
        data = {'uf': uf, 'day': day}
        return data
    finally:
        driver.close()
