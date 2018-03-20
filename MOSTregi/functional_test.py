import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Firefox

class FunctionalTest(unittest.TestCase):

    def setUp(self):
        print(". . . FunctionalTest setUp")
        self.browser = webdriver.Firefox()

    def tearDown(self):
        print(". . . FunctionalTest tearDown")
        self.browser.quit()

    def test_selenium_webdriver(self):
        print(". . . test_selenium_webdriver: ", end="")
        self.browser.get('http://localhost:8000')
        print("OK")

    def test_can_register_event(self):
        print(". . . test_can_register_event... ")
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
        self.browser.find_element_by_id("id_arrival_time_hour")
        print(". . . > .................... departure time field")
        self.browser.find_element_by_id("id_departure_time_hour")
        # print(". . . > .................... number_attending field")
        self.browser.find_element_by_id("id_number_attending")
        print(". . . > .................... school field")
        self.browser.find_element_by_id("id_school")

        name = self.browser.find_element_by_css_selector('input#id_name')
        name.clear()
        # time.sleep(.5)
        name.send_keys("Danny Burrito")
        name = self.browser.find_element_by_css_selector('input#id_email')
        name.clear()
        # time.sleep(.5)
        name.send_keys("person@webbersitorino.com")
        name = self.browser.find_element_by_css_selector('input#id_telephone')
        name.clear()
        # time.sleep(.5)
        name.send_keys("6463012333")
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_hour')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_minute')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_meridiem')
        name.send_keys(Keys.UP)
        # arrival: 10:30 a.m.
        name = self.browser.find_element_by_css_selector('select#id_departure_time_hour')
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_departure_time_meridiem')
        name.send_keys(Keys.DOWN)
        # departure: 12:00 p.m.
        name = self.browser.find_element_by_css_selector('input#id_number_attending')
        name.clear()
        name.send_keys("20")
        name = self.browser.find_element_by_css_selector('input#id_school')
        name.clear()
        name.send_keys("Schoolversity")
        name.submit()
        print(". . . test_can_register_event: OK")

    def test_can_edit_form(self):
        print(". . . test_can_edit_form... ")
        print(". . . > the user can get to the add page")
        self.browser.get('http://localhost:8000/events/new/')
        # ADD INFORMATION
        name = self.browser.find_element_by_css_selector('input#id_name')
        name.clear()
        name.send_keys("Danny Burrito")
        name = self.browser.find_element_by_css_selector('input#id_email')
        name.clear()
        name.send_keys("person@webbersitorino.com")
        name = self.browser.find_element_by_css_selector('input#id_telephone')
        name.clear()
        name.send_keys("6463012333")
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_hour')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_minute')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_meridiem')
        name.send_keys(Keys.UP)
        name = self.browser.find_element_by_css_selector('select#id_departure_time_hour')
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_departure_time_meridiem')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('input#id_number_attending')
        name.clear()
        name.send_keys("20")
        name = self.browser.find_element_by_css_selector('input#id_school')
        name.clear()
        name.send_keys("Schoolversity")
        name.submit()
        # go to edit page
        time.sleep(1)
        button = self.browser.find_element_by_id('edit_button')
        button.click()
        # ADD INFORMATION (again)
        name = self.browser.find_element_by_css_selector('input#id_name')
        name.clear()
        name.send_keys("Danny Burrito")
        name = self.browser.find_element_by_css_selector('input#id_email')
        name.clear()
        name.send_keys("person@webbersitorino.com")
        name = self.browser.find_element_by_css_selector('input#id_telephone')
        name.clear()
        name.send_keys("6463012333")
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_hour')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_minute')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_meridiem')
        name.send_keys(Keys.UP)
        # arrival: 10:30 a.m.
        name = self.browser.find_element_by_css_selector('select#id_departure_time_hour')
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_departure_time_meridiem')
        name.send_keys(Keys.DOWN)
        # departure: 12:00 p.m.
        name = self.browser.find_element_by_css_selector('input#id_number_attending')
        name.clear()
        name.send_keys("20")
        name = self.browser.find_element_by_css_selector('input#id_school')
        name.clear()
        name.send_keys("Schoolversity")
        name.submit()
        print(". . . test_can_edit_form: OK")

    def test_can_see_post_list(self):
        print(". . . test_can_see_post_list... ")
        # go to new form
        self.browser.get('http://localhost:8000/events/new/')
        # submit information
        name = self.browser.find_element_by_css_selector('input#id_name')
        name.clear()
        name.send_keys("Danny Likes PageLists")
        name = self.browser.find_element_by_css_selector('input#id_email')
        name.clear()
        name.send_keys("person@webbersitorino.com")
        name = self.browser.find_element_by_css_selector('input#id_telephone')
        name.clear()
        name.send_keys("6463012333")
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_hour')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_minute')
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_arrival_time_meridiem')
        name.send_keys(Keys.UP)
        # arrival: 10:30 a.m.
        name = self.browser.find_element_by_css_selector('select#id_departure_time_hour')
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name.send_keys(Keys.DOWN)
        name = self.browser.find_element_by_css_selector('select#id_departure_time_meridiem')
        name.send_keys(Keys.DOWN)
        # departure: 12:00 p.m.
        name = self.browser.find_element_by_css_selector('input#id_number_attending')
        name.clear()
        name.send_keys("20")
        name = self.browser.find_element_by_css_selector('input#id_school')
        name.clear()
        name.send_keys("Schoolversity")
        name.submit()
        # go to event event_list
        self.browser.get('http://localhost:8000/events/all/')
        # see event is there
        html = self.browser.find_element_by_tag_name('tbody').text
        self.assertIn('Danny Likes PageLists', html)
        print(". . . test_can_edit_form: OK")

    def test_can_delete_post(self):
        self.fail('Finish the test...')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FunctionalTest('test_selenium_webdriver'))
    suite.addTest(FunctionalTest('test_can_register_event'))
    suite.addTest(FunctionalTest('test_can_edit_form'))
    suite.addTest(FunctionalTest('test_can_see_post_list'))
    suite.addTest(FunctionalTest('test_can_delete_post'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())
    #unittest.main(warnings='ignore')
