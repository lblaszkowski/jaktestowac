from selenium import webdriver



driver = webdriver.Chrome()
driver.get('http://demo.eurobank.pl/logowanie_etap_1.html')
title = driver.title
print(title)
assert  title  == "Eurobank - Bankowość Internetowa - Logowanie"
driver.close()


