from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest
import time

class LogonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://pt-br.facebook.com/")

    def test_Login(self):

        driver = self.driver
        facebookUserName = "your_email@domain.com"
        facebookPassword = "input_your_password"
        emailFieldID = "email"
        passFieldID = "pass"
        loginButtonXpass = '//input[@value="Entrar"]'
        fbLogoXpass = "(//a[contains(@href, 'logo')])[1]"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginBottonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpass))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUserName)
        time.sleep(1)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        time.sleep(1)
        loginBottonElement.click()
        _test = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpass))
        print type(_test)
        time.sleep(6)

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()