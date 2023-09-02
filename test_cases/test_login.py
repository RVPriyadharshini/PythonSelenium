import time
import logging

from pageObjects.LoginPage import LoginPage
from TestData.data import Data
from selenium import webdriver
import pytest


class TestsLogin:

    #Test to validate  user loggedin successfully
    def test_loginpage(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(Data.url)
        logging.log(1, "User Successfully launched the URL")
        self.driver.implicitly_wait(10)
        self.lp=LoginPage(self.driver)
        self.lp.userName(Data.username)
        self.lp.passWord(Data.password)
        self.lp.clickLogin()
        time.sleep(5)
        actual_title=self.driver.title

        if actual_title == "OrangeHRM":
            assert True
            logging.log(5, "Title of the Home Page is: " + actual_title)
        else:
            assert False

        logging.log(6, "User successfully logged into the OrangeHRM application")
        self.driver.close()

    #Test to validate the login failure functionality
    def test_loginfailure(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(Data.url)
        logging.log(1, "User Successfully launched the URL")
        self.driver.implicitly_wait(10)
        self.lp=LoginPage(self.driver)
        self.lp.userName(Data.username)
        self.lp.passWord(Data.wrngpswrd)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.geterrormsg()
        self.driver.close()





