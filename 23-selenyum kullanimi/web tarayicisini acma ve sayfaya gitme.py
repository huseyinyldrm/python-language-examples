from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#WebDriver'in yolunu belirtin.(örn. 'path/to/chromedriver')
driverPath="path/to/chromedriver"

# Crome WebDriver'ini baslat.
driver=webdriver.Chrome()

#bir web sayfasina git.

driver.get("https://www.youtube.com/")

#sayfanin basligini yazdir.
print(driver.title)

#tarayiciyi kapat.
driver.quit()