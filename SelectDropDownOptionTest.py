from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

import unittest
import time

class SelectDropDownOptionTest(unittest.TestCase):

    def setUp(self):
        self.driver =  webdriver.Firefox()
        self.driver.get("https://pt-br.facebook.com/")

    def test_SelectOption(self):
        driver = self.driver

        emailFieldID = "email"


        dayDropDownID = "day"
        monthDropDownID = "month"
        yearDropDownID = "year"


        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))



        monthDropDownElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(monthDropDownID))
        dayDropDownElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(dayDropDownID))
        yearDropDownElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(yearDropDownID))

        Select(dayDropDownElement).select_by_visible_text("11")
        Select(monthDropDownElement).select_by_visible_text("Ago")
        Select(yearDropDownElement).select_by_visible_text("1978")

        time.sleep(8)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()