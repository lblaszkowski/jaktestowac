# Znany polityk musi szybko “zniknąć” prywatną stronę z internetów i prosi
# Ciebie o zakodzenie automatu sprawdzającego czy strona xxxstwory.pln na pewno się nie wyświetla.
# Czy za pomocą asercji i tytułu jesteśmy w stanie to sprawdzić?
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://xxxstwory.pln/')

title = driver.title
print(title)

assert  title  == "xxxstwory.pln"


driver.close()
