from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # Wilson opens his browser to his favorite to-do list app
        self.browser.get(self.live_server_url)

        # He notices that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He has the opportunity to create a to-do list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Like any obedient developer, he creates a reminder to:
        # 'Obey the Testing Goat'
        inputbox.send_keys('Obey the Testing Goat')

        # When he hits enter, the page updates and now lists his new
        # to-do: '1: Continue obeying the Test Goat' as a to-do item
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Obey the Testing Goat')

        # There is still a text box inviting Wilson to add another item
        # so he adds 'Step carefully along the cliff's wall'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Step carefully along the cliff wall')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, displaying both items on the list
        self.wait_for_row_in_list_table('1: Obey the Testing Goat')
        self.wait_for_row_in_list_table(
            '2: Step carefully along the cliff wall')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Wilson starts a new todo list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Obey the Testing Goat')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Obey the Testing Goat')

        # Wilson is presented with a URL unique to his list
        wilson_list_url = self.browser.current_url
        self.assertRegex(wilson_list_url, '/lists/.+')

        # Now a new user, Jean, visits the site

        ## Open a new browser session to ensure no information from
        ## Wilson's session is coming from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Jean visits the home page, there is no sign of Wilson's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Obey the Testing Goat', page_text)
        self.assertNotIn('make a fly', page_text)

        # Jean starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Jean receives her own unique URL
        jean_list_url = self.browser.current_url
        self.assertRegex(jean_list_url, '/lists/.+')
        self.assertNotEqual(jean_list_url, wilson_list_url)

        # Again, there is no trace of Wilson's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Obey the Testing Goat', page_text)
        inputbox.send_keys('Buy milk')

