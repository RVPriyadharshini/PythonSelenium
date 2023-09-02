import logging

from TestData import data
from TestLocators import locators
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def userName(self, username):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).clear()
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(
            username)
        logging.log(2, "user entered the user name")

    def passWord(self, password):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).clear()
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(
            password)
        logging.log(3, "user entered the Password")

    def clickLogin(self):
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        logging.log(4, "user Clicked the login button")

    def geterrormsg(self):
        err_msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().error_msg).text
        if err_msg == "Invalid credentials":
            assert True
        else:
            assert False
        logging.log(5, "user successfully validated the Invalid Credentials error message")










