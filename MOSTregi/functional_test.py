from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    print(". . . NewVisitorTest enter")

    def setUp(self):
        print(". . . NewVisitorTest setUp")
        self.browser = webdriver.Firefox()

    def tearDown(self):
        print(". . . NewVisitorTest tearDown")
        self.browser.quit()

    def test_selenium_webdriver(self):
        print(". . . test_selenium_webdriver: ", end="")
        self.browser.get('http://localhost:8000')
        print("OK")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
