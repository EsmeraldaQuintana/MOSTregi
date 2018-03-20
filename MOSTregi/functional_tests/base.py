import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Firefox

# SCREEN_DUMP_LOCATION = os.path.join(
#     os.path.dirname(os.path.abspath(__file__)), 'screendumps'
# )

class FunctionalTest(unittest.TestCase):

    def setUp(self):
        print(". . . FunctionalTest setUp")
        self.browser = webdriver.Firefox()

    def tearDown(self):
        print(". . . FunctionalTest tearDown")
        self.browser.quit()
        super().tearDown()

    # CODE TO BE USED LATER

    # def take_screenshot(self):
    #     filename = self._get_filename() + '.png'
    #     print('screenshotting to', filename)
    #     self.browser.get_screenshot_as_file(filename)

    # @wait
    # def wait_to_be_logged_in(self, email):
    #     self.browser.find_element_by_link_text('Log out')
    #     navbar = self.browser.find_element_by_css_selector('.navbar')
    #     self.assertIn(email, navbar.text)
    #
    # @wait
    # def wait_to_be_logged_out(self, email):
    #     self.browser.find_element_by_name('email')
    #     navbar = self.browser.find_element_by_css_selector('.navbar')
    #     self.assertNotIn(email, navbar.text)
