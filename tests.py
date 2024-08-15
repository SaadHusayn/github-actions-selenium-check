from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
import unittest

# since server is headless i.e doesnot have screen so we have to consider this
opts = FirefoxOptions()
opts.add_argument('--headless')

driver = webdriver.Firefox(options=opts)

class CheckTests(unittest.TestCase):

    def test_title(self):
        driver.get('https://www.google.com/')
        self.assertEqual(driver.title, 'Google')


if __name__ == "__main__":
    unittest.main()