from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class GetAttributes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com.br")
    def test_01(self):
        driver = self.driver
        emailFieldID = "email"
        passFieldID = "pass"

        emailFieldElement = WebDriverWait(driver, 8).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 8).until(lambda driver: driver.find_element_by_id(passFieldID))

        print emailFieldElement.get_attribute("name")
        print emailFieldElement.get_attribute("id")
        print emailFieldElement.get_attribute("class")

        print passFieldElement.get_attribute("name")
        print passFieldElement.get_attribute("id")
        print passFieldElement.get_attribute("class")
    def tearDown(self):
        self.driver.quit()
if __name__== "__name__":
    unittest.main()