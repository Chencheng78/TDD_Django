from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

MAX_WAIT = 10


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):


        self.fail('write me!')
