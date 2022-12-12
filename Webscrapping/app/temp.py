from selenium import webdriver
from selenium.webdriver.common.by import By
from config import set_chrome_options
import time

def getTemp():
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get('https://www.meteored.cl/tiempo-en_Santiago+de+Chile-America+Sur-Chile-Region+Metropolitana+de+Santiago-SCEL-horas-18578.html')
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, '//*[@id="sendOpGdpr"]').click()
        n = 4
        hours = []
        temp = []
        for i in range(0,8):
            hours.append(driver.find_element(By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr['+str(n)+']/td[2]/span').text)
            temp.append(driver.find_element(By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr['+str(n)+']/td[5]').text)
            n = n + 7

        day = driver.find_element(By.XPATH, '/html/body/span[2]/span[2]/span/span[1]/section/h3/span').text
        data = {'day': day, 'hours': hours, 'temp': temp}
        return data
    finally:
        driver.close()