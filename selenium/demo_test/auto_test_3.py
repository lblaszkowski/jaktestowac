import unittest
from selenium import webdriver


class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
        self.driver = webdriver.Chrome()

    def setUp(self):
        pass

    def test_demo_login(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Logowanie',
                         f'Otrzymana wartość title różni się od oczekiwanej dla strony: (url)')

    def test_demo_accounts(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont',
                         f'Otrzymana wartość title różni się od oczekiwanej dla strony: (url)')

    # def test_main_page(self):
    #     driver = self.driver
    #     url = 'http://eurobank.pl/'
    #     driver.get(url)
    #     title = driver.title
    #     print(title)
    #     self.assertEqual(title, 'Eurobank - wygodny bank na co dzień - eurobank.pl',
    #                      f'Otrzymana wartość title różni się od oczekiwanej dla strony: (url)')

    def test_demo_pulpit(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Pulpit',
                         f'Otrzymana wartość title różni się od oczekiwanej dla strony: (url)')

    def test_przelew_dowolny(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Przelew dowolny',
                         f'Otrzymana wartość title różni się od oczekiwanej dla strony: (url)')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.close()

