import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Firefox

from base import FunctionalTest

class DummyTest(FunctionalTest):

    def test_selenium_webdriver(self):
        print(". . . test_selenium_webdriver: ", end="")
        self.browser.get('http://localhost:8000')
        print("OK")
