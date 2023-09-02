import time

from pageObjects.LoginPage import LoginPage
from pageObjects.Homepage import HomePage
from TestData.data import Data
from selenium import webdriver
import pytest


class TestsEmployeeValidation:

    def test_loginpage(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(Data.url)
        self.driver.implicitly_wait(10)
        self.lp=LoginPage(self.driver)
        self.lp.userName(Data.username)
        self.lp.passWord(Data.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.ev=HomePage(self.driver)
        self.ev.Click_PIM()
        self.ev.Add_Employee(Data.firstName, Data.lastName)
        self.ev.Edit_Employee(Data.firstName, Data.changeLastName)
        time.sleep(5)
        self.ev.Delete_Employee(Data.firstName)
        self.driver.close()



