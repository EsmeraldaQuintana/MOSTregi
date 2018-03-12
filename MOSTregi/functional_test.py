from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Firefox
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

    def test_can_view_the_registration_form(self):
        print(". . . test_can_view_the_registration_form... ")
        print(". . . > the user can get to the add page")
        self.browser.get('http://localhost:8000/events/new/')

        print(". . . > the user can see the form")
        form = self.browser.find_element_by_tag_name('form')

        # FORM FIELDS TESTS
        print(". . . > the user can see the name field")
        self.browser.find_element_by_id("id_name")
        print(". . . > .................... email field")
        self.browser.find_element_by_id("id_email")
        print(". . . > .................... telephone field")
        self.browser.find_element_by_id("id_telephone")
        print(". . . > .................... date request field")
        self.browser.find_element_by_id("id_date_request")
        print(". . . > .................... arrival time field")
        self.browser.find_element_by_id("id_arrival_time")
        print(". . . > .................... departure time field")
        self.browser.find_element_by_id("id_departure_time")
        print(". . . > .................... number_attending field")
        self.browser.find_element_by_id("id_number_attending")
        print(". . . > .................... school field")
        self.browser.find_element_by_id("id_school")

        print(". . . > the user can submit information on form")
        self.fail('FINISH THE TEST')
        #response = webdriver.request('POST', '/events/new/', data={})
        #print(response)
        #self.assertIn('Devito', response.content.decode())

        print(". . . test_can_view_the_registration_form: OK")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(NewVisitorTest('test_selenium_webdriver'))
    suite.addTest(NewVisitorTest('test_can_view_the_registration_form'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())
    #unittest.main(warnings='ignore')
