from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

driver = webdriver.Firefox()

class CheckTests(unittest.TestCase):

    def test_title(self):
        driver.get('https://www.google.com/')
        self.assertEqual(driver.title, 'Google')


if __name__ == "__main__":
    unittest.main()