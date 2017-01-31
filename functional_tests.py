from selenium import webdriver

browser = webdriver.Firefox()

# Wilson opens his browser to his favorite to-do list app
browser.get('http://localhost:8000')

# He notices that he has reached the proper page
assert 'Django' in browser.title

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
