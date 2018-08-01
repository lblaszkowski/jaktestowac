import unittest
from selenium import webdriver


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
        self.driver = webdriver.Chrome()

    def test_demo_login(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert  title  == "Eurobank - Bankowość Internetowa - Logowanie"


    def test_demo_accounts(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/konta.html')
        title = driver.title
        print(title)
        assert title == 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont'


    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/pulpit.html')
        title = driver.title
        print(title)
        assert title == 'Eurobank - Bankowość Internetowa - Pulpit'

    def test_przelew_dowolny(self):
        driver =  self.driver
        driver.get('http://demo.eurobank.pl/przelew_nowy_zew.html')
        title = driver.title
        print(title)
        assert  title == 'Eurobank - Bankowość Internetowa - Przelew dowolny'

    @classmethod
    def tearDownClass(self):
         self.driver.close()

if __name__ == '__main__':
        unittest.main()
