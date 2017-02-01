from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Wilson opens his browser to his favorite to-do list app
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Obey the Testing Goat' for row in rows)
        )

        # There is still a text box inviting Wilson to add another item
        # so he adds 'Step carefully along the cliff's wall'
        self.fail('Finish the test!')

# The page updates again, displaying both items on the list

# Wilson is presented with a URL unique to his list

# He visits the provided URL, and notices that his list is
# still there

# Satisfied, he closes the browser window

if __name__ == '__main__':
    unittest.main(warnings='ignore')
