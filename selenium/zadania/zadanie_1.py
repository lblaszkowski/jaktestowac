# Rekruter chce sprawdzić, że nie tylko potrafisz przepisać kod z tutoriala więc prosi Ciebie
# abyś przetestował stronę wylosowaną przez https://www.discuvver.com/ (kliknij Take me to a useful website!).
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://e.ggtimer.com/')

title = driver.title
print(title)

assert  title  == "E.gg Timer - a simple countdown timer"

driver.close()