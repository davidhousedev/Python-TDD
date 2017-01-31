from selenium import webdriver
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
        self.fail('Finish the test!')

        # He has the opportunity to create a to-do list item

# Like any obedient developer, he creates a reminder to:
# 'Continue obeying the Test Goat'

# When he hits enter, the page updates and now lists his new
# to-do: '1: Continue obeying the Test Goat' as a to-do item

# There is still a text box inviting Wilson to add another item
# so he adds 'Step carefully along the cliff's wall'

# The page updates again, displaying both items on the list

# Wilson is presented with a URL unique to his list

# He visits the provided URL, and notices that his list is
# still there

# Satisfied, he closes the browser window

if __name__ == '__main__':
    unittest.main(warnings='ignore')