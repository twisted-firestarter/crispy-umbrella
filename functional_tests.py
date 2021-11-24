from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        new_item_input = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            new_item_input.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        new_item_input.send_keys('Buy peacock feathers')
        new_item_input.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        new_item_input = self.browser.find_element_by_id('id_new_item')
        new_item_input.send_keys('Use peacock feathers to make a fly')
        new_item_input.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')



if __name__ == '__main__':
    unittest.main()
