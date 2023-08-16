import time

from pageObjects.LoginPage import LoginPage
from pageObjects.Homepage import HomePage
from selenium import webdriver
import pytest


class TestsEmployeeValidation:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    wrngpswrd = "admin"
    firstName = "PriyaTest"
    lastName = "priya"
    changeLastName = "dharshini"

    def test_loginpage(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.lp=LoginPage(self.driver)
        self.lp.userName(self.username)
        self.lp.passWord(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.ev=HomePage(self.driver)
        self.ev.Click_PIM()
        self.ev.Add_Employee(self.firstName, self.lastName)
        self.ev.Edit_Employee(self.firstName, self.changeLastName)
        time.sleep(5)
        self.ev.Delete_Employee(self.firstName)



