from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time
MAX_WAIT = 10


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(' \n')
        self.get_item_input_box().send_keys(Keys.ENTER)

        time.sleep(3)
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Buy milk\n')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(0.5)

        self.check_for_row_in_list_table('1: Buy milk')

        self.get_item_input_box().send_keys(' \n')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(3)

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Make tea\n')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(0.5)

        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # enter a duplicated items.
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")
