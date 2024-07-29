# selenium ile bir web sitesini ziyaret edip etkileşimde bulunabilirsiniz.
# rutin olarak yapilmasi gereken islemler oldugu zaman selenium kullanilir.

from selenium import webdriver
import time

driver=webdriver.Chrome()

url="https://sadikturan.com"

driver.get(url)

time.sleep(2)
driver.maximize_window() # sayfa acildiktan sonra sayfa tam ekran olur.

driver.save_screenshot("sadikturan.com-homepage.png")

url="https://github.com/sadikturan"
driver.get(url) # bu sayfaya gider ve 2 saniye bekler.

print(driver.title)

#fotograf ceker ve kaydeder.
if("sadikturan" in driver.title):
    driver.save_screenshot("github-sadikturan.png")

time.sleep(2)

driver.back() # sonra tekrar eski sayfaya geri doner ve kapatir.

time.sleep(2)

driver.close()
