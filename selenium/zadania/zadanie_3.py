import unittest
from selenium import webdriver

class Page_MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
        self.driver = webdriver.Chrome()

    def SetUp(self):
        print("Początek testu")

    def test_page_title_mailinator(self):
        driver = self.driver
        driver.get('http://www.mailinator.com/')
        title = driver.title
        print(title)
        assert  title  == "Mailinator"

    def test_page_title_keepmeout(self):
        driver = self.driver
        driver.get('http://keepmeout.com/en/')
        title = driver.title
        print(title)
        assert  title  == "KeepMeOut"

    def tearDown(self):
        print("Koniec testu")

    @classmethod
    def tearDownClass(self):
        self.driver.close()

